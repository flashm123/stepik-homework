import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

button = browser.find_element_by_id("book")
button.click()

x = int(browser.find_element_by_id("input_value").text)
result = calc(x)

answer = browser.find_element_by_id("answer")
answer.send_keys(result)

browser.execute_script("window.scrollBy(0, 300);")

solveButton = browser.find_element_by_id("solve")
solveButton.click()
