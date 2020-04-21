from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
#button.click()
input1 = browser.find_element_by_id('book')
input1.click()




any_text = browser.find_element_by_id ('input_value')
x = any_text.text
print (any_text)

z = str((math.log(abs(12*math.sin(int(x))))))
    
input1 = browser.find_element_by_id('answer')
input1.send_keys(z)

button = browser.find_element_by_id("solve")
button.click()