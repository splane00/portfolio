
from constants import OPERATORS
from validator import is_operator, is_operand


def convert_prefix_to_postfix(tokens, index):
    """
    Recursively converts a prefix expression token list to postfix string.

    Args:
        tokens (list): List of tokens representing the prefix expression.
        index (list): Single-element list tracking current parsing position.

    Returns:
        str: Postfix expression string.

    Raises:
        ValueError: If tokens run out or invalid token found.
    """
    if index[0] >= len(tokens):
        raise ValueError("Incomplete expression: ran out of tokens")

    token = tokens[index[0]]
    index[0] += 1

    if is_operator(token):
        left = convert_prefix_to_postfix(tokens, index)
        right = convert_prefix_to_postfix(tokens, index)
        return f"{left} {right} {token}"
    elif is_operand(token):
        return token
    else:
        raise ValueError(f"Invalid token: '{token}'")
