# -------------------------BOILERPLATE--------------------------- #

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# ------------------------------------------------------------- #

# driver.find_element(By.CSS_SELECTOR, "input[value = 'radio2']").click()
# driver.find_element(By.ID, "checkBoxOption1").click()

# fieldset = driver.find_elements(By.TAG_NAME, "fieldset")
# for each_fieldset in fieldset:
#     print(each_fieldset.text)


# driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Shivam Das")

# driver.quit()
