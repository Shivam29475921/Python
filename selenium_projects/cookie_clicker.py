# importing webdriver to web-scrape
from selenium import webdriver

# importing By to find elements
from selenium.webdriver.common.by import By

# importing Options to stop the webpage from closing automatically right after being opened
from selenium.webdriver.chrome.options import Options

# import Keys to send non-typeable keys to the driver
from selenium.webdriver.common.keys import Keys
import time
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker")
time.sleep(3)

lang_select = driver.find_element(By.ID, "langSelect-EN")
lang_select.click()
cookie = driver.find_element(By.ID, 'bigCookie')
timeout = time.time() + 60*0.1
print(timeout, time.time())
while True:
    cookie.click()
    



