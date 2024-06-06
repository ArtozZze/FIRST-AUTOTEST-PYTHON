import pytest
from selenium import webdriver
import allure
import time
from selenium.webdriver.common.by import By

#открываем тестируемый ресурс
@allure.step("Проверка загрузки главной страници при переходе по ссылке")
def test_homepage():
    browser = webdriver.Edge()
    browser.get("https://www.chitai-gorod.ru")
    time.sleep(10)
    xpath_home = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div[1]/div[1]/div/a[1]/div/div[1]").text
    xpath_homeCheck = "Кто здесь главный?"
    if xpath_home in xpath_homeCheck:
        print("Главная страница загрузилась корректно")
    else:
        raise Exception("Главная страница не загрузилась! Или элемента с помощью которого проводится проверка больше нет")
    time.sleep(3)
    browser.quit()
#массив с элементами для проверки ()
def get_xpath_array():
    xpath_array = []
    xpath_array.append("/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[1]")
    xpath_array.append("/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[2]")
    xpath_array.append("/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[3]")
    return xpath_array
@allure.step("Проверяем наличие в каталоге разделов и название разделов при переходе в них")
def test_katalog():
    browser = webdriver.Edge()
    browser.get("https://www.chitai-gorod.ru")
    time.sleep(10)
    browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]").click()
    time.sleep(3)
    #различные переменные необходимые для проверок
    Screenshot_path = "D:/doodle/test_screenshot/"
    chek2 = ["МАНГА", "КОМИКСЫ", "КНИГИ С АВТОГРАФАМИ АВТОРОВ"]
    enter_button = get_xpath_array()
    #цикл для проверки наличия элементов из массива в каталоге веб сайта
    for xpath in enter_button:
        if len(enter_button) == 0:
            break
        try:
            time.sleep(3)
            browser.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div/div[1]/div[1]/button").click()
            time.sleep(2)
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
                browser.save_screenshot(Screenshot_path + f"Название страници каталога({chek}).png")
                time.sleep(2)
                raise Exception(f"Переход на страницу {chek} каталога не осущетвлен")
        except:
            print(f"XPATH {xpath} нет элемента")
            browser.save_screenshot(Screenshot_path + f"Название страници каталога({chek}).png")
time.sleep(6)