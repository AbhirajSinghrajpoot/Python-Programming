from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import pathlib

driver = webdriver.Chrome()
driver.get("https://www.python.org/")


event_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text
    }

with open(pathlib.Path("events.json"), "w") as file:
    json_events = json.dumps(events, indent=4)
    file.write(json_events)

print(json_events)

driver.quit()