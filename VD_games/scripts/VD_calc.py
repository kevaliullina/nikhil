from VD_games.engine import run_game
from VD_games.games.calc import generate_round

def main():
    description = "What is the result of the expression?"
    run_game(generate_round, description)

if __name__ == "__main__":
    main()
