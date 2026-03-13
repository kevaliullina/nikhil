"""Игра «Простое ли число?»: определить, является ли число простым."""

import random

def is_prime(num):
    """Проверяет, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_round():
    """Возвращает вопрос (число) и правильный ответ (yes/no)."""
    number = random.randint(1, 100)
    correct = 'yes' if is_prime(number) else 'no'
    return str(number), correct
