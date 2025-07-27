
from file_io import read_input_file, write_output_file
from prefix_to_postfix import convert_prefix_to_postfix
from validator import validate_expression
from constants import OPERATORS


def convert_line(line, line_number):
    """
    Creates labels for each line of input and converts expression to list.
    Includes error handling for unnecessary text in input file.
    """
    try:
        tokens = validate_expression(line)  # returns token list
        index = [0]
        result = convert_prefix_to_postfix(tokens, index)

        if index[0] != len(tokens):
            raise ValueError("Extra characters found after valid prefix expression")

        return f"{line_number}: {result}"
    except ValueError as e:
        return f"Line {line_number} ERROR: {str(e)}"

def main():
    input_filename = input("Enter input filename: ")
    output_filename = input("Enter output filename: ")

    try:
        lines = read_input_file(input_filename)
        results = []
        for i, line in enumerate(lines, start=1):
            results.append(convert_line(line, i))
            print(results[-1])
        write_output_file(output_filename, results)
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
