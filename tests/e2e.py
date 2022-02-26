from utils import FLASK_IP_BIND, FLASK_PORT_BIND
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os
import logging
from utils import GOOD_RETURN_CODE,BAD_RETURN_CODE


def test_scores_service(URL):
    drv_file = os.path.join(os.path.dirname(__file__), 'chromedriver')
    driver = webdriver.Chrome(executable_path=drv_file)
    driver.get(URL)
    scores = driver.find_elements(By.XPATH, "//*[contains(@id, 'score_')]")
    return_code = GOOD_RETURN_CODE
    for score in scores:
        if not (score.text.isnumeric() and 0 <= int(score.text) <= 100):
            return_code = BAD_RETURN_CODE
    driver.close()
    return return_code


def main_function():
    uri = f"http://{FLASK_IP_BIND}:{FLASK_PORT_BIND}"
    exit_code = test_scores_service(uri)
    logging.log(0, f"scoring module testing exit code {exit_code}")
    assert exit_code == GOOD_RETURN_CODE


main_function()
