from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#открываем тестируемый ресурс
browser = webdriver.Edge()
browser.get("https://www.chitai-gorod.ru")
time.sleep(5)
City = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]").click()
time.sleep(3)
#массив с элементами для проверки
def get_xpath_array():
    xpath_array = []
    xpath_array.append("/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[1]")
    xpath_array.append("/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[2]")
    xpath_array.append("/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[3]")
    return xpath_array
#различные переменные необходимые для проверок
chek2 = ["МАНГА", "КОМИКСЫ", "КНИГИ С АВТОГРАФАМИ АВТОРОВ"]
enter_button = get_xpath_array()
#цикл для проверки наличия элементов из массива в каталоге веб сайта
for xpath in enter_button:
    if len(enter_button) == 0:
        break
    try:
        time.sleep(3)
        katalog = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div/div[1]/div[1]/button").click()
        time.sleep(2)
        element = browser.find_element(By.XPATH, xpath)
        print(f"XPATH {xpath} есть")
        time.sleep(3)
        # действие с элементом, например, открыть его
        browser.find_element(By.XPATH, xpath).click()
        time.sleep(2)
        chek = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div[1]/h1").text
        if chek in chek2:
            print(f"Переход в {chek} произошол корректно")
        else:
            print(f"Переход на страницу каталога не осущетвлен")
        time.sleep(2)
    except:
        print(f"XPATH {xpath} нет элемента")
time.sleep(15)