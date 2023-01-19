from django.conf import settings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/admin")


def test_login(test_driver) -> None:
    login_element = test_driver.find_element(By.ID, "id_username")
    login_element.send_keys(settings.TEST_USER_NAME)

    password_element = test_driver.find_element(By.ID, "id_password")
    password_element.send_keys(settings.TEST_USER_PASSWORD)
    password_element.send_keys(Keys.RETURN)


test_login(driver)

driver.get("http://127.0.0.1:8000/admin/core/country/add")
country_element = driver.find_element(By.ID, "id_name")
country_element.send_keys("Япония")
country_element.send_keys(Keys.RETURN)

