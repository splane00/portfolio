"""
Contains classes and methods for building and using a Huffman Encoding Tree
based on a frequency table. Implements tree construction with tie-breaking rules,
preorder traversal for printing, code generation, encoding of clear text,
and decoding of encoded bitstrings.
"""

class Node:
    def __init__(self, chars, freq, left=None, right=None):
        self.chars = chars
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None

class HuffmanTree:
    def __init__(self, freq_table):
        self.freq_table = freq_table
        self.codes = {}
        self.root = None

    def build_tree(self):
        """
        Builds a binary tree from the character frequency table.
        The method creates a list of nodes, each representing a character and its frequency (weight).
        It repeatedly merges the two nodes with the lowest frequencies, applying tie-breaking rules:
            1. Frequency ascending
            2. Single-character nodes before multi-character nodes
            3. Alphabetical order of characters
        The merged node combines the characters and frequencies of its children.
        The process continues until only one node remains, which becomes the root of the tree.

        Returns:
            Node: The root node of the constructed tree.
        """
        nodes = [Node(ch, freq) for ch, freq in self.freq_table.items()]

        while len(nodes) > 1:
            """
            Custom sort: freq ascending, single-char before multi-char, alphabetical
            """
            nodes.sort(key=lambda n: (n.freq, len(n.chars) > 1, n.chars))

            left = nodes.pop(0)
            right = nodes.pop(0)

            merged_chars = ''.join(sorted(left.chars + right.chars))
            merged = Node(merged_chars, left.freq + right.freq, left, right)

            nodes.append(merged)

        self.root = nodes[0]
        return self.root

    def preorder(self, node):
        """
        Performs a preorder traversal of the binary tree starting from the given node.

        In preorder traversal, the current node is processed first, followed by the left subtree,
        and then the right subtree. For each visited node, its 'chars' and 'freq' attributes are printed.
        
        Args:
            node: The starting node for the traversal. Should be an instance of a tree node or None.
        """
        if node is None:
            return ""
        result = f"{repr(node.chars)}: {node.freq}\n"
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result


    def generate_codes(self):
        """
        Generates and returns a dictionary of codes for each symbol in the tree.

        This method initializes an empty dictionary to store the codes. If the tree has a root node,
        it recursively traverses the tree to assign a unique code (typically a binary string) to each symbol
        based on its position in the tree. The codes are stored in the `self.codes` attribute and returned.

        Returns:
            dict: A dictionary mapping each symbol to its corresponding code.
        """
        self.codes = {}
        if self.root is not None:
            self._generate_codes_recursive(self.root, "")
            return self.codes


    def _generate_codes_recursive(self, node, code):
        """
        Recursively generates binary codes for each leaf node in the tree.
        Updates the `self.codes` dictionary with character(s) as keys and their corresponding binary codes as values.
        
        Args:
            node: The current node in the tree.
            code (str): The binary code accumulated so far.
        """
        if node is None:
            return
        if node.is_leaf():
            self.codes[node.chars] = code
        else:
            self._generate_codes_recursive(node.left, code + '0')
            self._generate_codes_recursive(node.right, code + '1')

    def encode(self, text):
        """
        Encodes the given text using the predefined character codes.

        Each character in the input text is converted to uppercase and replaced with its corresponding code
        from the `self.codes` dictionary, if available. Characters not present in `self.codes` are ignored.

        Args:
            text (str): The input string to encode.

        Returns:
            str: The encoded string, consisting of the concatenated codes for each valid character.
        """
        return ''.join(self.codes[ch.upper()] for ch in text if ch.upper() in self.codes)

    def decode(self, encoded):
        """
        Decodes a binary string using the tree structure.

        Traverses the tree according to each bit in the encoded string ('0' for left, '1' for right).
        When a leaf node is reached, appends its character(s) to the result and resets to the root.
        Returns the fully decoded string.

        Args:
            encoded (str): The binary string to decode.

        Returns:
            str: The decoded string.
        """
        result = ""
        if self.root is None:
            return result

        node = self.root
        for bit in encoded:
            if node is None:
                break
            if bit == '0':
                node = node.left if node.left is not None else None
            else:
                node = node.right if node.right is not None else None

            if node is not None and node.is_leaf():
                result += node.chars
                node = self.root
        return result

