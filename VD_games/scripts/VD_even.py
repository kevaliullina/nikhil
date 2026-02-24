import random
from VD_games.cli import welcome_user

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    rounds = 3

    while correct_answers < rounds:
        number = random.randint(1, 100)
        correct = 'yes' if number % 2 == 0 else 'no'

        print(f'Question: {number}')
        answer = input('Your answer: ').strip().lower()

        if answer == correct:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

if __name__ == '__main__':
    main()
