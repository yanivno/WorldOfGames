import utils
import random
import time
import logging
from games.Game import Game


# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
class MemoryGame(Game):

    __comp_numbers = []
    __user_numbers = []

    def __init__(self, difficulty):
        Game.__init__(self, difficulty)

    # Will generate a list of random numbers between 1 to 101. The list length will be difficulty
    def __generate_sequence(self):
        print("generating number selection...")
        numbers = []
        for i in range(0, self.get_difficulty()):
            number = random.randint(utils.MINIMUM_ALLOWED_NUM, utils.MEMORY_GAME_MAX_ALLOWED_NUM)
            numbers.append(number)
        return numbers

    # Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
    def __get_list_from_user(self):
        numbers = []
        for i in range(1, self.get_difficulty() + 1):
            text = f"enter {i}/{self.get_difficulty()} num: "
            number = utils.get_num_input_in_range(text, utils.MINIMUM_ALLOWED_NUM, utils.MEMORY_GAME_MAX_ALLOWED_NUM)
            numbers.append(number)
        return numbers

    # A function to compare two lists if they are equal. The function will return True / False.
    def __is_list_equal(self):
        result = True
        for i in range(0, self.get_difficulty()):
            logging.debug(f"comparing {self.__comp_numbers[i]} and {self.__user_numbers[i]}")
            if utils.cmp(self.__comp_numbers[i], self.__user_numbers[i]) != 0:
                result = False
                break
        return result

    # Will call the functions above and play the game. Will return True / False if the user lost or won.
    def play(self):
        self.__comp_numbers = self.__generate_sequence()
        print(f"Comp numbers are: {self.__comp_numbers}", end='', flush=True)
        time.sleep(utils.MEMORY_GAME_SLEEP_TIME_SECS)
        print('\r', end='')
        print("DONE. please guess\n")

        logging.debug(f"my numbers are {self.__comp_numbers}")

        self.__user_numbers = self.__get_list_from_user()
        return self.__is_list_equal()
