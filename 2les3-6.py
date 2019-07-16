#Задание на alert accetpt

from selenium import webdriver

#открываем нужную страницу в браузере
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

#нажимаем кнопку на первом экране
button1 = browser.find_element_by_class_name("trollface")
button1.click()

#переключаемся на вторую вкладку
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

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
button2 = browser.find_element_by_class_name("btn-primary")
button2.click()

