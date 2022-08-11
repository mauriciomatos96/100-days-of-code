from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\development\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/")