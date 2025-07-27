"""
Operations:
1. Reads frequency table from 'FreqTable.txt' using `read_freq_table`.
2. Constructs a Huffman Tree from the frequency table.
3. Prints the tree in preorder traversal.
4. Prints Huffman codes for each character.
5. Reads clear text from 'ClearText.txt', encodes it using the Huffman Tree, and prints the encoded result.
6. Reads encoded text from 'Encoded.txt', decodes it using the Huffman Tree, and prints the decoded result.

Dependencies:
- tree.py: Contains the `HuffmanTree` class for building and operating on the Huffman Tree.
- files.py: Provides `read_freq_table` and `read_text_file` for file operations.
"""

from files import read_freq_table, read_text_file, write_to_file
from tree import HuffmanTree
from validator import validate_text_characters

def is_binary_string(s):
    return all(c in {'0', '1'} for c in s.replace('\n', '').replace(' ', ''))

def main():
    freq_path = input('Input file path to frequency table: ')
    freq_table = read_freq_table(freq_path)
    freq_table.pop('\n', None)

    if not freq_table:
        print("Error: Frequency table is empty or invalid.")
        return

    tree = HuffmanTree(freq_table)
    tree.build_tree()
    tree.generate_codes()

    input_path = input("Input file path to data to encode/decode: ").strip()
    input_text = read_text_file(input_path)

    input_lines = input_text.splitlines()

    result_lines = []

    for line in input_lines:
        cleaned_line = ''.join(line.split())  # remove whitespace

        if cleaned_line == "":
            # Preserve empty lines as is
            result_lines.append("")
            continue

        # Check if line looks like encoded (only 0 and 1)
        if all(c in {'0', '1'} for c in cleaned_line):
            # It's encoded line → decode it
            decoded = tree.decode(cleaned_line)
            result_lines.append(decoded)
        else:
            # If line contains chars other than 0 and 1 (and whitespace),
            # treat as text to encode

            # But if it contains any chars outside freq_table keys, remove them
            validated = validate_text_characters(line, freq_table.keys())

            if validated == "":
                # No valid characters to encode, write error message for this line
                result_lines.append("ERROR: Line contains invalid characters.")
            else:
                encoded = tree.encode(validated)
                result_lines.append(encoded)

    result = '\n'.join(result_lines)

    # Tree and code output (for reference)
    tree_output = tree.preorder(tree.root)
    code_output = "\n".join(
        f"{char}: {code}" for char, code in tree.codes.items()
    )

    full_output = (
        "HUFFMAN TREE (Preorder Traversal):\n"
        + tree_output
        + "\nHUFFMAN CODES:\n"
        + code_output
        + f"\n\nRESULT: \n"
        + result
    )

    output_path = "/Users/samilane/Documents/VSCode/JHU/Data Structures/SLaneLab3/input_output/OUTPUT.txt"
    write_to_file(output_path, full_output)
    print(f"Result saved to: {output_path}")

main()