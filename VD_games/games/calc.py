"""Игра «Калькулятор»: случайное арифметическое выражение."""

import random
def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(['+', '-', '*'])

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    question = f"{num1} {op} {num2}"
    return question, str(result)
