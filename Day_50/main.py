from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException
)
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

FACEBOOK_EMAIL = 'thiago@gmail.com'
FACEBOOK_PASSWORD = 'thiago@123'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")
sleep(3)  


botao_login = driver.find_element(By.XPATH, '//button[contains(text(), "Log in")]')
botao_login.click()
sleep(2)


facebook_login = driver.find_element(By.XPATH, '//button[contains(text(), "Continue with Facebook")]')
facebook_login.click()
sleep(3)

base_window = driver.window_handles[0]
facebook_login_window = driver.window_handles[1]
driver.switch_to.window(facebook_login_window)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
senha = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FACEBOOK_EMAIL)
senha.send_keys(FACEBOOK_PASSWORD)
senha.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

try:
    permitir_localizacao_botao = driver.find_element(By.XPATH, '//button[contains(text(), "Allow")]')
    permitir_localizacao_botao.click()
    sleep(1)
except NoSuchElementException:
    print("Location popup nahi aaya, skip...")


try:
    notificacao_botao = driver.find_element(By.XPATH, '//button[contains(text(), "Not interested")]')
    notificacao_botao.click()
    sleep(1)
except NoSuchElementException:
    print("Notification popup nahi aaya, skip...")


try:
    cookies = driver.find_element(By.XPATH, '//button[contains(text(), "Accept")]')
    cookies.click()
    sleep(1)
except NoSuchElementException:
    print("Cookie popup nahi aaya, skip...")


for n in range(100):
    sleep(1)
    try:
        print(f"Like #{n+1}")
        like_button = driver.find_element(
            By.XPATH,
            '//button[@aria-label="Like"]' 
        )
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        print("Like button nahi mila, skip...")
        sleep(2)

driver.quit()