# импортируем модули и отдельные классы
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# каждый тест должен начинаться с test_
def test_product_view_sku(browser):
    """
    Test case WERT-1
    """
    url = "https://test.qa.studio"
    browser.get(url=url)
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = browser.find_element(By.XPATH, value=x_path_table)
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = browser.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"
    
def test_new_products(browser):
  url =     url = "https://test.qa.studio"
  browser.get(url=url)
  element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-new ']")
  element.click()
  x_path_table = '//*[@id="rz-shop-content"]/ul/li[4]/div/div[2]/h2/a'
  element = browser.find_element(By.XPATH, value=x_path_table)
  element.click()
  sku = browser.find_element(By.CLASS_NAME, value="sku")
  assert sku.text == 'BFB9ZOK210', "Unexpected sku"
