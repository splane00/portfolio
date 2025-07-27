
def read_input_file(filename):
    # Reads the input file line by line, ignoring blank lines. 
    # Includes error handling for empty files and incorrect file names.
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
        if not lines:
            raise ValueError("Input file is empty or only contains blank lines")
        return lines
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")

def write_output_file(filename, results):
   # Writes results to the designated output file.
    with open(filename, 'w') as file:
        for line in results:
            file.write(line + '\n')
