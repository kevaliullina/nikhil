from VD_games.engine import run_game
from VD_games.games.gcd import generate_round

def main():
    description = "Find the greatest common divisor of given numbers."
    run_game(generate_round, description)

if __name__ == "__main__":
    main()
