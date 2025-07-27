Samantha Lane
Data Structures Lab 3

Huffman Encoding Tree Implementation

Features
- Reads a frequency table from a file.
- Constructs a Huffman tree using frequency ascending, single-character nodes before multi-character nodes, and alphabetical order for tie-breaking
- Prints the tree using preorder traversal.
- Generates Huffman codes for each character.
- Encodes plain text into binary strings.
- Decodes binary strings back into the original text.
- Saves Huffman tree, Huffman codes, and encoded/decoded outputs to files.

File Structure
main.py
- Reads input file paths
- Builds the Huffman tree
- Encodes and decodes files
- Prints outputs and writes encoded/decoded files

tree.py
- Node class representing nodes of the Huffman tree
- HuffmanTree class to build the tree, generate codes, encode, and decode

files.py
- read_freq_table(filename) — parses frequency table file
- read_text_file(filename) — reads plain or encoded text files

validator.py
- Validates frequency table format 
- Validates allowed characters in input files

The program will prompt for:
1. Frequency table file path (e.g., /SLaneLab3/input_output/FreqTable.txt)
2. Input file path to encode or decode (e.g., /SLaneLab3/input_output/ClearText.txt)

Outputs:
Saved to output.txt

Dependencies:
Python 3.x
