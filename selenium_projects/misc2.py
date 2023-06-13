# -----------------------BOILERPLATE--------------------------- #

# importing webdriver to web-scrape
from selenium import webdriver

# importing By to find elements
from selenium.webdriver.common.by import By

# importing Options to stop the webpage from closing automatically right after being opened
from selenium.webdriver.chrome.options import Options

# import Keys to send non-typeable keys to the driver
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# ---------------------------------------------------------- #


no_of_articles = driver.find_element(By.XPATH, "//*[@id='articlecount']/a[1]")
# print(no_of_articles.text)
# no_of_articles.click()

search_bar = driver.find_element(By.XPATH, "//*[@id='searchInput']")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)