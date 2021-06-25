import time
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/general.html"
browser = webdriver.Chrome(PATH)

browser.get(URL)

all_links = browser.find_elements_by_xpath('//a')

for i in all_links:
    link_href = i.get_attribute("href")
    i.click()
    saved_url = browser.current_url
    try:
        if link_href == saved_url:
            time.sleep(1)
            browser.back()
    except:
        print(" ")
        # browser.back()
        # browser.switch_to_window(browser.window_handles[-1])
