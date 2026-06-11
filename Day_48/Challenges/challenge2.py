from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import pathlib

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")
# print(articles[0].text)

# for article in articles:
#     print(article.text)
    
# all_portals = driver.find_elements(By.LINK_TEXT, "Portals")
# for portal in all_portals:
#     print(portal.text)

search = driver.find_element(By.NAME, "search")
search.click()
search.send_keys("Python")
search.send_keys(Keys.ENTER)