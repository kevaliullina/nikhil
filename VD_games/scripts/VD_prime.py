from VD_games.engine import run_game
from VD_games.games.prime import generate_round

def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_round, description)

if __name__ == "__main__":
    main()
