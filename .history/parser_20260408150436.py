
def parse(tokens):
    if "=" not in tokens:
        raise Exception("Invalid Expression")

    left = tokens[0]
    right = tokens[2:]
    
    return left, right
