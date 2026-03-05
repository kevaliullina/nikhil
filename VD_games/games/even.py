"""Игра «Чётное/нечётное»."""

import random

def generate_round():
    num = random.randint(1, 100)
    correct = 'yes' if num % 2 == 0 else 'no'
    return str(num), correct
