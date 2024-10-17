from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

url = "https://demoqa.com/webtables"

driver.implicitly_wait(10)
driver.get(url)

for i in range(3):
    # delete record sebelumnya yang 3 biji itu
    delete_record_element = f"//span[@id='delete-record-{i+1}']"
    driver.find_element(By.XPATH, delete_record_element).click()

with open('nama.csv') as  csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        driver.find_element(By.ID, "addNewRecordButton").click()
        driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys(row[0])
        driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys(row[1])
        driver.find_element(By.XPATH, "//input[@id='age']").send_keys(row[2])
        driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(row[3])
        driver.find_element(By.XPATH, "//input[@id='salary']").send_keys(row[4])
        driver.find_element(By.XPATH, "//input[@id='department']").send_keys(row[5])
        driver.find_element(By.XPATH, "//button[@id='submit']").click()

