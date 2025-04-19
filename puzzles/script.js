// Puzzle data structure
const puzzles = {
    1: {
        name: "Basic Variables",
        description: "Learn about variables and basic data types",
        puzzles: [
            {
                question: "Create a variable named 'age' and assign it the value 25",
                solution: "age = 25",
                hint: "Use the assignment operator =",
                test: (code) => code.includes("age = 25")
            },
            {
                question: "Create a variable named 'name' and assign it your name as a string",
                solution: "name = 'Your Name'",
                hint: "Use quotes for strings",
                test: (code) => code.includes("name =") && (code.includes("'") || code.includes('"'))
            }
        ]
    },
    2: {
        name: "Basic Operations",
        description: "Learn about arithmetic operations",
        puzzles: [
            {
                question: "Calculate the sum of 10 and 20 and store it in a variable 'result'",
                solution: "result = 10 + 20",
                hint: "Use the + operator",
                test: (code) => code.includes("result =") && code.includes("+")
            },
            {
                question: "Calculate the product of 5 and 3 and store it in a variable 'product'",
                solution: "product = 5 * 3",
                hint: "Use the * operator",
                test: (code) => code.includes("product =") && code.includes("*")
            }
        ]
    },
    3: {
        name: "Conditional Statements",
        description: "Learn about if-else statements",
        puzzles: [
            {
                question: "Write an if statement that checks if a variable 'age' is greater than 18",
                solution: "if age > 18:\n    print('Adult')",
                hint: "Use if and > operator",
                test: (code) => code.includes("if") && code.includes(">")
            },
            {
                question: "Write an if-else statement that checks if a number is even or odd",
                solution: "if number % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
                hint: "Use if-else and modulo operator %",
                test: (code) => code.includes("if") && code.includes("else") && code.includes("%")
            }
        ]
    },
    4: {
        name: "Loops",
        description: "Learn about for and while loops",
        puzzles: [
            {
                question: "Write a for loop that prints numbers from 1 to 5",
                solution: "for i in range(1, 6):\n    print(i)",
                hint: "Use for and range()",
                test: (code) => code.includes("for") && code.includes("range")
            },
            {
                question: "Write a while loop that counts down from 5 to 1",
                solution: "count = 5\nwhile count > 0:\n    print(count)\n    count -= 1",
                hint: "Use while and decrement operator",
                test: (code) => code.includes("while") && code.includes("-=")
            }
        ]
    },
    5: {
        name: "Lists",
        description: "Learn about list operations",
        puzzles: [
            {
                question: "Create a list named 'fruits' with three fruits",
                solution: "fruits = ['apple', 'banana', 'orange']",
                hint: "Use square brackets and commas",
                test: (code) => code.includes("fruits =") && code.includes("[") && code.includes("]")
            },
            {
                question: "Add 'grape' to the fruits list",
                solution: "fruits.append('grape')",
                hint: "Use append() method",
                test: (code) => code.includes("append")
            }
        ]
    },
    6: {
        name: "Functions",
        description: "Learn about function definition and calling",
        puzzles: [
            {
                question: "Define a function named 'greet' that takes a name parameter and prints 'Hello, {name}!'",
                solution: "def greet(name):\n    print(f'Hello, {name}!')",
                hint: "Use def and f-string",
                test: (code) => code.includes("def greet") && code.includes("f'")
            },
            {
                question: "Define a function named 'add' that takes two parameters and returns their sum",
                solution: "def add(a, b):\n    return a + b",
                hint: "Use def and return",
                test: (code) => code.includes("def add") && code.includes("return")
            }
        ]
    },
    7: {
        name: "Dictionaries",
        description: "Learn about dictionary operations",
        puzzles: [
            {
                question: "Create a dictionary named 'person' with keys 'name' and 'age'",
                solution: "person = {'name': 'John', 'age': 30}",
                hint: "Use curly braces and key-value pairs",
                test: (code) => code.includes("person =") && code.includes("{") && code.includes("}")
            },
            {
                question: "Add a new key 'city' with value 'New York' to the person dictionary",
                solution: "person['city'] = 'New York'",
                hint: "Use square bracket notation",
                test: (code) => code.includes("person[")
            }
        ]
    },
    8: {
        name: "Object-Oriented Programming",
        description: "Learn about classes and objects",
        puzzles: [
            {
                question: "Define a class named 'Car' with attributes 'brand' and 'model'",
                solution: "class Car:\n    def __init__(self, brand, model):\n        self.brand = brand\n        self.model = model",
                hint: "Use class and __init__",
                test: (code) => code.includes("class Car") && code.includes("__init__")
            },
            {
                question: "Add a method 'start_engine' to the Car class that prints 'Engine started'",
                solution: "def start_engine(self):\n    print('Engine started')",
                hint: "Define a method with self parameter",
                test: (code) => code.includes("def start_engine") && code.includes("self")
            }
        ]
    }
};

class PuzzleGame {
    constructor() {
        this.currentLevel = 1;
        this.currentPuzzleIndex = 0;
        this.score = 0;
        this.initializeUI();
        this.setupEventListeners();
        this.showTutorial();
    }

    initializeUI() {
        this.updateLevelInfo();
        this.updatePuzzleInfo();
        this.updateNavigationButtons();
        this.updateProgress();
    }

    setupEventListeners() {
        document.getElementById('run-code').addEventListener('click', () => this.runCode());
        document.getElementById('show-solution').addEventListener('click', () => this.showSolution());
        document.getElementById('prev-level').addEventListener('click', () => this.previousLevel());
        document.getElementById('next-level').addEventListener('click', () => this.nextLevel());
        document.getElementById('show-hint').addEventListener('click', () => this.toggleHint());
        document.getElementById('format-code').addEventListener('click', () => this.formatCode());
        document.getElementById('clear-code').addEventListener('click', () => this.clearCode());
        document.getElementById('clear-output').addEventListener('click', () => this.clearOutput());
        document.getElementById('copy-solution').addEventListener('click', () => this.copySolution());
    }

    updateLevelInfo() {
        const level = puzzles[this.currentLevel];
        document.getElementById('level-title').textContent = `Level ${this.currentLevel}: ${level.name}`;
        document.getElementById('level-description').textContent = level.description;
        document.getElementById('score').textContent = this.score;
        document.getElementById('puzzle-progress').textContent = `Puzzle ${this.currentPuzzleIndex + 1}/${level.puzzles.length}`;
        document.getElementById('level-status').textContent = this.currentPuzzleIndex === level.puzzles.length - 1 ? 'Final Puzzle' : 'In Progress';
    }

    updateProgress() {
        const totalLevels = Object.keys(puzzles).length;
        const progress = ((this.currentLevel - 1) * 100) / totalLevels;
        document.getElementById('progress-fill').style.width = `${progress}%`;
        document.getElementById('progress-text').textContent = `Level ${this.currentLevel}/${totalLevels}`;
    }

    updatePuzzleInfo() {
        const puzzle = this.getCurrentPuzzle();
        document.getElementById('puzzle-question').textContent = puzzle.question;
        document.getElementById('puzzle-hint').textContent = puzzle.hint;
        document.getElementById('code-input').value = '';
        document.getElementById('output').textContent = '';
        document.getElementById('hint-content').classList.add('hidden');
    }

    updateNavigationButtons() {
        document.getElementById('prev-level').disabled = this.currentLevel === 1;
        document.getElementById('next-level').disabled = 
            this.currentLevel === Object.keys(puzzles).length && 
            this.currentPuzzleIndex === puzzles[this.currentLevel].puzzles.length - 1;
    }

    getCurrentPuzzle() {
        return puzzles[this.currentLevel].puzzles[this.currentPuzzleIndex];
    }

    runCode() {
        const code = document.getElementById('code-input').value;
        const puzzle = this.getCurrentPuzzle();
        const output = document.getElementById('output');

        try {
            if (puzzle.test(code)) {
                output.textContent = "Correct! Well done!";
                output.style.color = "#27ae60";
                this.score += 5;
                this.updateLevelInfo();
                this.updateProgress();
                
                if (this.currentPuzzleIndex < puzzles[this.currentLevel].puzzles.length - 1) {
                    this.currentPuzzleIndex++;
                    this.updatePuzzleInfo();
                } else {
                    this.nextLevel();
                }
            } else {
                output.textContent = "Not quite right. Try again!";
                output.style.color = "#e74c3c";
            }
        } catch (error) {
            output.textContent = `Error: ${error.message}`;
            output.style.color = "#e74c3c";
        }
    }

    showSolution() {
        const puzzle = this.getCurrentPuzzle();
        document.getElementById('solution-code').textContent = puzzle.solution;
        document.getElementById('solution-modal').style.display = 'block';
    }

    toggleHint() {
        const hintContent = document.getElementById('hint-content');
        hintContent.classList.toggle('hidden');
    }

    formatCode() {
        const codeInput = document.getElementById('code-input');
        const code = codeInput.value;
        // Basic formatting - add proper indentation
        const formattedCode = code.split('\n').map(line => line.trim()).join('\n');
        codeInput.value = formattedCode;
    }

    clearCode() {
        document.getElementById('code-input').value = '';
    }

    clearOutput() {
        document.getElementById('output').textContent = '';
    }

    copySolution() {
        const solutionCode = document.getElementById('solution-code').textContent;
        navigator.clipboard.writeText(solutionCode).then(() => {
            const button = document.getElementById('copy-solution');
            const originalText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-check"></i> Copied!';
            setTimeout(() => {
                button.innerHTML = originalText;
            }, 2000);
        });
    }

    previousLevel() {
        if (this.currentLevel > 1) {
            this.currentLevel--;
            this.currentPuzzleIndex = 0;
            this.updateLevelInfo();
            this.updatePuzzleInfo();
            this.updateNavigationButtons();
            this.updateProgress();
        }
    }

    nextLevel() {
        const maxLevel = Object.keys(puzzles).length;
        if (this.currentLevel < maxLevel) {
            this.currentLevel++;
            this.currentPuzzleIndex = 0;
            this.updateLevelInfo();
            this.updatePuzzleInfo();
            this.updateNavigationButtons();
            this.updateProgress();
        }
    }

    showTutorial() {
        document.getElementById('tutorial-modal').style.display = 'block';
    }
}

function closeModal() {
    document.getElementById('solution-modal').style.display = 'none';
}

function closeTutorial() {
    document.getElementById('tutorial-modal').style.display = 'none';
}

// Initialize the game when the page loads
window.addEventListener('load', () => {
    new PuzzleGame();
}); 