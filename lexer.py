
import re


def tokenize(expression):
    tokens = re.findall(r'[a-zA-Z]+|\d+|[+\-*/=()]', expression)
    return tokens
