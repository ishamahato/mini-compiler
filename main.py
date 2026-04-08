

from lexer import tokenize
from parser import parse
from intermediate_code import generate_TAC

expression = input("Enter expression: ")

tokens = tokenize(expression)
left, right = parse(tokens)

tac, result = generate_TAC(right)

for line in tac:
    print(line)

print(f"{left} = {result}")