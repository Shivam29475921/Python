# importing webdriver to web-scrape
from selenium import webdriver
import time
# importing By to find elements
from selenium.webdriver.common.by import By

# importing Options to stop the webpage from closing automatically right after being opened
from selenium.webdriver.chrome.options import Options

# import Keys to send non-typeable keys to the driver
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("http://localhost/misc.php")
input1 = driver.find_element(By.XPATH, "//*[@id='1']")
input1.clear()
time.sleep(1)
input1.send_keys("Shivam Das")
input2 = driver.find_element(By.XPATH, "/html/body/form/input[2]")
input2.clear()
time.sleep(1)
input2.send_keys("Student")
time.sleep(1)
button = driver.find_element(By.TAG_NAME, "button")
button.click()
