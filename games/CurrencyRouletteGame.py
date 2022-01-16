import utils
import random
from handlers.free_currency_api_handler import get_currency_rate
from games.Game import Game


# This game will use the free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
class CurrencyRouletteGame(Game):

    __comp_money_usd = None
    __usd_ils_exchange_rate = None

    def __init__(self, difficulty):
        Game.__init__(self, difficulty)
        self.__comp_money_usd = random.randint(utils.MINIMUM_ALLOWED_NUM, utils.CURRENCY_ROULETTE_MAX_ALLOWED_NUM)
        self.__usd_ils_exchange_rate = get_currency_rate("ILS")

    # Will get the current currency rate from USD to ILS and will generate an interval as follows:
    # for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t + (5 - d))
    def __get_money_interval(self):
        comp_money_in_ils = self.__comp_money_usd * self.__usd_ils_exchange_rate
        interval_window = (5 - self.get_difficulty())
        min_interval = comp_money_in_ils - interval_window
        max_interval = comp_money_in_ils + interval_window
        return min_interval, max_interval

    # A method to prompt a guess from the user to enter a guess of value to a given amount of USD
    def __get_guess_from_user(self):
        text = f"Try and guess {self.__comp_money_usd}$ in ILS: "
        self.__user_guess_in_ils = utils.get_float_input(text)

    # Will call the functions above and play the game. Will return True / False if the user lost or won.
    def play(self):
        self.__get_guess_from_user()
        interval_min, interval_max = self.__get_money_interval()
        print(f"computer selected a sum between {interval_min:.2f} and {interval_max:.2f}. you chose {self.__user_guess_in_ils}.")
        return interval_min <= self.__user_guess_in_ils <= interval_max
