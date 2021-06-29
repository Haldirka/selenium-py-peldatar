import csv
from selenium import webdriver


PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://www.rpachallenge.com/"
browser = webdriver.Chrome(PATH)

challenge_data_list = []
with open("challenge.csv", newline='') as challenge_data:
    next(challenge_data)
    challenge_data_read = csv.reader(challenge_data, delimiter=";")
    data = list(challenge_data_read)

browser.get(URL)
browser.maximize_window()
start_button = browser.find_element_by_xpath('//button')
start_button.click()
for i in data:
    first_name_input = browser.find_element_by_xpath('//div//label[text()="First Name"]//..//input')
    email_input = browser.find_element_by_xpath('//div//label[text()="Email"]//..//input')
    role_in_company_input = browser.find_element_by_xpath('//div//label[text()="Role in Company"]//..//input')
    company_name_input = browser.find_element_by_xpath('//div//label[text()="Company Name"]//..//input')
    address_input = browser.find_element_by_xpath('//div//label[text()="Address"]//..//input')
    last_name_input = browser.find_element_by_xpath('//div//label[text()="Last Name"]//..//input')
    phone_number_input = browser.find_element_by_xpath('//div//label[text()="Phone Number"]//..//input')
    submit_button = browser.find_element_by_xpath('//input[@type="submit"]')

    first_name = (i[0])
    first_name_input.send_keys(first_name)
    last_name = (i[1])
    last_name_input.send_keys(last_name)
    company_name = (i[2])
    company_name_input.send_keys(company_name)
    role_in_company = (i[3])
    role_in_company_input.send_keys(role_in_company)
    address = (i[4])
    address_input.send_keys(address)
    email = (i[5])
    email_input.send_keys(email)
    phone_number = (i[6])
    phone_number_input.send_keys(phone_number)
    submit_button.click()
