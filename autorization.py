from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get("https://www.twitch.tv/")
time.sleep(5)
#кнопка должнабыть не кликабельна если не вводить логин и пароль
sing_in_homePage = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button").click()
time.sleep(2)
sing_in_authPage = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[3]/div/button")
time.sleep(2)
if sing_in_authPage.is_enabled():
    print("Ошибка: Кнопка кликабельна без введенного логина и пароля")
else:
    print("Кнопка не кликабельна алгоритм работает верно")
#если ввести только логин кнопка должнабыть не кликабельна
time.sleep(2)
login = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[1]/div/div[2]/div/input").send_keys("loginTest")
time.sleep(2)
sing_in_button = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[3]/div/button")
time.sleep(2)
if sing_in_button.is_enabled():
    print("Ошибка: Кнопка кликабельна без введенного логина и пароля")
else:
     print("Кнопка не кликабельна алгоритм работает верно")
time.sleep(2)
close = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[2]/button").click()
#если ввести только пароль кнопка должнабыть не кликабельна
time.sleep(2)
sing_in_homePage = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button").click()
time.sleep(2)
password = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[2]/div/div[1]/div[2]/div[1]/div/input").send_keys("12345678")
time.sleep(2)
sing_in_button = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[3]/div/button")
time.sleep(2)
if sing_in_button.is_enabled():
    print("Ошибка: Кнопка кликабельна без введенного логина и пароля")
else:
    print("Кнопка не кликабельна алгоритм работает верно")
    time.sleep(2)
close = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[2]/button").click()
#если ввести логин и пароль кнопка должна стать кликабельной
time.sleep(2)
sing_in_homePage = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button").click()
time.sleep(2)
login = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[1]/div/div[2]/div/input").send_keys("loginTest")
time.sleep(2)
password = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[2]/div/div[1]/div[2]/div[1]/div/input").send_keys("12345678")
time.sleep(2)
sing_in_button = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[3]/div/button")
time.sleep(2)
if sing_in_button.is_enabled():
    print("Кнопка кликабельна если ввести логин и пароль алгоритм работает верно")
else:
    print("ОШИБКА Кнопка не кликабельна алгоритм работает не верно")
time.sleep(2)
#при вводе не существующих логина и пароля или при ошибке в логине или пароле выдача сообщения "Неверный пароль. Попробуйте снова.Забыли пароль?"
#а также появляется буттон "Забыли пароль?"
SingIn = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]/form/div/div[3]/div/button").click()
alert = browser.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]")
time.sleep(1)
if alert.find_elements(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[2]"):
    print("Предупреждение присутствует")
else:
    print("Предупреждение отсутствует")
time.sleep(10)