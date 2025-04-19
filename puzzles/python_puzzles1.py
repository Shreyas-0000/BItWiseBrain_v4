{
    "name": "Python Variables & Data Types",
    "description": "Explore Python's variable declaration and different data types through engaging puzzles.",
    "puzzles": [
        {
            "question": "Declare a variable named 'age' and assign it the value 25.",
            "solution": "age = 25",
            "hint": "Use the assignment operator '=' to assign values to variables.",
            "test": "'age' in code and '=' in code"
        },
        {
            "question": "What will be the data type of the variable 'pi' after executing: pi = 3.14?",
            "solution": "float",
            "hint": "Numbers with decimal points are considered floating-point numbers.",
            "test": "'float' in answer"
        },
        {
            "question": "Convert the string '100' to an integer.",
            "solution": "num = int('100')",
            "hint": "Use the int() function to convert a string to an integer.",
            "test": "'int(' in code"
        },
        {
            "question": "Check the data type of the variable 'x' if x = True.",
            "solution": "bool",
            "hint": "True and False belong to a special data type.",
            "test": "'bool' in answer"
        },
        {
            "question": "Declare a list named 'fruits' containing 'apple', 'banana', and 'cherry'.",
            "solution": "fruits = ['apple', 'banana', 'cherry']",
            "hint": "Use square brackets to define a list.",
            "test": "'fruits' in code and '[' in code and ']' in code"
        },
        {
            "question": "What is the output of type(None)?",
            "solution": "<class 'NoneType'>",
            "hint": "None represents the absence of a value.",
            "test": "'NoneType' in answer"
        },
        {
            "question": "Declare a tuple named 'coordinates' with values (10, 20).",
            "solution": "coordinates = (10, 20)",
            "hint": "Use parentheses to define a tuple.",
            "test": "'coordinates' in code and '(' in code and ')' in code"
        },
        {
            "question": "Convert the integer 50 to a string.",
            "solution": "str_num = str(50)",
            "hint": "Use the str() function to convert an integer to a string.",
            "test": "'str(' in code"
        },
        {
            "question": "Declare a dictionary named 'person' with keys 'name' and 'age' and respective values 'Alice' and 30.",
            "solution": "person = {'name': 'Alice', 'age': 30}",
            "hint": "Use curly brackets to define a dictionary.",
            "test": "'person' in code and '{' in code and '}' in code"
        },
        {
            "question": "What will be the output of type(3 + 2j)?",
            "solution": "<class 'complex'>",
            "hint": "Complex numbers have a real and an imaginary part.",
            "test": "'complex' in answer"
        },
        {
            "question": "Declare a set named 'unique_numbers' with values 1, 2, and 3.",
            "solution": "unique_numbers = {1, 2, 3}",
            "hint": "Use curly brackets to define a set.",
            "test": "'unique_numbers' in code and '{' in code and '}' in code"
        },
        {
            "question": "What function is used to check the type of a variable?",
            "solution": "type()",
            "hint": "This function returns the data type of any variable.",
            "test": "'type(' in answer"
        },
        {
            "question": "What is the output of bool(0)?",
            "solution": "False",
            "hint": "Zero is considered a falsey value in Python.",
            "test": "'False' in answer"
        },
        {
            "question": "Declare a variable 'greeting' with the value 'Hello, World!' and print its length.",
            "solution": "greeting = 'Hello, World!'
print(len(greeting))",
            "hint": "Use the len() function to get the length of a string.",
            "test": "'len(' in code"
        },
        {
            "question": "What function can be used to get user input as a string?",
            "solution": "input()",
            "hint": "This function allows the user to enter text from the keyboard.",
            "test": "'input(' in answer"
        }
    ]
}
{
    "name": "Python Operators & Expressions",
    "description": "Practice different operators and expressions in Python through engaging puzzles.",
    "puzzles": [
        {
            "question": "Use the addition operator to sum 10 and 20 and store it in a variable 'result'.",
            "solution": "result = 10 + 20",
            "hint": "Use the + operator.",
            "test": "'result' in code and '+' in code"
        },
        {
            "question": "What is the result of 10 % 3?",
            "solution": "1",
            "hint": "The % operator gives the remainder of a division.",
            "test": "'1' in answer"
        },
        {
            "question": "Use the multiplication operator to multiply 5 by 4 and store it in 'product'.",
            "solution": "product = 5 * 4",
            "hint": "Use the * operator.",
            "test": "'product' in code and '*' in code"
        },
        {
            "question": "Use the floor division operator to divide 15 by 2 and store it in 'floor_div'.",
            "solution": "floor_div = 15 // 2",
            "hint": "Use the // operator for integer division.",
            "test": "'floor_div' in code and '//' in code"
        },
        {
            "question": "What will be the result of 2 ** 3?",
            "solution": "8",
            "hint": "The ** operator is used for exponentiation.",
            "test": "'8' in answer"
        },
        {
            "question": "Use the assignment operator to store 100 in a variable named 'x'.",
            "solution": "x = 100",
            "hint": "Use the = operator to assign a value.",
            "test": "'x' in code and '=' in code"
        },
        {
            "question": "Use the comparison operator to check if 10 is greater than 5 and store the result in 'is_greater'.",
            "solution": "is_greater = 10 > 5",
            "hint": "Use the > operator for greater than comparison.",
            "test": "'is_greater' in code and '>' in code"
        },
        {
            "question": "What will be the output of 10 == 10?",
            "solution": "True",
            "hint": "The == operator checks for equality.",
            "test": "'True' in answer"
        },
        {
            "question": "Use the logical AND operator to check if both 5 > 3 and 10 < 20 are true, and store the result in 'result'.",
            "solution": "result = (5 > 3) and (10 < 20)",
            "hint": "Use the 'and' keyword for logical AND.",
            "test": "'and' in code and 'result' in code"
        },
        {
            "question": "What will be the result of not False?",
            "solution": "True",
            "hint": "The 'not' operator negates a boolean value.",
            "test": "'True' in answer"
        },
        {
            "question": "Use the bitwise OR operator to combine 5 and 3 and store the result in 'bitwise_or'.",
            "solution": "bitwise_or = 5 | 3",
            "hint": "Use the | operator for bitwise OR.",
            "test": "'bitwise_or' in code and '|' in code"
        },
        {
            "question": "What will be the result of 5 & 3?",
            "solution": "1",
            "hint": "The & operator performs a bitwise AND.",
            "test": "'1' in answer"
        },
        {
            "question": "Use the compound assignment operator to add 10 to 'x' and update its value.",
            "solution": "x += 10",
            "hint": "Use the += operator for addition assignment.",
            "test": "'+=' in code and 'x' in code"
        },
        {
            "question": "What will be the result of 'Python' + 'Rocks'?",
            "solution": "'PythonRocks'",
            "hint": "The + operator concatenates strings.",
            "test": "'PythonRocks' in answer"
        },
        {
            "question": "Use the ternary operator to assign 'even' if x is even, otherwise 'odd'.",
            "solution": "result = 'even' if x % 2 == 0 else 'odd'",
            "hint": "Use the ternary operator syntax 'value_if_true if condition else value_if_false'.",
            "test": "'if' in code and 'else' in code and 'result' in code"
        }
    ]
}{
    "name": "Python Conditional Statements (if-elif-else)",
    "description": "Practice conditional statements in Python through engaging puzzles.",
    "puzzles": [
        {
            "question": "Write an if statement that prints 'Positive' if x is greater than 0.",
            "solution": "if x > 0:\n    print('Positive')",
            "hint": "Use the if keyword followed by a condition.",
            "test": "'if' in code and 'x > 0' in code"
        },
        {
            "question": "Write an if-else statement that prints 'Even' if x is even, otherwise prints 'Odd'.",
            "solution": "if x % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
            "hint": "Use if with modulo operator % to check evenness.",
            "test": "'if' in code and 'else' in code and '%' in code"
        },
        {
            "question": "Write an if-elif-else statement to check if x is positive, negative, or zero.",
            "solution": "if x > 0:\n    print('Positive')\nelif x < 0:\n    print('Negative')\nelse:\n    print('Zero')",
            "hint": "Use elif for additional conditions.",
            "test": "'if' in code and 'elif' in code and 'else' in code"
        },
        {
            "question": "Write a condition that prints 'Adult' if age is 18 or older, otherwise 'Minor'.",
            "solution": "if age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
            "hint": "Use >= to compare values.",
            "test": "'if' in code and 'else' in code and '>=' in code"
        },
        {
            "question": "Write an if statement that prints 'High' if score is above 90, otherwise does nothing.",
            "solution": "if score > 90:\n    print('High')",
            "hint": "Use if without an else statement.",
            "test": "'if' in code and 'score > 90' in code"
        },
        {
            "question": "Write an if statement that prints 'Weekend' if day is 'Saturday' or 'Sunday'.",
            "solution": "if day == 'Saturday' or day == 'Sunday':\n    print('Weekend')",
            "hint": "Use the or operator to check multiple conditions.",
            "test": "'if' in code and 'or' in code"
        },
        {
            "question": "Write an if-elif-else statement to categorize temperature: 'Cold' (<15), 'Warm' (15-30), 'Hot' (>30).",
            "solution": "if temp < 15:\n    print('Cold')\nelif temp <= 30:\n    print('Warm')\nelse:\n    print('Hot')",
            "hint": "Use comparison operators for range checks.",
            "test": "'if' in code and 'elif' in code and 'else' in code"
        },
        {
            "question": "Write an if statement that prints 'Discount Applied' if user is a 'member'.",
            "solution": "if user == 'member':\n    print('Discount Applied')",
            "hint": "Use == to compare string values.",
            "test": "'if' in code and '==' in code"
        },
        {
            "question": "Write an if-else statement to check if a number is divisible by 5 and print 'Divisible' or 'Not Divisible'.",
            "solution": "if num % 5 == 0:\n    print('Divisible')\nelse:\n    print('Not Divisible')",
            "hint": "Use modulo operator % to check divisibility.",
            "test": "'if' in code and 'else' in code and '%' in code"
        },
        {
            "question": "Write an if-elif-else statement to classify grades: 'A' (>=90), 'B' (>=80), 'C' (>=70), 'F' (<70).",
            "solution": "if grade >= 90:\n    print('A')\nelif grade >= 80:\n    print('B')\nelif grade >= 70:\n    print('C')\nelse:\n    print('F')",
            "hint": "Use multiple elif conditions for grading.",
            "test": "'if' in code and 'elif' in code and 'else' in code"
        },
        {
            "question": "Write an if statement that prints 'Valid' if age is between 18 and 65 (inclusive).",
            "solution": "if 18 <= age <= 65:\n    print('Valid')",
            "hint": "Use chained comparisons.",
            "test": "'if' in code and '<=' in code"
        },
        {
            "question": "Write an if-elif-else statement to check if a string starts with 'A', 'B', or 'C'.",
            "solution": "if name.startswith('A'):\n    print('Starts with A')\nelif name.startswith('B'):\n    print('Starts with B')\nelif name.startswith('C'):\n    print('Starts with C')",
            "hint": "Use the .startswith() method for strings.",
            "test": "'if' in code and 'startswith' in code"
        },
        {
            "question": "Write an if-else statement that prints 'Leap Year' if year is divisible by 4 but not 100, unless also divisible by 400.",
            "solution": "if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print('Leap Year')\nelse:\n    print('Not a Leap Year')",
            "hint": "Check divisibility rules for leap years.",
            "test": "'if' in code and 'else' in code and '%' in code"
        }
    ]
}

