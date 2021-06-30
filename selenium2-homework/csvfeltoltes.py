import csv
from selenium import webdriver

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/another_form.html"
browser = webdriver.Chrome(PATH)

browser.get(URL)

with open("table_in.csv", "r", encoding="utf-8") as data:
    next(data)
    reader_data = csv.reader(data)
    reader_data_list = list(reader_data)
    print(reader_data_list)

for i in reader_data_list:
    browser.find_element_by_id("fullname").clear()
    browser.find_element_by_id("fullname").send_keys(i[0].strip())
    browser.find_element_by_id("email").clear()
    browser.find_element_by_id("email").send_keys(i[1].strip())
    browser.find_element_by_id("dob").clear()
    browser.find_element_by_id("dob").send_keys(i[2].strip())
    browser.find_element_by_id("phone").clear()
    browser.find_element_by_id("phone").send_keys(i[3].strip())
    browser.find_element_by_id("submit").click()

