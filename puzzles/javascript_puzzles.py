{
    "name": "JavaScript Variables & Data Types",
    "description": "Learn about variables and data types in JavaScript.",
    "puzzles": [
        {
            "question": "Declare a variable named 'age' and assign it the value 25.",
            "solution": "let age = 25;",
            "hint": "Use 'let' to declare a variable.",
            "test": "let age" in code
        },
        {
            "question": "Declare a constant variable named 'PI' with a value of 3.14.",
            "solution": "const PI = 3.14;",
            "hint": "Use 'const' to declare a constant.",
            "test": "const PI" in code
        },
        {
            "question": "Declare a variable named 'name' and assign it the string 'John'.",
            "solution": "let name = 'John';",
            "hint": "Use single or double quotes for strings.",
            "test": "let name" in code
        },
        {
            "question": "Declare a boolean variable 'isStudent' and set it to true.",
            "solution": "let isStudent = true;",
            "hint": "Boolean values are either true or false.",
            "test": "let isStudent" in code
        },
        {
            "question": "Declare an undefined variable named 'x'.",
            "solution": "let x;",
            "hint": "Just declare the variable without assigning a value.",
            "test": "let x" in code
        },
        {
            "question": "Declare a null variable named 'y'.",
            "solution": "let y = null;",
            "hint": "Assign 'null' to the variable.",
            "test": "let y" in code
        },
        {
            "question": "Declare a variable named 'numbers' and assign it an array with values 1, 2, and 3.",
            "solution": "let numbers = [1, 2, 3];",
            "hint": "Use square brackets to define an array.",
            "test": "let numbers" in code
        },
        {
            "question": "Declare an object named 'person' with properties 'name' as 'Alice' and 'age' as 30.",
            "solution": "let person = { name: 'Alice', age: 30 };",
            "hint": "Use curly braces to define an object.",
            "test": "let person" in code
        },
        {
            "question": "Declare a variable using 'var' and assign it a value of 100.",
            "solution": "var score = 100;",
            "hint": "Use 'var' instead of 'let'.",
            "test": "var score" in code
        },
        {
            "question": "Declare a variable 'message' and assign it a template literal string 'Hello, World!'.",
            "solution": "let message = `Hello, World!`;",
            "hint": "Use backticks (`) for template literals.",
            "test": "let message" in code
        },
        {
            "question": "Declare a variable 'bigNumber' and assign it a BigInt value of 9007199254740991n.",
            "solution": "let bigNumber = 9007199254740991n;",
            "hint": "Use 'n' at the end of a number for BigInt.",
            "test": "let bigNumber" in code
        },
        {
            "question": "Declare a symbol variable named 'uniqueId'.",
            "solution": "let uniqueId = Symbol('id');",
            "hint": "Use 'Symbol()' to create a unique identifier.",
            "test": "let uniqueId" in code
        },
        {
            "question": "Check the type of variable 'data' using 'typeof'.",
            "solution": "typeof data;",
            "hint": "Use 'typeof' followed by the variable name.",
            "test": "typeof data" in code
        },
        {
            "question": "Convert a string '123' into a number and store it in variable 'num'.",
            "solution": "let num = Number('123');",
            "hint": "Use 'Number()' to convert a string to a number.",
            "test": "let num" in code
        },
        {
            "question": "Convert a number 456 into a string and store it in variable 'str'.",
            "solution": "let str = String(456);",
            "hint": "Use 'String()' to convert a number to a string.",
            "test": "let str" in code
        }
    ]
}
{
    "name": "JavaScript Operators & Expressions",
    "description": "Learn about operators and expressions in JavaScript.",
    "puzzles": [
        {
            "question": "Add 10 and 20 and store the result in a variable 'sum'.",
            "solution": "let sum = 10 + 20;",
            "hint": "Use the + operator for addition.",
            "test": "let sum" in code
        },
        {
            "question": "Subtract 5 from 15 and store the result in 'difference'.",
            "solution": "let difference = 15 - 5;",
            "hint": "Use the - operator for subtraction.",
            "test": "let difference" in code
        },
        {
            "question": "Multiply 4 by 3 and store the result in 'product'.",
            "solution": "let product = 4 * 3;",
            "hint": "Use the * operator for multiplication.",
            "test": "let product" in code
        },
        {
            "question": "Divide 20 by 4 and store the result in 'quotient'.",
            "solution": "let quotient = 20 / 4;",
            "hint": "Use the / operator for division.",
            "test": "let quotient" in code
        },
        {
            "question": "Find the remainder when 17 is divided by 3 and store it in 'remainder'.",
            "solution": "let remainder = 17 % 3;",
            "hint": "Use the % operator to get the remainder.",
            "test": "let remainder" in code
        },
        {
            "question": "Increment the variable 'count' by 1.",
            "solution": "count++;",
            "hint": "Use ++ to increment by 1.",
            "test": "count++" in code
        },
        {
            "question": "Decrement the variable 'score' by 1.",
            "solution": "score--;",
            "hint": "Use -- to decrement by 1.",
            "test": "score--" in code
        },
        {
            "question": "Check if 'x' is greater than 'y' and store the result in 'isGreater'.",
            "solution": "let isGreater = x > y;",
            "hint": "Use the > operator for comparison.",
            "test": "let isGreater" in code
        },
        {
            "question": "Check if 'a' is equal to 'b' using strict equality and store the result in 'isEqual'.",
            "solution": "let isEqual = a === b;",
            "hint": "Use === for strict equality comparison.",
            "test": "let isEqual" in code
        },
        {
            "question": "Use the logical AND operator to check if both 'p' and 'q' are true.",
            "solution": "let result = p && q;",
            "hint": "Use && for logical AND.",
            "test": "let result" in code
        },
        {
            "question": "Use the logical OR operator to check if either 'm' or 'n' is true.",
            "solution": "let result = m || n;",
            "hint": "Use || for logical OR.",
            "test": "let result" in code
        },
        {
            "question": "Use the logical NOT operator to invert the value of 'flag'.",
            "solution": "let inverted = !flag;",
            "hint": "Use ! to negate a boolean value.",
            "test": "let inverted" in code
        },
        {
            "question": "Use the ternary operator to assign 'adult' if age is 18 or more, otherwise 'minor'.",
            "solution": "let category = age >= 18 ? 'adult' : 'minor';",
            "hint": "Use ? : for the ternary operator.",
            "test": "let category" in code
        },
        {
            "question": "Use the exponentiation operator to calculate 2 to the power of 3 and store it in 'power'.",
            "solution": "let power = 2 ** 3;",
            "hint": "Use ** for exponentiation.",
            "test": "let power" in code
        },
        {
            "question": "Perform a compound assignment by adding 10 to 'total'.",
            "solution": "total += 10;",
            "hint": "Use += for addition assignment.",
            "test": "total += 10" in code
        }
    ]
}
{
    "name": "JavaScript Conditional Statements",
    "description": "Learn about conditional statements (if-else, switch) in JavaScript.",
    "puzzles": [
        {
            "question": "Check if a number is positive and store the result in 'isPositive'.",
            "solution": "let isPositive = number > 0;",
            "hint": "Use the > operator for comparison.",
            "test": "let isPositive" in code
        },
        {
            "question": "Use an if-else statement to check if 'age' is 18 or more and log 'Adult', otherwise log 'Minor'.",
            "solution": "if (age >= 18) { console.log('Adult'); } else { console.log('Minor'); }",
            "hint": "Use if-else to check the condition.",
            "test": "if (age" in code
        },
        {
            "question": "Check if 'score' is greater than or equal to 50, and store 'Pass' or 'Fail' in 'result'.",
            "solution": "let result = score >= 50 ? 'Pass' : 'Fail';",
            "hint": "Use the ternary operator for condition checking.",
            "test": "let result" in code
        },
        {
            "question": "Use an if-else-if ladder to check if 'temperature' is hot (>30), warm (15-30), or cold (<15).",
            "solution": "if (temperature > 30) { console.log('Hot'); } else if (temperature >= 15) { console.log('Warm'); } else { console.log('Cold'); }",
            "hint": "Use multiple if-else statements to check the range.",
            "test": "if (temperature" in code
        },
        {
            "question": "Use a switch statement to check the value of 'day' and log 'Weekend' for Saturday/Sunday, else 'Weekday'.",
            "solution": "switch(day) { case 'Saturday': case 'Sunday': console.log('Weekend'); break; default: console.log('Weekday'); }",
            "hint": "Use switch to handle multiple cases.",
            "test": "switch(day" in code
        },
        {
            "question": "Check if 'num' is even or odd and store 'Even' or 'Odd' in 'parity'.",
            "solution": "let parity = num % 2 === 0 ? 'Even' : 'Odd';",
            "hint": "Use the modulus operator % to check divisibility.",
            "test": "let parity" in code
        },
        {
            "question": "Write an if statement that logs 'Hello, Admin' if the user role is 'admin'.",
            "solution": "if (role === 'admin') { console.log('Hello, Admin'); }",
            "hint": "Use strict equality to check the role.",
            "test": "if (role" in code
        },
        {
            "question": "Write a switch statement that logs different messages for 'red', 'blue', and 'green' colors.",
            "solution": "switch(color) { case 'red': console.log('Red selected'); break; case 'blue': console.log('Blue selected'); break; case 'green': console.log('Green selected'); break; default: console.log('Unknown color'); }",
            "hint": "Use switch-case for handling multiple conditions.",
            "test": "switch(color" in code
        },
        {
            "question": "Use an if-else statement to check if a number is negative, zero, or positive and log the result.",
            "solution": "if (num < 0) { console.log('Negative'); } else if (num === 0) { console.log('Zero'); } else { console.log('Positive'); }",
            "hint": "Use if-else to check multiple conditions.",
            "test": "if (num" in code
        },
        {
            "question": "Use a nested if statement to check if 'score' is greater than 90, and if so, check if 'bonus' is true to log 'Excellent with Bonus'.",
            "solution": "if (score > 90) { if (bonus) { console.log('Excellent with Bonus'); } else { console.log('Excellent'); } }",
            "hint": "Use nested if statements for additional conditions.",
            "test": "if (score" in code
        },
        {
            "question": "Write an if-else statement to check if 'password' length is at least 8 characters and log 'Strong' or 'Weak'.",
            "solution": "if (password.length >= 8) { console.log('Strong'); } else { console.log('Weak'); }",
            "hint": "Use .length to check the password length.",
            "test": "if (password.length" in code
        },
        {
            "question": "Use an if-else statement to check if 'time' is before 12 PM (morning) or after (afternoon).",
            "solution": "if (time < 12) { console.log('Morning'); } else { console.log('Afternoon'); }",
            "hint": "Compare time with 12 using < operator.",
            "test": "if (time" in code
        },
        {
            "question": "Write a switch statement that checks 'grade' and logs 'Excellent' for 'A', 'Good' for 'B', 'Average' for 'C', and 'Fail' for others.",
            "solution": "switch(grade) { case 'A': console.log('Excellent'); break; case 'B': console.log('Good'); break; case 'C': console.log('Average'); break; default: console.log('Fail'); }",
            "hint": "Use switch-case to handle grade categories.",
            "test": "switch(grade" in code
        },
        {
            "question": "Use an if-else statement to check if 'userLoggedIn' is true and log 'Welcome', otherwise 'Please log in'.",
            "solution": "if (userLoggedIn) { console.log('Welcome'); } else { console.log('Please log in'); }",
            "hint": "Use an if condition to check the boolean value.",
            "test": "if (userLoggedIn" in code
        },
        {
            "question": "Use a ternary operator to assign 'Allowed' if 'age' is 21 or above, otherwise 'Not Allowed'.",
            "solution": "let status = age >= 21 ? 'Allowed' : 'Not Allowed';",
            "hint": "Use the ternary operator for simple conditions.",
            "test": "let status" in code
        }
    ]
}
{
    "name": "JavaScript Loops & Iteration",
    "description": "Learn about loops including for, while, and do-while in JavaScript.",
    "puzzles": [
        {
            "question": "Write a for loop that logs numbers from 1 to 5.",
            "solution": "for(let i = 1; i <= 5; i++) { console.log(i); }",
            "hint": "Use a for loop with an incrementing variable.",
            "test": "'for(let i = 1;' in code"
        },
        {
            "question": "Write a while loop that logs numbers from 1 to 5.",
            "solution": "let i = 1; while(i <= 5) { console.log(i); i++; }",
            "hint": "Use a while loop with a condition.",
            "test": "'while(i <=' in code"
        },
        {
            "question": "Write a do-while loop that logs numbers from 1 to 5.",
            "solution": "let i = 1; do { console.log(i); i++; } while(i <= 5);",
            "hint": "Use a do-while loop that runs at least once.",
            "test": "'do {' in code"
        },
        {
            "question": "Create a for loop that logs even numbers from 2 to 10.",
            "solution": "for(let i = 2; i <= 10; i += 2) { console.log(i); }",
            "hint": "Increase i by 2 in each iteration.",
            "test": "'for(let i = 2;' in code"
        },
        {
            "question": "Write a while loop that decrements from 5 to 1.",
            "solution": "let i = 5; while(i >= 1) { console.log(i); i--; }",
            "hint": "Decrease the loop variable inside while loop.",
            "test": "'while(i >=' in code"
        },
        {
            "question": "Use a for loop to iterate over an array of colors and log each one.",
            "solution": "let colors = ['red', 'blue', 'green']; for(let i = 0; i < colors.length; i++) { console.log(colors[i]); }",
            "hint": "Use array.length as the condition.",
            "test": "'for(let i = 0;' in code"
        },
        {
            "question": "Use a while loop to sum numbers from 1 to 10.",
            "solution": "let i = 1, sum = 0; while(i <= 10) { sum += i; i++; } console.log(sum);",
            "hint": "Accumulate sum inside the while loop.",
            "test": "'while(i <=' in code"
        },
        {
            "question": "Write a for loop using break to stop when i equals 3.",
            "solution": "for(let i = 1; i <= 5; i++) { if(i === 3) break; console.log(i); }",
            "hint": "Use the break statement inside the loop.",
            "test": "'if(i === 3) break;' in code"
        },
        {
            "question": "Write a for loop using continue to skip 3.",
            "solution": "for(let i = 1; i <= 5; i++) { if(i === 3) continue; console.log(i); }",
            "hint": "Use continue to skip one iteration.",
            "test": "'if(i === 3) continue;' in code"
        },
        {
            "question": "Use a for...of loop to iterate over an array of fruits.",
            "solution": "let fruits = ['apple', 'banana', 'cherry']; for(let fruit of fruits) { console.log(fruit); }",
            "hint": "Use for...of syntax to iterate.",
            "test": "'for(let fruit of' in code"
        },
        {
            "question": "Use a for...in loop to log keys of an object.",
            "solution": "let obj = {a:1, b:2, c:3}; for(let key in obj) { console.log(key); }",
            "hint": "Use for...in syntax for objects.",
            "test": "'for(let key in' in code"
        },
        {
            "question": "Write a while loop that keeps doubling a number until it reaches 100.",
            "solution": "let num = 1; while(num < 100) { num *= 2; console.log(num); }",
            "hint": "Multiply the number inside the loop.",
            "test": "'while(num <' in code"
        },
        {
            "question": "Write a nested for loop to generate a 3x3 grid of numbers.",
            "solution": "for(let i = 1; i <= 3; i++) { for(let j = 1; j <= 3; j++) { console.log(i, j); } }",
            "hint": "Use two for loops, one inside another.",
            "test": "'for(let i = 1;' in code and 'for(let j = 1;' in code"
        },
        {
            "question": "Write a loop that iterates over an array and stops when it finds 'stop'.",
            "solution": "let arr = ['go', 'run', 'stop', 'walk']; for(let item of arr) { if(item === 'stop') break; console.log(item); }",
            "hint": "Use break inside the loop when item is 'stop'.",
            "test": "'if(item === \"stop\") break;' in code"
        },
        {
            "question": "Write a do-while loop that runs at least once, even if the condition is false.",
            "solution": "let num = 10; do { console.log(num); num++; } while(num < 5);",
            "hint": "The loop should execute at least once before checking condition.",
            "test": "'do {' in code"
        }
    ]
}
{
    "name": "JavaScript Functions",
    "description": "Learn about function declaration, expressions, and arrow functions in JavaScript.",
    "puzzles": [
        {
            "question": "Declare a function named 'greet' that logs 'Hello, world!'.",
            "solution": "function greet() { console.log('Hello, world!'); }",
            "hint": "Use the function keyword followed by the function name.",
            "test": "'function greet() {' in code"
        },
        {
            "question": "Create a function expression named 'add' that returns the sum of two numbers.",
            "solution": "const add = function(a, b) { return a + b; };",
            "hint": "Assign a function to a variable using the function keyword.",
            "test": "'const add = function(' in code"
        },
        {
            "question": "Use an arrow function to multiply two numbers and store it in 'multiply'.",
            "solution": "const multiply = (a, b) => a * b;",
            "hint": "Use the => syntax for arrow functions.",
            "test": "'const multiply = (' in code"
        },
        {
            "question": "Write a function 'square' that returns the square of a number.",
            "solution": "function square(n) { return n * n; }",
            "hint": "Multiply the input by itself and return the result.",
            "test": "'function square(n)' in code"
        },
        {
            "question": "Convert 'square' function to an arrow function.",
            "solution": "const square = n => n * n;",
            "hint": "Arrow functions can omit parentheses for a single parameter.",
            "test": "'const square = n =>' in code"
        },
        {
            "question": "Create an IIFE that logs 'Immediately Invoked!'.",
            "solution": "(function() { console.log('Immediately Invoked!'); })();",
            "hint": "Wrap the function in parentheses and call it immediately.",
            "test": "'(function() {' in code"
        },
        {
            "question": "Write a function 'factorial' that calculates the factorial of a number.",
            "solution": "function factorial(n) { return n === 0 ? 1 : n * factorial(n - 1); }",
            "hint": "Use recursion to multiply numbers down to 1.",
            "test": "'function factorial(n)' in code"
        },
        {
            "question": "Create an arrow function 'double' that doubles a given number.",
            "solution": "const double = n => n * 2;",
            "hint": "Use the arrow function syntax with a single parameter.",
            "test": "'const double = n =>' in code"
        },
        {
            "question": "Write a function 'greetUser' that takes a name and logs 'Hello, [name]'.",
            "solution": "function greetUser(name) { console.log('Hello, ' + name); }",
            "hint": "Pass a parameter and concatenate it in the console.log.",
            "test": "'function greetUser(name)' in code"
        },
        {
            "question": "Use the rest operator in a function named 'sumAll' to add all its arguments.",
            "solution": "function sumAll(...nums) { return nums.reduce((a, b) => a + b, 0); }",
            "hint": "Use ... before the parameter to collect all arguments into an array.",
            "test": "'function sumAll(...nums)' in code"
        },
        {
            "question": "Create an arrow function 'isEven' that returns true if a number is even.",
            "solution": "const isEven = n => n % 2 === 0;",
            "hint": "Check if the remainder when dividing by 2 is zero.",
            "test": "'const isEven = n =>' in code"
        },
        {
            "question": "Write a function 'makeCounter' that returns a function which increments a counter.",
            "solution": "function makeCounter() { let count = 0; return function() { return ++count; }; }",
            "hint": "Use closure to maintain state across function calls.",
            "test": "'function makeCounter()' in code"
        },
        {
            "question": "Create a function 'sayHi' that logs 'Hi' every second using setInterval().",
            "solution": "function sayHi() { setInterval(() => console.log('Hi'), 1000); }",
            "hint": "Use setInterval to repeatedly execute a function.",
            "test": "'setInterval(() =>' in code"
        },
        {
            "question": "Write a function 'delayedLog' that logs 'Hello' after 2 seconds using setTimeout().",
            "solution": "function delayedLog() { setTimeout(() => console.log('Hello'), 2000); }",
            "hint": "Use setTimeout to execute a function after a delay.",
            "test": "'setTimeout(() =>' in code"
        },
        {
            "question": "Write a function 'bindExample' that uses bind() to set 'this' context.",
            "solution": "const obj = { value: 10 }; function getValue() { return this.value; } const boundFunc = getValue.bind(obj);",
            "hint": "Use bind() to attach a specific object to a function.",
            "test": "'bind(obj)' in code"
        }
    ]
}
{
    "name": "JavaScript Arrays & Array Methods",
    "description": "Learn about arrays and their methods in JavaScript.",
    "puzzles": [
        {
            "question": "Create an array named 'fruits' with 'apple', 'banana', and 'cherry'.",
            "solution": "let fruits = ['apple', 'banana', 'cherry'];",
            "hint": "Use square brackets to define an array.",
            "test": "'let fruits = [' in code"
        },
        {
            "question": "Add 'grape' to the end of the 'fruits' array.",
            "solution": "fruits.push('grape');",
            "hint": "Use the push() method to add an item.",
            "test": "'fruits.push(' in code"
        },
        {
            "question": "Remove the last element from the 'fruits' array.",
            "solution": "fruits.pop();",
            "hint": "Use the pop() method to remove the last item.",
            "test": "'fruits.pop();' in code"
        },
        {
            "question": "Remove the first element from the 'fruits' array.",
            "solution": "fruits.shift();",
            "hint": "Use the shift() method to remove the first item.",
            "test": "'fruits.shift();' in code"
        },
        {
            "question": "Add 'mango' to the beginning of the 'fruits' array.",
            "solution": "fruits.unshift('mango');",
            "hint": "Use the unshift() method to add an item at the beginning.",
            "test": "'fruits.unshift(' in code"
        },
        {
            "question": "Find the index of 'banana' in the 'fruits' array.",
            "solution": "let index = fruits.indexOf('banana');",
            "hint": "Use the indexOf() method to get the index.",
            "test": "'fruits.indexOf(' in code"
        },
        {
            "question": "Check if 'apple' exists in the 'fruits' array.",
            "solution": "let exists = fruits.includes('apple');",
            "hint": "Use the includes() method to check for existence.",
            "test": "'fruits.includes(' in code"
        },
        {
            "question": "Convert the 'fruits' array into a comma-separated string.",
            "solution": "let fruitString = fruits.join(', ');",
            "hint": "Use the join() method to create a string.",
            "test": "'fruits.join(' in code"
        },
        {
            "question": "Create a new array containing only the first two elements of 'fruits'.",
            "solution": "let newFruits = fruits.slice(0, 2);",
            "hint": "Use the slice() method to extract elements.",
            "test": "'fruits.slice(' in code"
        },
        {
            "question": "Remove the second element from the 'fruits' array.",
            "solution": "fruits.splice(1, 1);",
            "hint": "Use the splice() method to remove an element.",
            "test": "'fruits.splice(' in code"
        },
        {
            "question": "Reverse the order of elements in the 'fruits' array.",
            "solution": "fruits.reverse();",
            "hint": "Use the reverse() method.",
            "test": "'fruits.reverse();' in code"
        },
        {
            "question": "Sort the 'fruits' array in alphabetical order.",
            "solution": "fruits.sort();",
            "hint": "Use the sort() method to sort alphabetically.",
            "test": "'fruits.sort();' in code"
        },
        {
            "question": "Filter 'fruits' to get only those containing the letter 'a'.",
            "solution": "let filtered = fruits.filter(fruit => fruit.includes('a'));",
            "hint": "Use the filter() method with a condition.",
            "test": "'fruits.filter(' in code"
        },
        {
            "question": "Create a new array with fruit names in uppercase.",
            "solution": "let upperFruits = fruits.map(fruit => fruit.toUpperCase());",
            "hint": "Use the map() method to transform array elements.",
            "test": "'fruits.map(' in code"
        },
        {
            "question": "Find the first fruit that starts with 'b' in the 'fruits' array.",
            "solution": "let firstB = fruits.find(fruit => fruit.startsWith('b'));",
            "hint": "Use the find() method to get the first match.",
            "test": "'fruits.find(' in code"
        }
    ]
}
{
    "name": "JavaScript Objects & Object Methods",
    "description": "Learn about objects and their methods in JavaScript.",
    "puzzles": [
        {
            "question": "Create an object named 'person' with properties 'name' set to 'John' and 'age' set to 30.",
            "solution": "let person = { name: 'John', age: 30 };",
            "hint": "Use curly braces to define an object.",
            "test": "'let person = {' in code"
        },
        {
            "question": "Access the 'name' property of the 'person' object and store it in a variable 'personName'.",
            "solution": "let personName = person.name;",
            "hint": "Use dot notation to access object properties.",
            "test": "'person.name' in code"
        },
        {
            "question": "Add a new property 'gender' with value 'male' to the 'person' object.",
            "solution": "person.gender = 'male';",
            "hint": "Use dot notation to add a property.",
            "test": "'person.gender' in code"
        },
        {
            "question": "Remove the 'age' property from the 'person' object.",
            "solution": "delete person.age;",
            "hint": "Use the delete keyword to remove a property.",
            "test": "'delete person.age' in code"
        },
        {
            "question": "Check if the 'person' object has a property 'name'.",
            "solution": "let hasName = 'name' in person;",
            "hint": "Use the 'in' operator to check for properties.",
            "test": "'in person' in code"
        },
        {
            "question": "Get an array of all property names of the 'person' object.",
            "solution": "let keys = Object.keys(person);",
            "hint": "Use Object.keys() to get an array of keys.",
            "test": "'Object.keys(' in code"
        },
        {
            "question": "Get an array of all values of the 'person' object.",
            "solution": "let values = Object.values(person);",
            "hint": "Use Object.values() to get an array of values.",
            "test": "'Object.values(' in code"
        },
        {
            "question": "Get an array of key-value pairs from the 'person' object.",
            "solution": "let entries = Object.entries(person);",
            "hint": "Use Object.entries() to get an array of key-value pairs.",
            "test": "'Object.entries(' in code"
        },
        {
            "question": "Merge the 'person' object with another object { city: 'New York' }.",
            "solution": "let updatedPerson = { ...person, city: 'New York' };",
            "hint": "Use the spread operator (...) to merge objects.",
            "test": "'...person' in code"
        },
        {
            "question": "Create a method 'greet' inside 'person' that returns 'Hello, I am John!'.",
            "solution": "person.greet = function() { return 'Hello, I am ' + this.name + '!'; };",
            "hint": "Use 'this' to reference object properties inside a method.",
            "test": "'person.greet' in code"
        },
        {
            "question": "Call the 'greet' method of the 'person' object and store the result in 'greeting'.",
            "solution": "let greeting = person.greet();",
            "hint": "Call the method using dot notation.",
            "test": "'person.greet()' in code"
        },
        {
            "question": "Create a new object 'car' with properties 'brand' set to 'Toyota' and 'model' set to 'Camry'.",
            "solution": "let car = { brand: 'Toyota', model: 'Camry' };",
            "hint": "Use curly braces to define the object.",
            "test": "'let car = {' in code"
        },
        {
            "question": "Use Object.assign() to copy the 'person' object into a new object 'newPerson'.",
            "solution": "let newPerson = Object.assign({}, person);",
            "hint": "Use Object.assign() to clone objects.",
            "test": "'Object.assign(' in code"
        },
        {
            "question": "Convert the 'person' object into a JSON string and store it in 'personJSON'.",
            "solution": "let personJSON = JSON.stringify(person);",
            "hint": "Use JSON.stringify() to convert an object to a string.",
            "test": "'JSON.stringify(' in code"
        },
        {
            "question": "Parse the 'personJSON' string back into an object and store it in 'parsedPerson'.",
            "solution": "let parsedPerson = JSON.parse(personJSON);",
            "hint": "Use JSON.parse() to convert a string back into an object.",
            "test": "'JSON.parse(' in code"
        }
    ]
}
{
    "name": "JavaScript String Methods & Manipulation",
    "description": "Learn about string methods and manipulation in JavaScript.",
    "puzzles": [
        {
            "question": "Create a string variable named 'message' with the value 'Hello, World!'.",
            "solution": "let message = 'Hello, World!';",
            "hint": "Use single or double quotes to define a string.",
            "test": "'let message =' in code"
        },
        {
            "question": "Find the length of the 'message' string and store it in a variable 'length'.",
            "solution": "let length = message.length;",
            "hint": "Use the .length property.",
            "test": "'message.length' in code"
        },
        {
            "question": "Convert 'message' to uppercase and store it in 'upperMessage'.",
            "solution": "let upperMessage = message.toUpperCase();",
            "hint": "Use the .toUpperCase() method.",
            "test": "'message.toUpperCase()' in code"
        },
        {
            "question": "Convert 'message' to lowercase and store it in 'lowerMessage'.",
            "solution": "let lowerMessage = message.toLowerCase();",
            "hint": "Use the .toLowerCase() method.",
            "test": "'message.toLowerCase()' in code"
        },
        {
            "question": "Extract the word 'Hello' from 'message' and store it in 'greeting'.",
            "solution": "let greeting = message.substring(0, 5);",
            "hint": "Use the .substring() method with appropriate indexes.",
            "test": "'message.substring(' in code"
        },
        {
            "question": "Replace 'World' with 'JavaScript' in 'message' and store it in 'newMessage'.",
            "solution": "let newMessage = message.replace('World', 'JavaScript');",
            "hint": "Use the .replace() method.",
            "test": "'message.replace(' in code"
        },
        {
            "question": "Split 'message' into an array of words and store it in 'words'.",
            "solution": "let words = message.split(' ');",
            "hint": "Use the .split() method with a space as a separator.",
            "test": "'message.split(' in code"
        },
        {
            "question": "Check if 'message' contains the word 'Hello' and store the result in 'hasHello'.",
            "solution": "let hasHello = message.includes('Hello');",
            "hint": "Use the .includes() method.",
            "test": "'message.includes(' in code"
        },
        {
            "question": "Trim the whitespace from ' message ' and store it in 'trimmedMessage'.",
            "solution": "let trimmedMessage = ' message '.trim();",
            "hint": "Use the .trim() method.",
            "test": "'.trim(' in code"
        },
        {
            "question": "Concatenate 'Hello' and 'World' into 'fullMessage' with a space in between.",
            "solution": "let fullMessage = 'Hello' + ' ' + 'World';",
            "hint": "Use the + operator to concatenate strings.",
            "test": "'Hello' + ' ' + 'World' in code"
        },
        {
            "question": "Extract the first character of 'message' and store it in 'firstChar'.",
            "solution": "let firstChar = message.charAt(0);",
            "hint": "Use the .charAt() method.",
            "test": "'message.charAt(' in code"
        },
        {
            "question": "Find the index of 'World' in 'message' and store it in 'index'.",
            "solution": "let index = message.indexOf('World');",
            "hint": "Use the .indexOf() method.",
            "test": "'message.indexOf(' in code"
        },
        {
            "question": "Check if 'message' starts with 'Hello' and store the result in 'startsWithHello'.",
            "solution": "let startsWithHello = message.startsWith('Hello');",
            "hint": "Use the .startsWith() method.",
            "test": "'message.startsWith(' in code"
        },
        {
            "question": "Check if 'message' ends with 'World!' and store the result in 'endsWithWorld'.",
            "solution": "let endsWithWorld = message.endsWith('World!');",
            "hint": "Use the .endsWith() method.",
            "test": "'message.endsWith(' in code"
        },
        {
            "question": "Repeat 'Hello' three times and store it in 'repeatedMessage'.",
            "solution": "let repeatedMessage = 'Hello'.repeat(3);",
            "hint": "Use the .repeat() method.",
            "test": "'Hello'.repeat(' in code"
        }
    ]
}
{
    "name": "JavaScript DOM Manipulation & Events",
    "description": "Learn about manipulating the DOM and handling events in JavaScript.",
    "puzzles": [
        {
            "question": "Select an element with id 'content' and store it in a variable 'element'.",
            "solution": "let element = document.getElementById('content');",
            "hint": "Use document.getElementById().",
            "test": "'document.getElementById(' in code"
        },
        {
            "question": "Change the inner text of the element with id 'content' to 'Hello, DOM!'.",
            "solution": "document.getElementById('content').innerText = 'Hello, DOM!';",
            "hint": "Use the innerText property.",
            "test": "'.innerText =' in code"
        },
        {
            "question": "Select all paragraph elements and store them in a variable 'paragraphs'.",
            "solution": "let paragraphs = document.getElementsByTagName('p');",
            "hint": "Use document.getElementsByTagName().",
            "test": "'document.getElementsByTagName(' in code"
        },
        {
            "question": "Select all elements with class 'highlight' and store them in 'highlights'.",
            "solution": "let highlights = document.getElementsByClassName('highlight');",
            "hint": "Use document.getElementsByClassName().",
            "test": "'document.getElementsByClassName(' in code"
        },
        {
            "question": "Select the first element with class 'box' using querySelector and store it in 'box'.",
            "solution": "let box = document.querySelector('.box');",
            "hint": "Use document.querySelector().",
            "test": "'document.querySelector(' in code"
        },
        {
            "question": "Select all elements with class 'box' using querySelectorAll and store them in 'boxes'.",
            "solution": "let boxes = document.querySelectorAll('.box');",
            "hint": "Use document.querySelectorAll().",
            "test": "'document.querySelectorAll(' in code"
        },
        {
            "question": "Create a new paragraph element and store it in 'newPara'.",
            "solution": "let newPara = document.createElement('p');",
            "hint": "Use document.createElement().",
            "test": "'document.createElement(' in code"
        },
        {
            "question": "Append 'newPara' to the body element.",
            "solution": "document.body.appendChild(newPara);",
            "hint": "Use appendChild() on document.body.",
            "test": "'document.body.appendChild(' in code"
        },
        {
            "question": "Remove the element with id 'content' from the DOM.",
            "solution": "document.getElementById('content').remove();",
            "hint": "Use the remove() method.",
            "test": "'.remove(' in code"
        },
        {
            "question": "Change the background color of the element with id 'box' to blue.",
            "solution": "document.getElementById('box').style.backgroundColor = 'blue';",
            "hint": "Use the style property.",
            "test": "'.style.backgroundColor =' in code"
        },
        {
            "question": "Add a class 'active' to the element with id 'menu'.",
            "solution": "document.getElementById('menu').classList.add('active');",
            "hint": "Use the classList.add() method.",
            "test": "'.classList.add(' in code"
        },
        {
            "question": "Attach a click event listener to the button with id 'btn' that logs 'Button clicked!'.",
            "solution": "document.getElementById('btn').addEventListener('click', () => console.log('Button clicked!'));",
            "hint": "Use addEventListener().",
            "test": "'addEventListener(' in code"
        },
        {
            "question": "Change the text of the button with id 'btn' when clicked.",
            "solution": "document.getElementById('btn').addEventListener('click', function() { this.innerText = 'Clicked!'; });",
            "hint": "Use addEventListener() and this.innerText.",
            "test": "'addEventListener(' in code"
        },
        {
            "question": "Toggle the class 'visible' on the element with id 'menu' when clicked.",
            "solution": "document.getElementById('menu').addEventListener('click', function() { this.classList.toggle('visible'); });",
            "hint": "Use classList.toggle().",
            "test": "'classList.toggle(' in code"
        },
        {
            "question": "Prevent the default action when clicking a link with id 'link'.",
            "solution": "document.getElementById('link').addEventListener('click', function(event) { event.preventDefault(); });",
            "hint": "Use event.preventDefault().",
            "test": "'event.preventDefault(' in code"
        }
    ]
}
{
    "name": "JavaScript ES6 Features",
    "description": "Learn about let, const, template literals, and destructuring in JavaScript.",
    "puzzles": [
        {
            "question": "Declare a variable 'x' using let and assign it the value 10.",
            "solution": "let x = 10;",
            "hint": "Use the let keyword.",
            "test": "'let ' in code and '=' in code"
        },
        {
            "question": "Declare a constant 'PI' with the value 3.14.",
            "solution": "const PI = 3.14;",
            "hint": "Use the const keyword.",
            "test": "'const ' in code and '=' in code"
        },
        {
            "question": "Use template literals to create a string 'Hello, John!' using a variable 'name' with value 'John'.",
            "solution": "let name = 'John';\nlet greeting = `Hello, ${name}!`;",
            "hint": "Use backticks and ${} syntax.",
            "test": "'`Hello, ${' in code"
        },
        {
            "question": "Destructure an array [1,2,3] into variables a, b, and c.",
            "solution": "let [a, b, c] = [1, 2, 3];",
            "hint": "Use array destructuring syntax.",
            "test": "'let [a, b, c] =' in code"
        },
        {
            "question": "Destructure an object {name: 'Alice', age: 25} into variables 'name' and 'age'.",
            "solution": "let {name, age} = {name: 'Alice', age: 25};",
            "hint": "Use object destructuring syntax.",
            "test": "'let {name, age} =' in code"
        },
        {
            "question": "Use default parameter value in a function 'greet' that takes a name and defaults to 'Guest'.",
            "solution": "function greet(name = 'Guest') { return `Hello, ${name}!`; }",
            "hint": "Use '=' in function parameters.",
            "test": "'function greet(name = ' in code"
        },
        {
            "question": "Use the spread operator to merge two arrays [1,2] and [3,4].",
            "solution": "let merged = [...[1,2], ...[3,4]];",
            "hint": "Use ... before arrays.",
            "test": "'...' in code"
        },
        {
            "question": "Use the rest operator to collect remaining arguments in a function 'sum'.",
            "solution": "function sum(...numbers) { return numbers.reduce((a, b) => a + b, 0); }",
            "hint": "Use ... before parameter name.",
            "test": "'function sum(...' in code"
        },
        {
            "question": "Use arrow function syntax to create a function 'add' that adds two numbers.",
            "solution": "const add = (a, b) => a + b;",
            "hint": "Use => instead of function keyword.",
            "test": "'=>' in code"
        },
        {
            "question": "Use destructuring to swap values of variables x and y (x=5, y=10).",
            "solution": "[x, y] = [y, x];",
            "hint": "Use array destructuring.",
            "test": "'[x, y] =' in code"
        },
        {
            "question": "Use template literals to create a multi-line string stored in 'text'.",
            "solution": "let text = `This is\na multi-line\nstring.`;",
            "hint": "Use backticks for multi-line strings.",
            "test": "'`' in code"
        },
        {
            "question": "Use object property shorthand to create an object {name, age} from variables.",
            "solution": "let name = 'Bob', age = 30;\nlet person = {name, age};",
            "hint": "Omit key-value pairs if variable names match keys.",
            "test": "'{name, age}' in code"
        },
        {
            "question": "Use computed property names to create an object with a dynamic key 'prop'.",
            "solution": "let prop = 'dynamicKey';\nlet obj = {[prop]: 'value'};",
            "hint": "Use [] around the computed key.",
            "test": "'[' in code and ']' in code"
        },
        {
            "question": "Use object destructuring with default values for missing properties in {name: 'Eve'}.",
            "solution": "let {name, age = 25} = {name: 'Eve'};",
            "hint": "Assign default values in destructuring syntax.",
            "test": "'let {name, age =' in code"
        },
        {
            "question": "Use a tagged template literal function 'tag' that wraps text in [].",
            "solution": "function tag(strings) { return `[${strings[0]}]`; }\nlet result = tag`Hello`;",
            "hint": "Create a function to process template literals.",
            "test": "'function tag(strings)' in code"
        }
    ]
}
{
    "name": "JavaScript Advanced Functions",
    "description": "Learn about Closures, Callbacks, and Higher-Order Functions in JavaScript.",
    "puzzles": [
        {
            "question": "Create a function 'outer' that defines a variable and returns an inner function accessing that variable.",
            "solution": "function outer() {\n  let count = 0;\n  return function inner() { return ++count; };\n}",
            "hint": "Define a function inside another function and return it.",
            "test": "'function outer' in code and 'return function' in code"
        },
        {
            "question": "Create a function 'delayedHello' that logs 'Hello' after 2 seconds using setTimeout.",
            "solution": "function delayedHello() { setTimeout(() => console.log('Hello'), 2000); }",
            "hint": "Use setTimeout with an arrow function.",
            "test": "'setTimeout' in code"
        },
        {
            "question": "Create a function 'repeat' that takes a function and calls it twice.",
            "solution": "function repeat(fn) { fn(); fn(); }",
            "hint": "Accept a function as an argument and call it twice.",
            "test": "'function repeat' in code and 'fn()' in code"
        },
        {
            "question": "Create a higher-order function 'applyTwice' that takes a function and a value, and applies the function twice.",
            "solution": "function applyTwice(fn, x) { return fn(fn(x)); }",
            "hint": "Call the function twice with the given value.",
            "test": "'function applyTwice' in code"
        },
        {
            "question": "Create a function 'createMultiplier' that takes a number and returns a function that multiplies by that number.",
            "solution": "function createMultiplier(x) { return function(y) { return x * y; }; }",
            "hint": "Return a function that uses the outer function's parameter.",
            "test": "'function createMultiplier' in code and 'return function' in code"
        },
        {
            "question": "Create a function 'once' that ensures another function can only be called once.",
            "solution": "function once(fn) { let called = false; return function() { if (!called) { called = true; return fn(); } }; }",
            "hint": "Use a boolean flag to track function calls.",
            "test": "'function once' in code"
        },
        {
            "question": "Create a function 'compose' that takes two functions and returns their composition.",
            "solution": "function compose(f, g) { return function(x) { return f(g(x)); }; }",
            "hint": "Return a function that applies g first, then f.",
            "test": "'function compose' in code"
        },
        {
            "question": "Create a function 'debounce' that delays execution of a function until after 500ms of inactivity.",
            "solution": "function debounce(fn, delay = 500) { let timer; return function() { clearTimeout(timer); timer = setTimeout(fn, delay); }; }",
            "hint": "Use setTimeout and clearTimeout.",
            "test": "'setTimeout' in code and 'clearTimeout' in code"
        },
        {
            "question": "Create a function 'throttle' that ensures a function is only called at most once every 2 seconds.",
            "solution": "function throttle(fn, limit = 2000) { let lastCall = 0; return function() { let now = Date.now(); if (now - lastCall >= limit) { lastCall = now; fn(); } }; }",
            "hint": "Use Date.now() to track the last call time.",
            "test": "'Date.now' in code"
        },
        {
            "question": "Create a function 'memoize' that caches function results to optimize performance.",
            "solution": "function memoize(fn) { let cache = {}; return function(x) { if (x in cache) return cache[x]; return cache[x] = fn(x); }; }",
            "hint": "Use an object to store results.",
            "test": "'cache' in code"
        },
        {
            "question": "Create a function 'mapArray' that mimics the behavior of Array.prototype.map using a higher-order function.",
            "solution": "function mapArray(arr, fn) { let result = []; for (let i of arr) result.push(fn(i)); return result; }",
            "hint": "Loop over the array and apply the function to each element.",
            "test": "'for' in code and 'fn' in code"
        },
        {
            "question": "Create a function 'filterArray' that mimics the behavior of Array.prototype.filter using a higher-order function.",
            "solution": "function filterArray(arr, fn) { let result = []; for (let i of arr) if (fn(i)) result.push(i); return result; }",
            "hint": "Loop over the array and add elements that pass the test.",
            "test": "'for' in code and 'if' in code"
        },
        {
            "question": "Create a function 'reduceArray' that mimics Array.prototype.reduce.",
            "solution": "function reduceArray(arr, fn, initial) { let acc = initial; for (let i of arr) acc = fn(acc, i); return acc; }",
            "hint": "Loop over the array, updating the accumulator.",
            "test": "'for' in code and 'fn(acc, i)' in code"
        },
        {
            "question": "Create a function 'bindExample' that binds an object's method to always use its own context.",
            "solution": "let obj = { value: 10, getValue: function() { return this.value; } }; let boundFunc = obj.getValue.bind(obj);",
            "hint": "Use bind() to ensure the correct 'this' context.",
            "test": "'bind(' in code"
        },
        {
            "question": "Create a function 'partial' that allows partial application of functions.",
            "solution": "function partial(fn, ...fixedArgs) { return function(...remainingArgs) { return fn(...fixedArgs, ...remainingArgs); }; }",
            "hint": "Use spread syntax to capture fixed and remaining arguments.",
            "test": "'...' in code"
        }
    ]
}
{
    "name": "JavaScript Asynchronous JavaScript",
    "description": "Learn about Promises and Async/Await in JavaScript.",
    "puzzles": [
        {
            "question": "Create a function 'fetchData' that returns a promise resolving with 'Data fetched' after 2 seconds.",
            "solution": "function fetchData() { return new Promise(resolve => setTimeout(() => resolve('Data fetched'), 2000)); }",
            "hint": "Use setTimeout inside a Promise.",
            "test": "'new Promise' in code and 'setTimeout' in code"
        },
        {
            "question": "Create an async function 'getData' that waits for 'fetchData' and logs the result.",
            "solution": "async function getData() { let data = await fetchData(); console.log(data); }",
            "hint": "Use async/await syntax.",
            "test": "'async function' in code and 'await' in code"
        },
        {
            "question": "Create a function 'fetchWithCallback' that takes a callback and calls it with 'Data received' after 2 seconds.",
            "solution": "function fetchWithCallback(cb) { setTimeout(() => cb('Data received'), 2000); }",
            "hint": "Use setTimeout to delay callback execution.",
            "test": "'setTimeout' in code"
        },
        {
            "question": "Convert 'fetchWithCallback' into a promise-based function 'fetchPromise'.",
            "solution": "function fetchPromise() { return new Promise(resolve => fetchWithCallback(resolve)); }",
            "hint": "Wrap the callback function inside a promise.",
            "test": "'new Promise' in code"
        },
        {
            "question": "Create a function 'parallelRequests' that runs two fetch promises in parallel and logs both results.",
            "solution": "async function parallelRequests() { let results = await Promise.all([fetchData(), fetchData()]); console.log(results); }",
            "hint": "Use Promise.all to wait for multiple promises.",
            "test": "'Promise.all' in code"
        },
        {
            "question": "Create a function 'fetchWithError' that rejects with 'Error fetching data' after 2 seconds.",
            "solution": "function fetchWithError() { return new Promise((_, reject) => setTimeout(() => reject('Error fetching data'), 2000)); }",
            "hint": "Use reject inside a Promise.",
            "test": "'reject' in code"
        },
        {
            "question": "Handle errors in 'getData' using try-catch block.",
            "solution": "async function getData() { try { let data = await fetchWithError(); console.log(data); } catch (error) { console.error(error); } }",
            "hint": "Wrap await call inside try-catch.",
            "test": "'try' in code and 'catch' in code"
        },
        {
            "question": "Create a function 'fetchWithFinally' that logs 'Request completed' in a finally block.",
            "solution": "async function fetchWithFinally() { try { let data = await fetchData(); console.log(data); } finally { console.log('Request completed'); } }",
            "hint": "Use finally after try-catch.",
            "test": "'finally' in code"
        },
        {
            "question": "Create a function 'raceRequests' that logs the fastest result from two fetch promises.",
            "solution": "async function raceRequests() { let result = await Promise.race([fetchData(), fetchWithError()]); console.log(result); }",
            "hint": "Use Promise.race to get the first resolved/rejected promise.",
            "test": "'Promise.race' in code"
        },
        {
            "question": "Create a function 'sequentialRequests' that runs two fetch promises sequentially and logs both results.",
            "solution": "async function sequentialRequests() { let first = await fetchData(); console.log(first); let second = await fetchData(); console.log(second); }",
            "hint": "Use multiple await calls in sequence.",
            "test": "'await' in code and 'console.log' in code"
        },
        {
            "question": "Create a function 'timeoutPromise' that rejects if 'fetchData' takes more than 3 seconds.",
            "solution": "function timeoutPromise() { return Promise.race([fetchData(), new Promise((_, reject) => setTimeout(() => reject('Timeout exceeded'), 3000))]); }",
            "hint": "Use Promise.race with a timeout reject promise.",
            "test": "'Promise.race' in code"
        },
        {
            "question": "Create a function 'delayedLog' that logs a message after 1 second using async/await.",
            "solution": "async function delayedLog() { await new Promise(resolve => setTimeout(resolve, 1000)); console.log('Delayed log'); }",
            "hint": "Await a timeout inside an async function.",
            "test": "'await' in code and 'setTimeout' in code"
        },
        {
            "question": "Create a function 'resolveImmediately' that returns a promise resolved immediately with 'Resolved'.",
            "solution": "function resolveImmediately() { return Promise.resolve('Resolved'); }",
            "hint": "Use Promise.resolve().",
            "test": "'Promise.resolve' in code"
        },
        {
            "question": "Create a function 'rejectImmediately' that returns a promise rejected immediately with 'Rejected'.",
            "solution": "function rejectImmediately() { return Promise.reject('Rejected'); }",
            "hint": "Use Promise.reject().",
            "test": "'Promise.reject' in code"
        },
        {
            "question": "Create an async function 'fetchAndLog' that logs data, catches errors, and logs 'Done' after fetching.",
            "solution": "async function fetchAndLog() { try { let data = await fetchWithError(); console.log(data); } catch (error) { console.error(error); } finally { console.log('Done'); } }",
            "hint": "Use try-catch-finally inside an async function.",
            "test": "'try' in code and 'finally' in code"
        }
    ]
}
{
    "name": "JavaScript Error Handling & Debugging",
    "description": "Learn about error handling techniques and debugging in JavaScript.",
    "puzzles": [
        {
            "question": "Create a try-catch block that handles a ReferenceError when calling an undefined function.",
            "solution": "try { undefinedFunction(); } catch (error) { console.error(error); }",
            "hint": "Wrap the function call inside a try block and catch the error.",
            "test": "'try' in code and 'catch' in code"
        },
        {
            "question": "Create a function 'safeDivide' that returns 'Cannot divide by zero' if the denominator is zero.",
            "solution": "function safeDivide(a, b) { try { if (b === 0) throw new Error('Cannot divide by zero'); return a / b; } catch (error) { return error.message; } }",
            "hint": "Use throw inside try block to raise an error.",
            "test": "'try' in code and 'throw' in code"
        },
        {
            "question": "Use finally in a function 'logCompletion' to always log 'Process completed'.",
            "solution": "function logCompletion() { try { console.log('Processing...'); } finally { console.log('Process completed'); } }",
            "hint": "Use a finally block after try.",
            "test": "'finally' in code"
        },
        {
            "question": "Create a function 'parseJSON' that catches JSON parsing errors and returns 'Invalid JSON'.",
            "solution": "function parseJSON(json) { try { return JSON.parse(json); } catch (error) { return 'Invalid JSON'; } }",
            "hint": "Use try-catch around JSON.parse.",
            "test": "'JSON.parse' in code and 'catch' in code"
        },
        {
            "question": "Create a function 'validateNumber' that throws an error if input is not a number.",
            "solution": "function validateNumber(input) { if (typeof input !== 'number') throw new TypeError('Input must be a number'); return input; }",
            "hint": "Use typeof to check input type before proceeding.",
            "test": "'throw' in code and 'typeof' in code"
        },
        {
            "question": "Create a function 'handlePromiseError' that catches rejections from a promise.",
            "solution": "async function handlePromiseError() { try { let data = await Promise.reject('Promise rejected'); console.log(data); } catch (error) { console.error(error); } }",
            "hint": "Use try-catch around await.",
            "test": "'try' in code and 'await' in code"
        },
        {
            "question": "Create a function 'customError' that defines and throws a custom error with a message.",
            "solution": "class CustomError extends Error { constructor(message) { super(message); this.name = 'CustomError'; } } function customError() { throw new CustomError('Something went wrong'); }",
            "hint": "Extend Error class to create a custom error.",
            "test": "'class' in code and 'extends Error' in code"
        },
        {
            "question": "Create a function 'retryOperation' that retries a function up to 3 times if it fails.",
            "solution": "async function retryOperation(fn, retries = 3) { for (let i = 0; i < retries; i++) { try { return await fn(); } catch (error) { if (i === retries - 1) throw error; } } }",
            "hint": "Use a loop with try-catch inside.",
            "test": "'for' in code and 'try' in code"
        },
        {
            "question": "Create a function 'debugMessage' that logs messages using console.debug().",
            "solution": "function debugMessage(msg) { console.debug(msg); }",
            "hint": "Use console.debug for debugging output.",
            "test": "'console.debug' in code"
        },
        {
            "question": "Create a function 'silentError' that runs a function and returns null if it throws an error.",
            "solution": "function silentError(fn) { try { return fn(); } catch { return null; } }",
            "hint": "Use try-catch but return null on error.",
            "test": "'try' in code and 'catch' in code"
        },
        {
            "question": "Use console.trace() inside a function 'traceExecution' to print the function call stack.",
            "solution": "function traceExecution() { console.trace('Tracing execution'); }",
            "hint": "Use console.trace to log stack trace.",
            "test": "'console.trace' in code"
        },
        {
            "question": "Create a function 'logWarning' that logs a warning using console.warn().",
            "solution": "function logWarning(msg) { console.warn(msg); }",
            "hint": "Use console.warn to log a warning.",
            "test": "'console.warn' in code"
        },
        {
            "question": "Create a function 'logError' that logs an error using console.error().",
            "solution": "function logError(msg) { console.error(msg); }",
            "hint": "Use console.error to log an error.",
            "test": "'console.error' in code"
        },
        {
            "question": "Create a function 'handleNestedErrors' that catches an error inside another try-catch block.",
            "solution": "function handleNestedErrors() { try { try { throw new Error('Inner error'); } catch (innerError) { console.error('Inner:', innerError); throw new Error('Outer error'); } } catch (outerError) { console.error('Outer:', outerError); } }",
            "hint": "Use nested try-catch blocks.",
            "test": "'try' in code and 'catch' in code"
        },
        {
            "question": "Create a function 'catchAll' that catches any error and logs 'An error occurred'.",
            "solution": "function catchAll(fn) { try { return fn(); } catch { console.error('An error occurred'); } }",
            "hint": "Use catch without specifying error parameter.",
            "test": "'catch' in code and 'console.error' in code"
        }
    ]
}{
    "name": "JavaScript Object-Oriented Programming (Classes, Prototypes, Inheritance)",
    "description": "Learn about Object-Oriented Programming in JavaScript, including classes, prototypes, and inheritance.",
    "puzzles": [
        {
            "question": "Create a class 'Person' with a constructor that sets 'name' and 'age'.",
            "solution": "class Person { constructor(name, age) { this.name = name; this.age = age; } }",
            "hint": "Use the 'class' keyword and a constructor function.",
            "test": "'class' in code and 'constructor' in code"
        },
        {
            "question": "Extend the 'Person' class to create a 'Student' class with an additional 'grade' property.",
            "solution": "class Student extends Person { constructor(name, age, grade) { super(name, age); this.grade = grade; } }",
            "hint": "Use 'extends' to inherit from another class and 'super' to call the parent constructor.",
            "test": "'extends' in code and 'super' in code"
        },
        {
            "question": "Add a method 'introduce' to the 'Person' class that returns 'My name is NAME and I am AGE years old.'",
            "solution": "class Person { constructor(name, age) { this.name = name; this.age = age; } introduce() { return `My name is ${this.name} and I am ${this.age} years old.`; } }",
            "hint": "Define a method inside the class that uses template literals.",
            "test": "'introduce' in code and 'return' in code"
        },
        {
            "question": "Create a prototype method 'greet' for a function constructor 'Animal' that returns 'Hello from TYPE'.",
            "solution": "function Animal(type) { this.type = type; } Animal.prototype.greet = function() { return `Hello from ${this.type}`; };",
            "hint": "Use the prototype property to define methods on a constructor function.",
            "test": "'prototype' in code and 'function' in code"
        },
        {
            "question": "Create an instance of 'Person' named 'john' with name 'John' and age 30.",
            "solution": "const john = new Person('John', 30);",
            "hint": "Use the 'new' keyword to create an instance of a class.",
            "test": "'new' in code and 'Person' in code"
        },
        {
            "question": "Create a getter 'fullName' in a class 'User' that returns 'firstName lastName'.",
            "solution": "class User { constructor(firstName, lastName) { this.firstName = firstName; this.lastName = lastName; } get fullName() { return `${this.firstName} ${this.lastName}`; } }",
            "hint": "Use the 'get' keyword to define a getter method.",
            "test": "'get' in code and 'fullName' in code"
        },
        {
            "question": "Create a static method 'describe' in a class 'Vehicle' that returns 'Vehicles are used for transportation'.",
            "solution": "class Vehicle { static describe() { return 'Vehicles are used for transportation'; } }",
            "hint": "Use the 'static' keyword to define a class method.",
            "test": "'static' in code and 'describe' in code"
        },
        {
            "question": "Create an instance of 'Student' named 'alice' with name 'Alice', age 20, and grade 'A'.",
            "solution": "const alice = new Student('Alice', 20, 'A');",
            "hint": "Use 'new' to instantiate a class with multiple parameters.",
            "test": "'new' in code and 'Student' in code"
        },
        {
            "question": "Use Object.create() to create an object 'dog' inheriting from 'animalPrototype' with a 'bark' method.",
            "solution": "const animalPrototype = { species: 'Animal' }; const dog = Object.create(animalPrototype); dog.bark = function() { return 'Woof!'; };",
            "hint": "Use Object.create() to inherit from another object.",
            "test": "'Object.create' in code and 'bark' in code"
        },
        {
            "question": "Use Object.assign() to merge two objects 'obj1' and 'obj2'.",
            "solution": "const obj1 = { a: 1 }; const obj2 = { b: 2 }; const mergedObj = Object.assign({}, obj1, obj2);",
            "hint": "Use Object.assign() to merge properties of objects.",
            "test": "'Object.assign' in code"
        },
        {
            "question": "Create a symbol property 'id' for a class 'Employee'.",
            "solution": "class Employee { constructor(name) { this.name = name; this.id = Symbol('id'); } }",
            "hint": "Use the Symbol function to create a unique property.",
            "test": "'Symbol' in code"
        },
        {
            "question": "Use the instanceof operator to check if 'john' is an instance of 'Person'.",
            "solution": "console.log(john instanceof Person);",
            "hint": "Use the 'instanceof' keyword to check object type.",
            "test": "'instanceof' in code"
        },
        {
            "question": "Create a private field '#salary' in a class 'Employee'.",
            "solution": "class Employee { #salary; constructor(name, salary) { this.name = name; this.#salary = salary; } }",
            "hint": "Use '#' to define private fields in classes.",
            "test": "'#salary' in code"
        },
        {
            "question": "Create a class 'Rectangle' with a method 'area' that returns width * height.",
            "solution": "class Rectangle { constructor(width, height) { this.width = width; this.height = height; } area() { return this.width * this.height; } }",
            "hint": "Define a method inside the class to calculate area.",
            "test": "'area' in code and '*' in code"
        },
        {
            "question": "Create a function 'isPrototypeOfExample' that checks if 'Person.prototype' is the prototype of 'john'.",
            "solution": "function isPrototypeOfExample() { return Person.prototype.isPrototypeOf(john); }",
            "hint": "Use isPrototypeOf() to check prototype inheritance.",
            "test": "'isPrototypeOf' in code"
        }
    ]
}
{
    "name": "JavaScript APIs & Advanced Topics (Fetch API, Event Loop, Local Storage, Modules)",
    "description": "Explore advanced JavaScript concepts such as Fetch API, Event Loop, Local Storage, and Modules through engaging puzzles.",
    "puzzles": [
        {
            "question": "Use Fetch API to get data from 'https://jsonplaceholder.typicode.com/posts/1' and log the response.",
            "solution": "fetch('https://jsonplaceholder.typicode.com/posts/1')\n    .then(response => response.json())\n    .then(data => console.log(data));",
            "hint": "Use fetch() followed by .then() to handle the response.",
            "test": "'fetch' in code and 'then' in code"
        },
        {
            "question": "Explain what the Event Loop does in JavaScript.",
            "solution": "The Event Loop continuously checks the call stack and task queue, executing tasks from the queue when the stack is empty.",
            "hint": "It helps in handling asynchronous operations.",
            "test": "'Event Loop' in answer"
        },
        {
            "question": "Store a user's name in Local Storage with key 'username'.",
            "solution": "localStorage.setItem('username', 'JohnDoe');",
            "hint": "Use localStorage.setItem(key, value).",
            "test": "'localStorage.setItem' in code"
        },
        {
            "question": "Retrieve the 'username' from Local Storage and log it to the console.",
            "solution": "console.log(localStorage.getItem('username'));",
            "hint": "Use localStorage.getItem(key) to retrieve data.",
            "test": "'localStorage.getItem' in code"
        },
        {
            "question": "Create a JavaScript module that exports a function 'greet' returning 'Hello, World!'.",
            "solution": "export function greet() { return 'Hello, World!'; }",
            "hint": "Use the export keyword before the function declaration.",
            "test": "'export' in code and 'function' in code"
        },
        {
            "question": "Import the 'greet' function from a module named 'utils.js'.",
            "solution": "import { greet } from './utils.js';",
            "hint": "Use the import keyword to bring functions from another file.",
            "test": "'import' in code and 'from' in code"
        },
        {
            "question": "Use async/await to fetch data from 'https://jsonplaceholder.typicode.com/posts/1'.",
            "solution": "async function getData() {\n    let response = await fetch('https://jsonplaceholder.typicode.com/posts/1');\n    let data = await response.json();\n    console.log(data);\n}",
            "hint": "Use async function with await inside.",
            "test": "'async' in code and 'await' in code"
        },
        {
            "question": "Explain the difference between sessionStorage and localStorage.",
            "solution": "sessionStorage stores data for a session and is cleared when the page is closed, while localStorage persists data even after the browser is closed.",
            "hint": "Think about how long each storage type keeps data.",
            "test": "'sessionStorage' in answer and 'localStorage' in answer"
        },
        {
            "question": "Remove 'username' from Local Storage.",
            "solution": "localStorage.removeItem('username');",
            "hint": "Use localStorage.removeItem(key).",
            "test": "'localStorage.removeItem' in code"
        },
        {
            "question": "Explain what happens when calling setTimeout with a delay of 0ms.",
            "solution": "setTimeout with 0ms still goes into the task queue and executes after the current call stack is cleared.",
            "hint": "Think about the Event Loop and task queue.",
            "test": "'setTimeout' in answer and 'task queue' in answer"
        },
        {
            "question": "Create a Web Worker script that logs 'Hello from Worker!'.",
            "solution": "self.onmessage = function(event) { console.log('Hello from Worker!'); };",
            "hint": "Use self.onmessage in a worker script.",
            "test": "'self.onmessage' in code"
        },
        {
            "question": "Explain the difference between synchronous and asynchronous code in JavaScript.",
            "solution": "Synchronous code executes line by line, blocking execution, while asynchronous code allows non-blocking execution with callbacks, promises, or async/await.",
            "hint": "Think about how execution is handled in the call stack.",
            "test": "'synchronous' in answer and 'asynchronous' in answer"
        },
        {
            "question": "Use navigator.geolocation API to get the user's current location.",
            "solution": "navigator.geolocation.getCurrentPosition(position => console.log(position));",
            "hint": "Use navigator.geolocation.getCurrentPosition(callback).",
            "test": "'navigator.geolocation.getCurrentPosition' in code"
        },
        {
            "question": "Explain the purpose of the BroadcastChannel API in JavaScript.",
            "solution": "The BroadcastChannel API allows communication between different browser contexts (e.g., tabs, windows) with the same origin.",
            "hint": "Think about how different browser tabs can communicate.",
            "test": "'BroadcastChannel' in answer"
        },
        {
            "question": "Explain the difference between import and require in JavaScript.",
            "solution": "import is used in ES modules and supports static analysis, while require is used in CommonJS modules and supports dynamic imports.",
            "hint": "Think about module systems in JavaScript.",
            "test": "'import' in answer and 'require' in answer"
        }
    ]
}


