from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(executable_path="H:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.edx.org/")
links = driver.find_elements_by_tag_name("a")
print(len(links))
for link in links:
    print(link.text)
driver.quit()

