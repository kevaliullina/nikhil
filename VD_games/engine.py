"""Общий движок для проведения игр."""

from VD_games.cli import welcome_user

def run_game(generate_round, description):
    name = welcome_user()
    print(description)

    rounds_count = 3
    correct_answers = 0

    while correct_answers < rounds_count:
        question, correct = generate_round()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip().lower()

        if answer == correct:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
