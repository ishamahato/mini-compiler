
def generate_TAC(right):
    temp_count = 1
    output = []

    precedence = {'+':1, '-':1, '*':2, '/':2}

    def apply_op(op, b, a):
        nonlocal temp_count
        temp = f"t{temp_count}"
        temp_count += 1
        output.append(f"{temp} = {a} {op} {b}")
        return temp

    values = []
    ops = []

    for token in right:
        if token.isalnum():
            values.append(token)
        elif token in precedence:
            while (ops and precedence.get(ops[-1], 0) >= precedence[token]):
                op = ops.pop()
                b = values.pop()
                a = values.pop()
                values.append(apply_op(op, b, a))
            ops.append(token)

    while ops:
        op = ops.pop()
        b = values.pop()
        a = values.pop()
        values.append(apply_op(op, b, a))

    return output, values[0]
