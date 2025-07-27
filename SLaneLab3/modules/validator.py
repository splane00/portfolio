"""
Validator module to handle input verification for the Huffman Encoding program.
Includes functions to validate frequency table format and allowed characters in input files.
"""

def validate_freq_table_format(freq_table):
    """
    Ensure the frequency table is in the correct format:
    - Dictionary with single characters as keys (letters, numbers, punctuation)
    - Frequencies are positive integers
    """
    if not isinstance(freq_table, dict):
        raise ValueError("Frequency table must be a dictionary.")
    
    for char, freq in freq_table.items():
        if not isinstance(char, str) or len(char) != 1:
            raise ValueError(f"Invalid character key: {char}")
        if not isinstance(freq, int) or freq <= 0:
            raise ValueError(f"Invalid frequency for {char}: {freq}")
    return True

def validate_text_characters(text, valid_chars):
    """
    Ensure the input text contains only characters that exist in the frequency table.
    """
    return ''.join(ch for ch in text if ch.upper() in valid_chars or ch == '\n')
