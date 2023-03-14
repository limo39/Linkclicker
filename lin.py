from selenium import webdriver
from selenium.webdriver.common.by import By  
import time


driver = webdriver.Chrome()

# navigate to the page with the link
driver.get("https://aif.la/3Ir4k84")

# find the link element by its CSS selector
link = driver.find_element(By.CSS_SELECTOR, "a.link-class")

for i in range(102):
    link.click()
    # time.sleep(1)

driver.quit()

