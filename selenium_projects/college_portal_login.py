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

driver.get("https://cmsys.bangabasi.ac.in/ocms/index.php")
data_of_birth = driver.find_element(By.XPATH, "//*[@id='field_2']")
data_of_birth.send_keys("16/12/2002")

mobile_number = driver.find_element(By.XPATH, "//*[@id='field_7']")
mobile_number.send_keys("9038246179")

login_btn = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/p[1]/button")
login_btn.click()
