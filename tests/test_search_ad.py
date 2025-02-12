import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get('http://tech-avito-intern.jumpingcrab.com/')
    yield driver
    driver.quit()

def test_search_ad(driver):
    search_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/input')
    search_query = "тестовое объявление 1"
    search_input.send_keys(search_query)

    search_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/button')
    search_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div[1]/a/div/div/div[1]/h4')))

    ads_titles = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[2]/div[5]/div/a/div/div/div[1]/h4')

    # **Объявляем переменную search_words**
    search_words = search_query.lower().split()