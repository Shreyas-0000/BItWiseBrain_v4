import random
import time
from typing import List, Dict, Any
import sys

class PythonPuzzles:
    def __init__(self):
        self.current_level = 1
        self.score = 0
        self.puzzles = {
            1: {
                "name": "Basic Variables",
                "description": "Learn about variables and basic data types",
                "puzzles": [
                    {
                        "question": "Create a variable named 'age' and assign it the value 25",
                        "solution": "age = 25",
                        "hint": "Use the assignment operator =",
                        "test": lambda code: "age = 25" in code
                    },
                    {
                        "question": "Create a variable named 'name' and assign it your name as a string",
                        "solution": "name = 'Your Name'",
                        "hint": "Use quotes for strings",
                        "test": lambda code: "name =" in code and ("'" in code or '"' in code)
                    }
                ]
            },
            2: {
                "name": "Basic Operations",
                "description": "Learn about arithmetic operations",
                "puzzles": [
                    {
                        "question": "Calculate the sum of 10 and 20 and store it in a variable 'result'",
                        "solution": "result = 10 + 20",
                        "hint": "Use the + operator",
                        "test": lambda code: "result =" in code and "+" in code
                    },
                    {
                        "question": "Calculate the product of 5 and 3 and store it in a variable 'product'",
                        "solution": "product = 5 * 3",
                        "hint": "Use the * operator",
                        "test": lambda code: "product =" in code and "*" in code
                    }
                ]
            },
            3: {
                "name": "Conditional Statements",
                "description": "Learn about if-else statements",
                "puzzles": [
                    {
                        "question": "Write an if statement that checks if a variable 'age' is greater than 18",
                        "solution": "if age > 18:\n    print('Adult')",
                        "hint": "Use if and > operator",
                        "test": lambda code: "if" in code and ">" in code
                    },
                    {
                        "question": "Write an if-else statement that checks if a number is even or odd",
                        "solution": "if number % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
                        "hint": "Use if-else and modulo operator %",
                        "test": lambda code: "if" in code and "else" in code and "%" in code
                    }
                ]
            },
            4: {
                "name": "Loops",
                "description": "Learn about for and while loops",
                "puzzles": [
                    {
                        "question": "Write a for loop that prints numbers from 1 to 5",
                        "solution": "for i in range(1, 6):\n    print(i)",
                        "hint": "Use for and range()",
                        "test": lambda code: "for" in code and "range" in code
                    },
                    {
                        "question": "Write a while loop that counts down from 5 to 1",
                        "solution": "count = 5\nwhile count > 0:\n    print(count)\n    count -= 1",
                        "hint": "Use while and decrement operator",
                        "test": lambda code: "while" in code and "-=" in code
                    }
                ]
            },
            5: {
                "name": "Lists",
                "description": "Learn about list operations",
                "puzzles": [
                    {
                        "question": "Create a list named 'fruits' with three fruits",
                        "solution": "fruits = ['apple', 'banana', 'orange']",
                        "hint": "Use square brackets and commas",
                        "test": lambda code: "fruits =" in code and "[" in code and "]" in code
                    },
                    {
                        "question": "Add 'grape' to the fruits list",
                        "solution": "fruits.append('grape')",
                        "hint": "Use append() method",
                        "test": lambda code: "append" in code
                    }
                ]
            },
            6: {
                "name": "Functions",
                "description": "Learn about function definition and calling",
                "puzzles": [
                    {
                        "question": "Define a function named 'greet' that takes a name parameter and prints 'Hello, {name}!'",
                        "solution": "def greet(name):\n    print(f'Hello, {name}!')",
                        "hint": "Use def and f-string",
                        "test": lambda code: "def greet" in code and "f'" in code
                    },
                    {
                        "question": "Define a function named 'add' that takes two parameters and returns their sum",
                        "solution": "def add(a, b):\n    return a + b",
                        "hint": "Use def and return",
                        "test": lambda code: "def add" in code and "return" in code
                    }
                ]
            },
            7: {
                "name": "Dictionaries",
                "description": "Learn about dictionary operations",
                "puzzles": [
                    {
                        "question": "Create a dictionary named 'person' with keys 'name' and 'age'",
                        "solution": "person = {'name': 'John', 'age': 30}",
                        "hint": "Use curly braces and key-value pairs",
                        "test": lambda code: "person =" in code and "{" in code and "}" in code
                    },
                    {
                        "question": "Add a new key 'city' with value 'New York' to the person dictionary",
                        "solution": "person['city'] = 'New York'",
                        "hint": "Use square bracket notation",
                        "test": lambda code: "person[" in code and "]" in code
                    }
                ]
            },
            8: {
                "name": "Object-Oriented Programming",
                "description": "Learn about classes and objects",
                "puzzles": [
                    {
                        "question": "Define a class named 'Car' with attributes 'brand' and 'model'",
                        "solution": "class Car:\n    def __init__(self, brand, model):\n        self.brand = brand\n        self.model = model",
                        "hint": "Use class and __init__",
                        "test": lambda code: "class Car" in code and "__init__" in code
                    },
                    {
                        "question": "Add a method 'start_engine' to the Car class that prints 'Engine started'",
                        "solution": "def start_engine(self):\n    print('Engine started')",
                        "hint": "Define a method with self parameter",
                        "test": lambda code: "def start_engine" in code and "self" in code
                    }
                ]
            }
        }

    def display_welcome(self):
        print("\n=== Welcome to Python Puzzle Learning System ===")
        print("Learn Python programming through interactive puzzles!")
        print("Each level focuses on different Python concepts.")
        print("Complete puzzles to advance to the next level.\n")

    def display_level_info(self):
        level_info = self.puzzles[self.current_level]
        print(f"\n=== Level {self.current_level}: {level_info['name']} ===")
        print(f"Description: {level_info['description']}")
        print(f"Current Score: {self.score}\n")

    def get_user_input(self) -> str:
        print("Enter your code (press Ctrl+D or Ctrl+Z to finish):")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        return "\n".join(lines)

    def run_puzzle(self, puzzle: Dict[str, Any]) -> bool:
        print(f"\nPuzzle: {puzzle['question']}")
        print(f"Hint: {puzzle['hint']}")
        
        user_code = self.get_user_input()
        
        try:
            if puzzle['test'](user_code):
                print("\nCorrect! Well done!")
                print(f"Solution: {puzzle['solution']}")
                return True
            else:
                print("\nNot quite right. Try again!")
                return False
        except Exception as e:
            print(f"\nError in your code: {str(e)}")
            return False

    def run_level(self) -> bool:
        level_info = self.puzzles[self.current_level]
        all_correct = True
        
        for puzzle in level_info['puzzles']:
            if not self.run_puzzle(puzzle):
                all_correct = False
                break
        
        if all_correct:
            self.score += 10
            print(f"\nCongratulations! You've completed Level {self.current_level}!")
            return True
        else:
            print(f"\nKeep practicing Level {self.current_level}!")
            return False

    def run(self):
        self.display_welcome()
        
        while self.current_level <= len(self.puzzles):
            self.display_level_info()
            
            if self.run_level():
                if self.current_level < len(self.puzzles):
                    self.current_level += 1
                else:
                    print("\nCongratulations! You've completed all levels!")
                    break
            
            choice = input("\nDo you want to continue? (y/n): ")
            if choice.lower() != 'y':
                break
        
        print(f"\nFinal Score: {self.score}")
        print("Thanks for learning Python with puzzles!")

if __name__ == "__main__":
    puzzle = PythonPuzzle()
    puzzle.run() 