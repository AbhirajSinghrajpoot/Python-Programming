from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import pathlib

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

driver.find_element(By.NAME, "fName").send_keys("John")
driver.find_element(By.NAME, "lName").send_keys("Smith")
driver.find_element(By.NAME, "email").send_keys("johnsmith@example.com")
driver.find_element(By.CSS_SELECTOR, "form button").click()

input("Press Enter to close...")