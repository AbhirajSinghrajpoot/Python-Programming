from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:

        money = driver.find_element(By.ID, "money").text

        if money == "":
            money = 0
        else:
            money = int(money.replace(",", ""))

        store_items = driver.find_elements(By.CSS_SELECTOR, "#store b")

        prices = []

        for item in store_items:
            text = item.text

            if "-" in text:
                price = int(
                    text.split("-")[1]
                    .strip()
                    .replace(",", "")
                )
                prices.append(price)

        affordable = {}

        for n in range(len(prices)):
            if prices[n] <= money:
                affordable[prices[n]] = n

        if affordable:
            highest_price = max(affordable)
            item_to_buy = affordable[highest_price]

            store_items[item_to_buy].click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)
        break

driver.quit()