# McCarthyScript

A minimalist interpreted programming language inspired by Cormac McCarthy's writing style. The language is designed to be direct, unambiguous, and focused on essential operations.

## Features

- Simple, English-like syntax
- Basic arithmetic operations
- String manipulation
- Variable handling
- Input/Output operations

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/mccarthy.git
cd mccarthy
```

2. Ensure you have Python 3.x installed:
```bash
python --version
```

## Usage

Run a McCarthyScript program:
```bash
python mccarthy.py your_program.txt
```

## Language Syntax

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `speak` | Print output | `speak "Hello, world"` |
| `listen` | Get user input | `let name equals listen` |
| `let` | Variable declaration | `let x equals 5` |

### Operations

| Operation | Syntax | Example |
|-----------|--------|---------|
| Multiplication | `multiply num1 multiply num2` | `let product equals multiply 5 multiply 6` |
| Addition | `add num1 add num2` | `let sum equals add 5 add 6` |
| String Concatenation | `concatenate str1 concatenate str2` | `let greeting equals concatenate "Hello" concatenate name` |
| String Reversal | `reverse(str)` | `let reversed equals reverse("hello")` |
| String Repetition | `repeat(str, count)` | `let repeated equals repeat("ha", 3)` |

## Example Programs

### Hello World
```mccarthy
speak "The world was dark and cold. The man spoke."
speak "Hello, world"
```

### Input and Output
```mccarthy
speak "The man stood in the road. He spoke."
speak "What is your name?"
let name equals listen
speak "The man nodded. He said:"
speak concatenate "Hello, " concatenate name
```

### Multiplication
```mccarthy
speak "Enter first number:"
let num1 equals listen
speak "Enter second number:"
let num2 equals listen
let product equals multiply num1 multiply num2
speak "The product is:"
speak product
```

### String Reversal
```mccarthy
speak "Enter a string to reverse:"
let input equals listen
let reversed equals reverse(input)
speak "The reversed string is:"
speak reversed
```

### String Repetition
```mccarthy
speak "Enter a phrase to repeat:"
let phrase equals listen
speak "How many times to repeat it?"
let count equals listen
let repeated equals repeat(phrase, count)
speak "Here is your repeated phrase:"
speak repeated
```

## Language Philosophy

McCarthyScript embraces the sparse, direct style of Cormac McCarthy's writing. The language is designed to be:
- Minimalist
- Direct
- Unambiguous
- Focused on essential operations

Each command should feel like a clear, declarative statement, much like McCarthy's prose.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
