from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3669102606&distance=25&f_AL=true&f_E=1%2C2%2C3%2C4&geoId=101174742&keywords=python%20developer&refresh=true"
ACCOUNT_USERNAME = os.environ("username")
ACCOUNT_PASSWORD = os.environ("password")


chrome_driver_path = r"C:\Development\chromedriver.exe"

chrome_options = Options()  # Create a Options class, necessarly to keep open the Chrome Browser
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window() #This is just for maximize the window


driver.get(URL)
# documentation_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(documentation_link.text)

signin_button = driver.find_element(by=By.LINK_TEXT,value="Sign in") # finding the signin button and click
signin_button.click()

time.sleep(5) # wait for 5 second to load  the sign in page

input_username = driver.find_element(by=By.ID, value= "username") # type in the username and pwd and click the signin button
input_username.send_keys(ACCOUNT_USERNAME)
input_password = driver.find_element(by=By.ID,value="password")
input_password.send_keys(ACCOUNT_PASSWORD)
signin = driver.find_element(by=By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
signin.click()

time.sleep(5)

next_btn = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
next_btn.click()
#  Scroll down to the bottom of the page
next_btn.send_keys(Keys.END)

# Close messages overlay
message_overlay = driver.find_element(by=By.ID, value="ember114")
message_overlay.click()

follow_button = driver.find_element(by=By.CLASS_NAME, value="follow")
follow_button.click()


time.sleep(10)
# driver.quit()


