"""Игра «Арифметическая прогрессия»: найти пропущенное число."""

import random

def generate_progression(start, step, length, hidden_index):
    """Генерирует строку прогрессии с пропуском."""
    progression = []
    for i in range(length):
        if i == hidden_index:
            progression.append('..')
        else:
            progression.append(str(start + i * step))
    return ' '.join(progression)

def generate_round():
    """Возвращает вопрос (прогрессию с пропуском) и правильный ответ."""
    length = random.randint(5, 10)          # длина прогрессии (не менее 5)
    start = random.randint(1, 20)           # начальное число
    step = random.randint(1, 10)             # шаг прогрессии
    hidden_index = random.randint(0, length - 1)   # позиция пропуска
    hidden_value = start + hidden_index * step     # пропущенное число

    question = generate_progression(start, step, length, hidden_index)
    return question, str(hidden_value)
