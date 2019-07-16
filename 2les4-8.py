#Задание: ждем нужный текст на странице

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)

#открыть страницу
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

#подождать цену 10000 RUR (12 сек)
label = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )
button1 = browser.find_element_by_id("book")
button1.click()

##считываем и рассчитываем значение для переменной х 
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

#введем значение answer в поле
input1 = browser.find_element_by_id("answer")
input1.send_keys(y)


#нажимаем кнопку Отправить 
button2 = browser.find_element_by_id("solve")
button2.click()




