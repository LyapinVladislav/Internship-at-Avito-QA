import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    # Инициализация драйвера для Selenium
    driver = webdriver.Chrome()  # Или любой другой драйвер (Firefox, Edge и т.д.)
    driver.get("http://tech-avito-intern.jumpingcrab.com/")
    yield driver
    driver.quit()