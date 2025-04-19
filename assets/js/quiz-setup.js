document.addEventListener('DOMContentLoaded', function() {
    // Navbar functionality
    const hamburger = document.querySelector('.hamburger');
    const navbar = document.querySelector('.left-navbar');
    const content = document.querySelector('.content-wrapper');

    hamburger.addEventListener('click', () => {
        navbar.classList.toggle('collapsed');
        content.classList.toggle('expanded');
    });

    // Get stored quiz results if they exist
    const previousResults = JSON.parse(localStorage.getItem('quizResults') || '{"totalQuestions": 0, "correctAnswers": 0}');
    const questionsElement = document.querySelector('.score-item:first-child .score-value');
    const accuracyElement = document.querySelector('.score-item:last-child .score-value');

    // Update score display
    function updateScoreDisplay() {
        const accuracy = previousResults.totalQuestions > 0 
            ? Math.round((previousResults.correctAnswers / previousResults.totalQuestions) * 100) 
            : 0;
        
        questionsElement.textContent = previousResults.totalQuestions;
        accuracyElement.textContent = `${accuracy}%`;
    }

    // Initialize score display
    updateScoreDisplay();

    // Quiz setup functionality
    const languageSelect = document.getElementById('language');
    const questionLimitSelect = document.getElementById('question-limit');
    const startButton = document.getElementById('start-quiz');

    // Check if all options are selected
    function checkFormValidity() {
        const isValid = languageSelect.value && questionLimitSelect.value;
        startButton.disabled = !isValid;
    }

    // Handle language selection
    languageSelect.addEventListener('change', () => {
        // Remove the default "Select language" option when any language is selected
        if (languageSelect.value) {
            const defaultOption = languageSelect.querySelector('option[value=""]');
            if (defaultOption) {
                defaultOption.remove();
            }
        }
        checkFormValidity();
    });

    // Handle question limit selection
    questionLimitSelect.addEventListener('change', checkFormValidity);

    // Initialize question limit value if it has a preselected value
    if (questionLimitSelect.options[questionLimitSelect.selectedIndex].value) {
        // Trigger the changed animation for the preselected value
        const questionLimitWrapper = questionLimitSelect.closest('.select-wrapper');
        questionLimitWrapper.classList.add('changed');
        setTimeout(() => {
            questionLimitWrapper.classList.remove('changed');
        }, 1000);
    }

    // Check form validity immediately to enable button if question limit is pre-selected
    checkFormValidity();

    // Add keyboard navigation for the form
    function setupKeyboardNavigation() {
        // Set initial focus on language select on page load
        languageSelect.focus();
        
        // Auto-open dropdown when focused
        languageSelect.addEventListener('focus', () => {
            languageSelect.size = 5; // Show 5 options
            languageSelect.click(); // Simulate click to open dropdown
        });
        
        languageSelect.addEventListener('blur', () => {
            languageSelect.size = 1; // Reset to normal select
        });
        
        // Handle enter key on selects to focus next element
        languageSelect.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                questionLimitSelect.focus();
            }
        });
        
        // Auto-open dropdown when focused
        questionLimitSelect.addEventListener('focus', () => {
            questionLimitSelect.size = 5; // Show 5 options
            questionLimitSelect.click(); // Simulate click to open dropdown
        });
        
        questionLimitSelect.addEventListener('blur', () => {
            questionLimitSelect.size = 1; // Reset to normal select
        });
        
        questionLimitSelect.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                if (!startButton.disabled) {
                    startButton.focus();
                }
            }
        });
        
        // Allow starting quiz with Enter key when button is focused
        startButton.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !startButton.disabled) {
                e.preventDefault();
                startQuiz();
            }
        });
        
        // Add global Ctrl+Enter shortcut to start quiz if form is valid
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey && e.key === 'Enter' && !startButton.disabled) {
                e.preventDefault();
                startQuiz();
            }
        });
    }

    // Enhance select dropdowns with animations
    const selectWrappers = document.querySelectorAll('.select-wrapper');
    
    selectWrappers.forEach(wrapper => {
        const select = wrapper.querySelector('select');
        
        // Add focus effects
        select.addEventListener('focus', () => {
            wrapper.classList.add('focused');
        });
        
        select.addEventListener('blur', () => {
            wrapper.classList.remove('focused');
        });
        
        // Add change animation
        select.addEventListener('change', () => {
            wrapper.classList.add('changed');
            setTimeout(() => {
                wrapper.classList.remove('changed');
            }, 1000);
        });
    });

    // Function to start the quiz
    function startQuiz() {
        const quizSettings = {
            language: languageSelect.value,
            questionLimit: parseInt(questionLimitSelect.value)
        };
        
        // Save settings to localStorage
        localStorage.setItem('quizSettings', JSON.stringify(quizSettings));
        
        // Redirect to quiz page with animation
        startButton.textContent = 'Starting Quiz...';
        startButton.style.opacity = '0.7';
        startButton.disabled = true;
        
        setTimeout(() => {
            window.location.href = 'game.html';
        }, 500);
    }

    // Handle form submission
    startButton.addEventListener('click', () => {
        if (!startButton.disabled) {
            startQuiz();
        }
    });

    // Add animations for form elements
    function addEntryAnimations() {
        const formGroups = document.querySelectorAll('.form-group');
        formGroups.forEach((group, index) => {
            group.style.opacity = '0';
            group.style.transform = 'translateY(20px)';
            setTimeout(() => {
                group.style.transition = 'all 0.5s ease';
                group.style.opacity = '1';
                group.style.transform = 'translateY(0)';
            }, index * 200);
        });
    }

    // Initialize animations
    addEntryAnimations();
    
    // Setup keyboard navigation
    setupKeyboardNavigation();
});
