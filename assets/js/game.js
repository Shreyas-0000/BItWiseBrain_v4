// Quiz Generation
async function generateQuestionsByLanguage() {
    try {
        const quizSettings = JSON.parse(localStorage.getItem('quizSettings'));
        if (!quizSettings) {
            throw new Error('Quiz settings not found');
        }

        const { language, questionLimit } = quizSettings;
        
        // Import API configuration
        const API_KEYS = await import('../../config/api_keys.js');
        
        // Build the QuizAPI.io URL
        let url = `${API_KEYS.default.QUIZ_API.baseUrl}/questions`;
        
        const params = new URLSearchParams({
            apiKey: API_KEYS.default.QUIZ_API.key,
            tags: language, // Using language as tag instead of category
            limit: questionLimit
        });
        
        url += '?' + params.toString();
        
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Failed to fetch questions from API');
        }
        
        const data = await response.json();
        
        if (!data || data.length === 0) {
            throw new Error('No questions returned from API');
        }
        
        return data.map(q => {
            // Create options array from the answers object
            const options = [];
            const answers = q.answers;
            
            // Add all non-null answers to options array
            Object.keys(answers).forEach(key => {
                if (answers[key] !== null) {
                    options.push(answers[key]);
                }
            });
            
            // Determine the correct answer
            const correctAnswers = q.correct_answers;
            let correctAnswer = '';
            
            Object.keys(correctAnswers).forEach(key => {
                if (correctAnswers[key] === 'true') {
                    // Extract the answer text from the corresponding answer
                    const answerKey = key.replace('_correct', '');
                    correctAnswer = q.answers[answerKey];
                }
            });
            
            return {
                id: q.id, // Store the question ID for tracking
                question: q.question,
                options: options,
                answer: correctAnswer,
                difficulty: q.difficulty || 'medium',
                category: q.tags && q.tags.length > 0 ? q.tags[0] : language
            };
        });
    } catch (error) {
        console.error('Error generating questions:', error);
        return [];
    }
}

// Main Quiz Logic
document.addEventListener('DOMContentLoaded', function() {
    const quizSettings = JSON.parse(localStorage.getItem('quizSettings'));
    if (!quizSettings) {
        window.location.href = 'quiz-setup.html';
        return;
    }

    const questionsContainer = document.getElementById('questions-container');
    const scoreElement = document.getElementById('score');
    const questionTemplate = document.getElementById('question-template');
    const questionsAnsweredElement = document.getElementById('questions-answered');
    const accuracyElement = document.getElementById('accuracy');
    const endQuizBtn = document.getElementById('end-quiz');
    const popup = document.getElementById('end-quiz-popup');
    const tryAgainBtn = document.getElementById('try-again');
    const finalQuestions = document.getElementById('final-questions');
    const finalAccuracy = document.getElementById('final-accuracy');
    const finalScore = document.getElementById('final-score');

    let score = 0;
    let correctAnswers = 0;
    let incorrectAnswers = 0;
    let questionsAnswered = 0;
    let currentQuestionIndex = 0;
    let questions = [];
    let answeredQuestionIds = new Set(); // Track answered question IDs
    let isLoading = false;
    let preloadTimeout = null;

    // Load previously answered questions from localStorage
    const loadAnsweredQuestions = () => {
        const language = quizSettings.language;
        const answeredKey = `answered_${language}_questions`;
        const storedAnsweredQuestions = localStorage.getItem(answeredKey);
        if (storedAnsweredQuestions) {
            try {
                const parsedIds = JSON.parse(storedAnsweredQuestions);
                if (Array.isArray(parsedIds)) {
                    parsedIds.forEach(id => answeredQuestionIds.add(id));
                }
            } catch (error) {
                console.error('Error parsing answered questions:', error);
            }
        }
    };

    // Save answered questions to localStorage
    const saveAnsweredQuestions = () => {
        const language = quizSettings.language;
        const answeredKey = `answered_${language}_questions`;
        localStorage.setItem(answeredKey, JSON.stringify([...answeredQuestionIds]));
    };

    // Initialize answered questions
    loadAnsweredQuestions();

    // Filter out previously answered questions
    const filterAnsweredQuestions = (allQuestions) => {
        if (answeredQuestionIds.size === 0) return allQuestions;
        
        return allQuestions.filter(q => q.id && !answeredQuestionIds.has(q.id));
    };

    // Quiz Initialization
    async function startQuiz() {
        try {
            questionsContainer.innerHTML = `
                <div class="question-slide">
                    <div id="boxed">
                        <h2 class="question-text">Loading questions...</h2>
                    </div>
                </div>
            `;

            await loadQuestions();
            setupKeyboardNavigation();
        } catch (error) {
            console.error('Error starting quiz:', error);
            showError();
        }
    }

    // Question Loading
    async function loadQuestions() {
        if (isLoading) return;
        isLoading = true;
        
        try {
            const allQuestions = await generateQuestionsByLanguage();
            
            if (allQuestions.length === 0) {
                throw new Error('No questions received from API');
            }

            // Filter out previously answered questions if possible
            const filteredQuestions = filterAnsweredQuestions(allQuestions);
            
            // If all questions have been answered before or we don't have enough new questions,
            // use the original questions and reset the tracking
            if (filteredQuestions.length < Math.min(5, quizSettings.questionLimit)) {
                questions = allQuestions;
                // Only clear tracking if we're completely out of questions
                if (filteredQuestions.length === 0) {
                    answeredQuestionIds.clear();
                    console.log('All questions have been answered before. Resetting tracking.');
                } else {
                    console.log(`Only ${filteredQuestions.length} new questions available. Using all questions.`);
                }
            } else {
                // We have enough new questions to use
                questions = filteredQuestions.slice(0, quizSettings.questionLimit);
                console.log(`Showing ${questions.length} new questions.`);
            }

            displayQuestions();
        } catch (error) {
            console.error('Error loading questions:', error);
            showError();
        } finally {
            isLoading = false;
        }
    }

    // Question Display
    function displayQuestions() {
        questionsContainer.innerHTML = '';
        
        questions.forEach((q, index) => {
            const slide = questionTemplate.content.cloneNode(true);
            
            // Use innerHTML for the formatted question
            const questionElement = slide.querySelector('.question-text');
            questionElement.innerHTML = decodeHTMLEntities(q.question);
            
            const difficultyElement = slide.querySelector('.difficulty');
            difficultyElement.textContent = q.difficulty;
            difficultyElement.className = `difficulty ${q.difficulty}`;
            
            const choicesContainer = slide.querySelector('.choices-container');
            q.options.forEach((option, choiceIndex) => {
                const choiceElement = document.createElement('div');
                choiceElement.className = 'choice-container';
                choiceElement.tabIndex = 0;
                choiceElement.setAttribute('data-question-index', index);
                choiceElement.setAttribute('data-choice-index', choiceIndex);
                
                // Create choice prefix
                const prefixSpan = document.createElement('span');
                prefixSpan.className = 'choice-prefix';
                prefixSpan.textContent = String.fromCharCode(65 + choiceIndex);
                
                // Create choice text with formatted HTML
                const textSpan = document.createElement('span');
                textSpan.className = 'choice-text';
                textSpan.innerHTML = decodeHTMLEntities(option);
                
                // Store the original option for answer checking
                textSpan.dataset.rawOption = option;
                
                // Append elements
                choiceElement.appendChild(prefixSpan);
                choiceElement.appendChild(textSpan);
                
                choiceElement.addEventListener('click', () => handleAnswer(choiceElement, option, q.answer, index));
                choiceElement.addEventListener('keydown', (e) => {
                    if (e.key === ' ' || e.key === 'Enter') {
                        e.preventDefault();
                        handleAnswer(choiceElement, option, q.answer, index);
                    }
                });
                
                choicesContainer.appendChild(choiceElement);
            });
            
            questionsContainer.appendChild(slide);
        });

        // After all questions are rendered, check for scrollbars and adjust container width if needed
        setTimeout(() => {
            adjustContainerWidths();
            setupContainerResizeObserver();
            addNavigationGuide();
        }, 100); // Small delay to ensure content is fully rendered
    }

    // Function to adjust container widths based on content
    function adjustContainerWidths() {
        const boxedElements = document.querySelectorAll('#boxed');
        boxedElements.forEach(boxed => {
            // Check if the element has a scrollbar
            const hasVerticalScrollbar = boxed.scrollHeight > boxed.clientHeight;
            const contentWidth = getContentWidth(boxed);
            
            if (hasVerticalScrollbar || contentWidth > 320) { // 320px is slightly less than the default width of 340px
                // Calculate how much extra width is needed
                const extraWidth = Math.min(300, Math.max(0, contentWidth - 320)); // Max 300px extra, min 0px
                
                // Adjust the slide and boxed element width
                const slide = boxed.closest('.question-slide');
                if (slide) {
                    // Increase width based on content needs, up to a maximum
                    const newWidth = Math.min(750, 380 + extraWidth);
                    slide.style.maxWidth = `${newWidth}px`;
                    boxed.style.width = `${newWidth - 40}px`; // Account for padding
                    
                    // Log the adjustment for debugging
                    console.log(`Adjusted container width to ${newWidth}px (content width: ${contentWidth}px)`);
                }
            }
        });
    }

    // Helper function to get the actual content width needed
    function getContentWidth(element) {
        // Check direct scrollWidth first as a quick method
        if (element.scrollWidth > element.clientWidth) {
            // Element already has horizontal overflow, use that as a starting point
            return element.scrollWidth;
        }
        
        // Create a temporary element to measure content width
        const tempDiv = document.createElement('div');
        tempDiv.style.position = 'absolute';
        tempDiv.style.visibility = 'hidden';
        tempDiv.style.width = '340px'; // Match the original container width
        tempDiv.style.padding = '20px'; // Match padding
        tempDiv.style.boxSizing = 'border-box';
        tempDiv.style.overflow = 'auto';
        tempDiv.innerHTML = element.innerHTML;
        
        document.body.appendChild(tempDiv);
        
        // Check if this temp div has scrollbars with the original width
        const hasScrollbar = tempDiv.scrollHeight > tempDiv.clientHeight;
        
        // Calculate extra width needed for horizontal content (long code snippets, etc.)
        const longestLineWidth = calculateLongestLineWidth(tempDiv);
        
        document.body.removeChild(tempDiv);
        
        // If we have scrollbars or content that needs more width, increase the container
        if (hasScrollbar || longestLineWidth > 300) { // 300px is the content area width (340px - 40px padding)
            // Return a larger width to accommodate the content
            return Math.min(750, longestLineWidth + 120); // Add extra space for padding/margins
        }
        
        return 340; // Default container width
    }
    
    // Function to find the longest line in an element with complex content
    function calculateLongestLineWidth(element) {
        // Check direct elements that might need more space
        let maxWidth = 0;
        
        // Look at code tags first as they often have the longest lines
        const codeTags = element.querySelectorAll('.code-tag');
        codeTags.forEach(codeTag => {
            // Create a temp span to measure this specific code tag
            const tempSpan = document.createElement('span');
            tempSpan.style.position = 'absolute';
            tempSpan.style.visibility = 'hidden';
            tempSpan.style.whiteSpace = 'nowrap'; // Prevent wrapping so we get the full width
            tempSpan.style.font = window.getComputedStyle(codeTag).font;
            tempSpan.textContent = codeTag.textContent; // Get the raw text
            
            document.body.appendChild(tempSpan);
            const width = tempSpan.getBoundingClientRect().width;
            document.body.removeChild(tempSpan);
            
            maxWidth = Math.max(maxWidth, width);
        });
        
        // Now check choice text and question text elements
        const textElements = element.querySelectorAll('.choice-text, .question-text');
        textElements.forEach(textEl => {
            // For text content, we'll split by lines and measure each line
            const lines = textEl.textContent.split('\n');
            lines.forEach(line => {
                const tempSpan = document.createElement('span');
                tempSpan.style.position = 'absolute';
                tempSpan.style.visibility = 'hidden';
                tempSpan.style.whiteSpace = 'nowrap';
                tempSpan.style.font = window.getComputedStyle(textEl).font;
                tempSpan.textContent = line;
                
                document.body.appendChild(tempSpan);
                const width = tempSpan.getBoundingClientRect().width;
                document.body.removeChild(tempSpan);
                
                maxWidth = Math.max(maxWidth, width);
            });
        });
        
        return maxWidth;
    }

    // Function to decode HTML entities and properly display HTML tags
    function decodeHTMLEntities(text) {
        if (!text) return '';
        
        // First decode HTML entities like &lt; to < and &gt; to >
        const textArea = document.createElement('textarea');
        textArea.innerHTML = text;
        let decodedText = textArea.value;
        
        // Replace HTML tags with formatted versions that look like code
        decodedText = decodedText.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        
        // Highlight HTML tags in code style
        decodedText = decodedText.replace(/&lt;(\/?[a-zA-Z][a-zA-Z0-9]*)(.*?)&gt;/g, '<span class="code-tag">&lt;$1$2&gt;</span>');
        
        // Create a div to hold the HTML with formatted tags
        const div = document.createElement('div');
        div.innerHTML = decodedText;
        
        // Return the text content with HTML tag highlighting
        return div.innerHTML;
    }

    // Answer Handling
    function handleAnswer(choiceElement, selectedAnswer, correctAnswer, questionIndex) {
        const questionSlide = choiceElement.closest('.question-slide');
        if (questionSlide.querySelector('.correct') || questionSlide.querySelector('.incorrect')) {
            return;
        }
        
        const isCorrect = selectedAnswer === correctAnswer;
        
        // Get the current question and mark it as answered
        const currentQuestion = questions[questionIndex];
        if (currentQuestion && currentQuestion.id) {
            answeredQuestionIds.add(currentQuestion.id);
            // Save to localStorage after each answer
            saveAnsweredQuestions();
        }
        
        if (isCorrect) {
            choiceElement.classList.add('correct');
            correctAnswers++;
            score += 10;
        } else {
            choiceElement.classList.add('incorrect');
            
            // Highlight correct answer
            const choices = questionSlide.querySelectorAll('.choice-container');
            choices.forEach(choice => {
                const choiceTextElement = choice.querySelector('.choice-text');
                const rawOption = choiceTextElement.dataset.rawOption;
                if (rawOption === correctAnswer) {
                    choice.classList.add('correct');
                }
            });
            
            incorrectAnswers++;
        }
        
        questionsAnswered++;
        currentQuestionIndex = questionIndex;
        
        updateUI();
        
        if (questionsAnswered === questions.length) {
            setTimeout(() => {
                showEndQuizPopup();
            }, 1000);
        } else if (currentQuestionIndex < questions.length - 1) {
            setTimeout(() => {
                scrollToNextQuestion();
            }, 1500);
        }
    }

    // UI Update
    function updateUI() {
        scoreElement.textContent = score;
        questionsAnsweredElement.textContent = `${questionsAnswered}/${questions.length}`;
        
        const accuracy = questionsAnswered > 0 
            ? Math.round((correctAnswers / questionsAnswered) * 100) 
            : 0;
        
        accuracyElement.textContent = `${accuracy}%`;
    }

    // Navigation
    function setupKeyboardNavigation() {
        document.addEventListener('keydown', handleKeyboardNavigation);
        
        // Add navigation guide
        addNavigationGuide();
        
        // Ensure the hamburger menu toggle functionality works
        const hamburger = document.querySelector('.hamburger');
        const navbar = document.querySelector('.left-navbar');
        
        if (hamburger && navbar) {
            hamburger.addEventListener('click', () => {
                navbar.classList.toggle('expanded');
            });
        }
    }
    
    // Handle keyboard navigation
    function handleKeyboardNavigation(e) {
        // Get the current focused element
        const activeElement = document.activeElement;
        
        // Handle different key presses
        switch (e.key) {
            case 'Tab':
                // Prevent default tab behavior to implement custom focus control
                e.preventDefault();
                
                // If shift is pressed, go to previous option
                if (e.shiftKey) {
                    navigateToPreviousOption(activeElement);
                } else {
                    navigateToNextOption(activeElement);
                }
                break;
                
            case 'ArrowUp':
                e.preventDefault();
                scrollToPreviousQuestion();
                break;
                
            case 'ArrowDown':
                e.preventDefault();
                scrollToNextQuestion();
                break;
                
            case 'Escape':
                e.preventDefault();
                endQuiz();
                break;
        }
    }
    
    // Navigate to the next option in the current question
    function navigateToNextOption(currentElement) {
        // Get the visible question index
        currentQuestionIndex = getCurrentQuestionIndex();
        
        if (!currentElement || !currentElement.classList.contains('choice-container')) {
            // If no option is focused, focus the first option of the current visible question
            const currentQuestion = document.querySelectorAll('.question-slide')[currentQuestionIndex];
            const firstOption = currentQuestion.querySelector('.choice-container');
            if (firstOption) {
                firstOption.focus();
            }
            return;
        }
        
        // Get current question index and choice index
        const questionIndex = parseInt(currentElement.getAttribute('data-question-index'));
        const choiceIndex = parseInt(currentElement.getAttribute('data-choice-index'));
        
        // If we're already on the visible question, navigate within it
        if (questionIndex === currentQuestionIndex) {
            // Find all choices in the current question
            const currentQuestion = document.querySelectorAll('.question-slide')[questionIndex];
            const choices = currentQuestion.querySelectorAll('.choice-container');
            
            // Focus the next choice, or loop back to the first choice
            const nextIndex = (choiceIndex + 1) % choices.length;
            choices[nextIndex].focus();
        } else {
            // If we're not on the visible question, focus the first option of the visible question
            const currentQuestion = document.querySelectorAll('.question-slide')[currentQuestionIndex];
            const firstOption = currentQuestion.querySelector('.choice-container');
            if (firstOption) {
                firstOption.focus();
            }
        }
    }
    
    // Navigate to the previous option in the current question
    function navigateToPreviousOption(currentElement) {
        // Get the visible question index
        currentQuestionIndex = getCurrentQuestionIndex();
        
        if (!currentElement || !currentElement.classList.contains('choice-container')) {
            // If no option is focused, focus the last option of the current visible question
            const currentQuestion = document.querySelectorAll('.question-slide')[currentQuestionIndex];
            const allOptions = currentQuestion.querySelectorAll('.choice-container');
            const lastOption = allOptions[allOptions.length - 1];
            if (lastOption) {
                lastOption.focus();
            }
            return;
        }
        
        // Get current question index and choice index
        const questionIndex = parseInt(currentElement.getAttribute('data-question-index'));
        const choiceIndex = parseInt(currentElement.getAttribute('data-choice-index'));
        
        // If we're already on the visible question, navigate within it
        if (questionIndex === currentQuestionIndex) {
            // Find all choices in the current question
            const currentQuestion = document.querySelectorAll('.question-slide')[questionIndex];
            const choices = currentQuestion.querySelectorAll('.choice-container');
            
            // Focus the previous choice, or loop back to the last choice
            const prevIndex = (choiceIndex - 1 + choices.length) % choices.length;
            choices[prevIndex].focus();
        } else {
            // If we're not on the visible question, focus the last option of the visible question
            const currentQuestion = document.querySelectorAll('.question-slide')[currentQuestionIndex];
            const allOptions = currentQuestion.querySelectorAll('.choice-container');
            const lastOption = allOptions[allOptions.length - 1];
            if (lastOption) {
                lastOption.focus();
            }
        }
    }

    // Helper function to get current question index based on scroll position
    function getCurrentQuestionIndex() {
        const slides = document.querySelectorAll('.question-slide');
        const containerRect = document.querySelector('.container').getBoundingClientRect();
        const containerCenter = containerRect.top + containerRect.height / 2;
        
        let closestSlideIndex = 0;
        let minDistance = Infinity;
        
        slides.forEach((slide, index) => {
            const slideRect = slide.getBoundingClientRect();
            const slideCenter = slideRect.top + slideRect.height / 2;
            const distance = Math.abs(slideCenter - containerCenter);
            
            if (distance < minDistance) {
                minDistance = distance;
                closestSlideIndex = index;
            }
        });
        
        return closestSlideIndex;
    }

    function scrollToPreviousQuestion() {
        if (currentQuestionIndex > 0) {
            currentQuestionIndex--;
            const slides = document.querySelectorAll('.question-slide');
            slides[currentQuestionIndex].scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    function scrollToNextQuestion() {
        if (currentQuestionIndex < questions.length - 1) {
            currentQuestionIndex++;
            const slides = document.querySelectorAll('.question-slide');
            slides[currentQuestionIndex].scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // Helper function to get current slide (used in keyboard navigation)
    function getCurrentSlide() {
        const slides = document.querySelectorAll('.question-slide');
        return slides[currentQuestionIndex];
    }

    // Quiz End
    function endQuiz() {
        showEndQuizPopup();
    }

    function showError() {
        questionsContainer.innerHTML = `
            <div class="question-slide">
                <div id="boxed" class="error">
                    <h2 class="question-text">Error loading questions</h2>
                    <p>Please try again or select different quiz settings.</p>
                    <button onclick="window.location.href='quiz-setup.html'" class="retry-btn">
                        Try Again
                    </button>
                </div>
            </div>
        `;
    }

    function showEndQuizPopup() {
        finalQuestions.textContent = `${questionsAnswered}/${questions.length}`;
        finalAccuracy.textContent = accuracyElement.textContent;
        finalScore.textContent = score;

        popup.classList.add('active');

        // Save quiz results to localStorage
        const previousResults = JSON.parse(localStorage.getItem('quizResults') || '{"totalQuestions": 0, "correctAnswers": 0}');
        
        const updatedResults = {
            totalQuestions: previousResults.totalQuestions + questionsAnswered,
            correctAnswers: previousResults.correctAnswers + correctAnswers
        };
        
        localStorage.setItem('quizResults', JSON.stringify(updatedResults));
    }

    endQuizBtn.addEventListener('click', endQuiz);
    tryAgainBtn.addEventListener('click', () => {
        window.location.href = 'quiz-setup.html';
    });

    startQuiz();

    // After container adjustments, monitor for any layout changes
    function setupContainerResizeObserver() {
        // Set up a resize observer to monitor container size changes
        if ('ResizeObserver' in window) {
            const resizeObserver = new ResizeObserver(entries => {
                // If any observed element changes size, recalculate container widths
                adjustContainerWidths();
            });
            
            // Observe each question container
            document.querySelectorAll('#boxed').forEach(container => {
                resizeObserver.observe(container);
            });
        }
        
        // Also listen for window resize events
        window.addEventListener('resize', adjustContainerWidths);
    }

    // Function to add navigation guide
    function addNavigationGuide() {
        // Check if guide already exists
        if (document.getElementById('navigation-guide')) {
            return;
        }
        
        // Create the navigation guide container
        const guideContainer = document.createElement('div');
        guideContainer.id = 'navigation-guide';
        guideContainer.className = 'navigation-guide';
        
        // Add the guide content
        guideContainer.innerHTML = `
            <div class="guide-header">
                <h3>Keyboard Navigation</h3>
                <button id="close-guide" aria-label="Close navigation guide">×</button>
            </div>
            <div class="guide-content">
                <div class="shortcut-item">
                    <span class="key">Tab</span>
                    <span class="key-desc">Next option</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Shift + Tab</span>
                    <span class="key-desc">Previous option</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Enter / Space</span>
                    <span class="key-desc">Select option</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">↓</span>
                    <span class="key-desc">Next question</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">↑</span>
                    <span class="key-desc">Previous question</span>
                </div>
                <div class="shortcut-item">
                    <span class="key">Esc</span>
                    <span class="key-desc">End quiz</span>
                </div>
            </div>
        `;
        
        // Add the guide to the page
        document.body.appendChild(guideContainer);
        
        // Add event listener to close button
        const closeButton = document.getElementById('close-guide');
        closeButton.addEventListener('click', () => {
            guideContainer.classList.add('hidden');
        });
    }
});
