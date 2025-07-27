Samantha Lane
Data Structures Lab 2

Overview
This program converts prefix expressions to their corresponding postfix expressions using a recursive algorithm. It supports:
- Single-letter operands (e.g., A, B, C)
- Multi-digit numeric operands (e.g., 10, 34)
- Operators: +, -, *, /, $ (exponentiation), and ^ (if included)
- Both space-separated and compact (no spaces) prefix expressions
- The program reads prefix expressions from an input file, validates them with detailed error checking, converts them recursively without using stacks, and writes the results or error messages to an output file.

Features
- Recursive conversion: Converts prefix directly to postfix using recursion, reflecting the natural structure of expressions.
- Robust validation: Detects invalid tokens, operand/operator imbalance, empty lines, illegal characters, and incomplete expressions.
- Multi-digit support: Correctly handles operands with multiple digits both in space-separated and compact input.
- Input flexibility: Accepts prefix expressions written with spaces or compact (e.g., *+AB-CD).
- Helpful error messages: Provides clear, line-numbered feedback on any input errors.
- File I/O: Reads input and writes output from/to files specified by the user.

Files
file_io.py - Handles input/output files
main.py — Program entry point; handles input/output and calls conversion.
validator.py — Validates and tokenizes input expressions.
prefix_to_postfix.py — Contains recursive logic to convert prefix tokens to postfix string.
constants.py — Defines operator characters.