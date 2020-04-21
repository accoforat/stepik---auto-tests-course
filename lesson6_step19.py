from selenium import webdriver
import time
import math
import os 

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
  
    

    input1 = browser.find_element_by_class_name('trollface')
    input1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window (new_window)
    print (new_window)
	
    
    any_text = browser.find_element_by_id ('input_value')
    x = any_text.text

    z = str((math.log(abs(12*math.sin(int(x))))))
    
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(z)
   
    

    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
