import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEditAd(unittest.TestCase):
    def setUp(self):
        # Настроим драйвер
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://tech-avito-intern.jumpingcrab.com/advertisements/5")
        self.driver.maximize_window()

    def test_edit_ad(self):
        # Ожидаем, что загрузится следующее состояние страницы
        self.driver.implicitly_wait(10)

        # Пример редактирования — добавить логику изменения и сохранения объявления

    def tearDown(self):
        # Закрываем браузер после теста
        self.driver.quit()