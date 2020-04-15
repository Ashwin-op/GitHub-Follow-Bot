import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initializing the headless chrome
driver = webdriver.Chrome()
driver.get("https://github.com/login")
wait = WebDriverWait(driver, 10)

# Locating username and password field
username = wait.until(EC.presence_of_element_located((By.ID, "login_field")))
password = wait.until(EC.presence_of_element_located((By.ID, "password")))

# password and username need to go into these values
username.send_keys("username")
password.send_keys("password")

# Clicking the sign in button
login_form = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@value='Sign in']")))
login_form.click()

# Go to the followers tab
nameOfUser = "" # Input github username here

driver.get("https://github.com/{}?tab=followers".format(nameOfUser))
time.sleep(3)

# Find the followers
users = driver.find_elements_by_xpath("//a[@data-hovercard-type='user']")
temp = []
for follower in users:
    temp.append(follower.get_attribute("href"))
list_set = set(temp) 
followers = (list(list_set))

# Follow everyone who is following 'nameOfUser'
for user in followers:
    for page in range(1, 5):
        string = "{}?page={}&tab=following".format(user, page)
        driver.get(string)
        time.sleep(3)

        follow_button = driver.find_elements_by_xpath("//input[@aria-label='Follow this person']")

        try:
            for i in follow_button:
                i.submit()
        except:
            pass

driver.close()
