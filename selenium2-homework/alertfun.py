import time

from selenium import webdriver
from selenium.webdriver import ActionChains

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/alert_playground.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    alert_button = browser.find_element_by_xpath('//input[@name="alert"]')
    box_button = browser.find_element_by_xpath('//input[@name="confirmation"]')
    prompt_button = browser.find_element_by_xpath('//input[@name="prompt"]')
    double_click_button = browser.find_element_by_id("double-click")
    text_p = browser.find_element_by_id("demo")
    sample_text = "This is a text"

    alert_button.click()
    switch_to_alert = browser.switch_to.alert
    switch_to_alert.accept()

    box_button.click()
    switch_to_alert.dismiss()

    prompt_button.click()
    switch_to_alert.send_keys(sample_text)
    switch_to_alert.accept()

    assert (text_p.text == "You entered: " + sample_text)

    action = ActionChains(browser)
    action.double_click(double_click_button).perform()
    switch_to_alert.accept()
except:
    print("something went wrong :(")
finally:
    browser.quit()
