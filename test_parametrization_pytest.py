import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link',
                         ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(15)

    browser.get(link)
    answer = math.log(int(time.time()))

    _input = browser.find_element_by_class_name("string-quiz__textarea")
    _input.send_keys(str(answer))

    # time.sleep(3)

    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button.click()

    result = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint"), "Correct!"))

    time.sleep(5)
