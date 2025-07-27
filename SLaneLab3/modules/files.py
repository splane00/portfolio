"""
Calls input files to be used in main.py. This includes three files: 
1. ClearText.txt (decoded text file)
2. Encoded.txt (encoded file)
3. FreqTable.txt (frequency table)
"""
def read_freq_table(filepath):
    """
    Reads a frequency table file with flexible formats:
    A - 1
    A: 1
    A 1
    A = 1
    A:1, B: 2, C:3
    Will accept comma- or newline-separated entries.
    Returns a dictionary: {char: frequency}
    """
    freq_dict = {}

    with open(filepath, 'r') as file:
        content = file.read()

    # Normalize commas to newlines
    content = content.replace(',', '\n')

    for line in content.splitlines():
        line = line.strip()
        if not line:
            continue  # skip empty lines

        # Try to split line by possible delimiters
        for delimiter in [':', '=', '-', ' ']:
            if delimiter in line:
                parts = line.split(delimiter)
                if len(parts) == 2:
                    char_part = parts[0].strip()
                    freq_part = parts[1].strip()
                    break
        else:
            # If no delimiter found, invalid line - skip or raise error
            print(f"Skipping invalid line: {line}")
            continue

        # Validate char_part length and freq_part is digit
        if len(char_part) == 1 and char_part.isalpha() and freq_part.isdigit():
            char = char_part.upper()
            freq = int(freq_part)
            freq_dict[char] = freq
        else:
            print(f"Skipping invalid line: {line}")
    
    return freq_dict


def add_newline_to_freq_table(freq_table, freq=0):
        """
        Ensure the newline character '\\n' is in the frequency table.
        If not present, add it with the given frequency (default 0).
        """
        if '\n' not in freq_table:
            freq_table['\n'] = freq
        return freq_table

def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_to_file(filepath, data):
    """
    Writes the given data to the specified file.
    
    Args:
        filepath (str): Path to the output file.
        data (str): Text content to write.
    """
    with open(filepath, 'w') as f:
        f.write(data)

