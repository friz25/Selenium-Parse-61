"""
Selenium - https://pypi.org/project/selenium/
Драйвер Chrome - https://chromedriver.chromium.org/downloads
"""
from selenium import webdriver
import time
# Указываем полный путь к geckodriver.exe на вашем ПК.
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class SileniumTest:
    options = Options()

    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.youtube.com/")
    print("Браузер запущен. Вход выполнен!")
    # time.sleep(4)
    # element = driver.find_element(By.XPATH, """/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[3]/a""")
    # element.click()

    """Поиск канала на YouTube"""
    time.sleep(1)
    search_bar = driver.find_element(By.XPATH, """//input[@id="search"]""")
    search_bar.send_keys("Гоблин")
    # print("search_bar.send_keys('Гоблин')")
    search_button = driver.find_element(By.XPATH, """/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button""")
    search_button.click()
    # print("search_button.click()")

    """Поиск (названий) первых 10ти видео"""
    time.sleep(1)
    videos = driver.find_elements(By.ID, """title-wrapper""")
    print("")
    for i in range(len(videos)):
        print(videos[i].text)
        if i == 10:
            break
    """Выведем ссылку на первое видео"""
    print("")
    # print(videos[0].get_attribute('href'))

if __name__ == '__main__':
    SileniumTest()