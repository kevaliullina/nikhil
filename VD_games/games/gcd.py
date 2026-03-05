"""Игра «НОД»: нахождение наибольшего общего делителя."""

import random
import math

def generate_round():
    """Возвращает два числа и их НОД."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(correct)
