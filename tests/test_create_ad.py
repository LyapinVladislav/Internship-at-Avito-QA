from selenium.webdriver.common.by import By

def test_create_ad(driver):
    # Перейти на страницу создания объявления
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button[3]').click()

    # Заполнить поля
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[2]/input').send_keys("Заголовок объявления")
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[3]/input').send_keys("1000")  # Цена
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[4]/input').send_keys("Описание объявления")
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[5]/input').send_keys("https://avatars.mds.yandex.net/i?id=3c3067fd6e31b3d1000fe88a76c03494cea6809d-8819379-images-thumbs&n=13")

    # Нажать кнопку "Сохранить"
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/button[2]').click()

    # Проверка, что объявление добавлено
    ad_title = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[2]/input').get_attribute('value')
    ad_price = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[3]/input').get_attribute('value')
    ad_description = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/div[4]/input').get_attribute('value')

    assert ad_title == "Заголовок объявления"
    assert ad_price == "1000"
    assert ad_description == "Описание объявления"