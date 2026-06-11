from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException
)
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
PHONE = os.getenv("LINKEDIN_PHONE")


driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

input("LinkedIn page opened. Press Enter after inspection...")

time.sleep(2)
sign_in_button = driver.find_element(
    By.LINK_TEXT,
    "Sign in"
)
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(
    By.XPATH,
    '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div[2]/button[1]'
)

email_field.click()
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(
    By.CSS_SELECTOR,
    ".job-card-container--clickable"
)

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.NAME, "fb-single-line-text__input")
        if phone.get_attribute("value") == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.NAME, "artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_buttons = driver.find_elements(
                By.NAME,
                "artdeco-modal__confirm-dialog-btn"
            )

            discard_button = discard_buttons[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.NAME, "artdeco-modal__dismiss")
        close_button.click()

    except (NoSuchElementException, ElementClickInterceptedException):
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()