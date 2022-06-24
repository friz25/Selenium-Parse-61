"""
Selenium - https://pypi.org/project/selenium/
Драйвер Chrome - https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
import time
# Указываем полный путь к geckodriver.exe на вашем ПК.
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\PythonProjects\\Selenium61\\chromedriver.exe')
driver.get("https://www.youtube.com/")
time.sleep(4)
element = driver.find_element(By.XPATH, """/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[3]/a""")
element.click()