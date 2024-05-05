from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser = webdriver.Edge()
browser.get("https://www.chitai-gorod.ru")
time.sleep(5)
search_string = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div/div[1]/div[2]/div[1]/form/input[1]").send_keys("дюна")
time.sleep(3)
button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div/div[1]/div[2]/div[1]/form/button").click()
time.sleep(3)
chek = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div[1]/div/div/div[1]/section/section/div/article[1]/div[2]/a/div/div[1]").text
chek1 = "Дюна"
if chek == chek1:
    print("Test complite")
else:
    print("Test error search not: Дюна")
time.sleep(5)
City = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]").click()
time.sleep(2)
katalog = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/header/div/div[1]/div[1]/button").click()
time.sleep(3)
razdel_kataloga = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[5]/div/div[2]/div/div[2]/div/div[2]/div[2]/a[2]").click()
time.sleep(3)
catalog_manga = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div[1]/h1").text
time.sleep(2)
catalog_chek = "МАНГА"
if catalog_manga == catalog_chek:
    print("Test complite")
else:
    print("Ошибка открылся другой раздел: Манга")
time.sleep(15)