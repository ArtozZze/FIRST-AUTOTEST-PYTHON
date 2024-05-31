from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#открываем тестируемый ресурс
browser = webdriver.Edge()
browser.get("http://ts.red-promo.ru/")
time.sleep(5)
#массив с элементами для проверки в которых переход происходит на страницу сразу, без всплывающего списка с дополнительными опциями
def get_xpath():
    xpath_array = []
    xpath_array.append("/html/body/div[1]/nav/div[2]/ul/li[1]/a")
    xpath_array.append("/html/body/div[1]/nav/div[2]/ul/li[3]/a")
    xpath_array.append("/html/body/div[1]/nav/div[2]/ul/li[4]/a")
    xpath_array.append("/html/body/div[1]/nav/div[2]/ul/li[5]/a")
    xpath_array.append("/html/body/div[1]/nav/div[2]/ul/li[6]/a")
    return xpath_array
time.sleep(2)
#что нибудь дополнительное для проверок можно добавлять или удалять
chek2 = ["Альтернативные стейки", "Стейки на кости", "Отрубы", "Молочная продукция", "Побаловать себя"]
enter_button = get_xpath()
#цикл для проверки наличия элементов из массива в каталоге веб сайта
for xpath in enter_button:
    if len(enter_button) == 0:
        break
    try:
        sidebar = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/a").click()
        time.sleep(2)
        print(f"XPATH: ({xpath}) - есть")
        time.sleep(2)
        browser.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        chek = browser.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div").text
        #Проверяем что переход на страницу выбранную в каталоге произошол корректно
        if chek in chek2:
            print(f"Переход в раздел {chek} произошол корректно")
            time.sleep(2)
            home = browser.find_element(By.XPATH, "/html/body/div[2]/div[1]/header/div/div[1]/div/div[2]/div[3]/div/nav/div/div/ul/li[1]").click()
        else:
            print(f"Переход на страницу каталога не осущетвлен")
        time.sleep(2)
    except:
        print(f"XPATH: {xpath} - отсутствует на странице или в настоящее время называется по другому")
time.sleep(15)