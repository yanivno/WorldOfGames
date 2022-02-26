from utils import FLASK_IP_BIND, FLASK_PORT_BIND
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
import logging


def test_scores_service(URL):
    drv_file = os.path.join(os.path.dirname(__file__), 'chromedriver')
    driver = webdriver.Chrome(executable_path=drv_file)
    driver.get(URL)
    scores = driver.find_elements(By.XPATH, "//*[contains(@id, 'score_')]")
    is_valid = True
    for score in scores:
        if not (score.text.isnumeric() and 0 <= int(score.text) <= 100):
            is_valid = False
    driver.close()
    return is_valid


def main_function():
    uri = f"http://{FLASK_IP_BIND}:{FLASK_PORT_BIND}"
    score = test_scores_service(uri)
    exit_code = -1
    if score:
        exit_code = 0
    logging.log(0, f"scoring module testing exit code {exit_code}")


main_function()
