from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5) 

try:
    driver.get('https://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    assert '/inventory.html' in driver.current_url

    titulo = driver.find_element(By.CSS_SELECTOR,
        'div.header_secondary_container .title').text

    assert titulo == 'Products'
    print('Título de sección OK →', titulo)

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print(f'Se encontraron {len(productos)} productos.')

    productos[0].find_element(By.TAG_NAME, 'button').click()

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == '1'
    print('Carrito OK →', badge)
    print('TEST OK')

except Exception as e:
    print('TEST FALLÓ', str(e))
finally:

    driver.quit()