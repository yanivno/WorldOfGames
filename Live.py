import utils
from games.MemoryGame import MemoryGame
from games.CurrencyRouletteGame import CurrencyRouletteGame
from games.GuessGame import GuessGame


# receives a person name and prints welcome message
def welcome(name):
    welcome_msg = f"""Hello {name} and welcome to the World of Games (WoG)
Here you can find many cool games to play
"""
    return welcome_msg


# interacts with the user to load the game
def load_game():
    game_menu = """Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
Enter your selection: """
    diff_menu = """Please choose game difficulty from 1 to 5:"""
    game_selection = utils.get_num_input_in_range(game_menu, 1, 3)
    diff_selection = utils.get_num_input_in_range(diff_menu, 1, 5)
    # the return is used only for now...
    games = {'1': MemoryGame, '2': GuessGame, '3': CurrencyRouletteGame}
    game = games[str(game_selection)](diff_selection)
    is_user_winner = game.play()
    user_title = 'WINNER' if is_user_winner else 'LOSER'
    print(f"You are a {user_title}. Good Bye")





