from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")


price = driver.find_element(By.ID, "priceblock_ourprice")
print(price.text)

search_bar = driver.find_element(By.NAME, "q")
print(search_bar.tag_name)

bug_link = driver.find_element(
    By.XPATH,
    '//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
)
print(bug_link.text)

css_link = driver.find_element(By.CSS_SELECTOR, "css")
print(css_link.text)

driver.quit()