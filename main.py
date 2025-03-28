from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "https://klas.kw.ac.kr/usr/cmn/login/LoginForm.do"
driver.get(url)

time.sleep(2)

id_field = driver.find_element(By.XPATH, '//*[@id="loginId"]')
id_field.send_keys(os.getenv("ID"))

password_field = driver.find_element(By.XPATH, '//*[@id="loginPwd"]')
password_field.send_keys(os.getenv("PASSWORD"))

login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/div[2]/button')
login_button.click()

time.sleep(5)

lecture_plan_url = "https://klas.kw.ac.kr/std/cps/atnlc/LectrePlanStdPage.do"
driver.get(lecture_plan_url)

time.sleep(3)

search_field = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div[2]/table[1]/tbody/tr[2]/td[1]/input')
search_field.clear()
search_field.send_keys("실험설계및분석")

search_button = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div[2]/div/button')
search_button.click()

time.sleep(3)

result_row = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div[2]/table[2]/tbody/tr')
result_row.click()

time.sleep(5)

target_element = driver.find_element(By.XPATH, '/html/body/main/div/div/div/div[2]/div[2]/table[2]/tbody/tr[2]/td')
element_text = target_element.text
print(element_text)

driver.quit()
