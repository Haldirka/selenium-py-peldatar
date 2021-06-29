import csv
from selenium import webdriver


PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://www.rpachallenge.com/"
browser = webdriver.Chrome(PATH)


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

    first_name_input.send_keys(i[0])
    last_name_input.send_keys(i[1])
    company_name_input.send_keys(i[2])
    role_in_company_input.send_keys(i[3])
    address_input.send_keys(i[4])
    email_input.send_keys(i[5])
    phone_number_input.send_keys(i[6])
    submit_button.click()
