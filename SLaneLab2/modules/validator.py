
from constants import OPERATORS

def is_operator(ch):
    return ch in OPERATORS

def is_operand(token):
    return token.isalpha() or token.isdigit()

def tokenize_compact_expression(expr):
    tokens = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch in OPERATORS:
            tokens.append(ch)
            i += 1
        elif ch.isdigit():
            num = ''
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(num)
        elif ch.isalpha():
            tokens.append(ch)
            i += 1
        elif ch.isspace():
            i += 1  # skip spaces if any
        else:
            raise ValueError(f"Invalid character: '{ch}'")
    return tokens

def tokenize_expression(expr):
    expr = expr.strip()
    if " " in expr:
        return expr.split()
    else:
        return tokenize_compact_expression(expr)

def validate_expression(expr):
    """
    Error handling: returns None if no error present
    Errors detected: empty files, missing data, expressions starting with an operand, 
    invalid characters, correct number of operands/operators (operands = operators - 1)
    """
    if not expr.strip():
        raise ValueError("Empty expression")

    tokens = tokenize_expression(expr)

    if not is_operator(tokens[0]):
        raise ValueError("Expression must start with an operator")

    for token in tokens:
        if not (is_operator(token) or is_operand(token)):
            raise ValueError(f"Invalid token: '{token}'")

    num_operands = sum(1 for t in tokens if is_operand(t))
    num_operators = sum(1 for t in tokens if is_operator(t))

    if num_operands <= num_operators:
        raise ValueError("Too few operands for the number of operators")
    if num_operands > num_operators + 1:
        raise ValueError("Too many operands for the number of operators")

    return tokens