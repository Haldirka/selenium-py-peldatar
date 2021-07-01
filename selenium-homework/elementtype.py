from selenium import webdriver


PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    first_button = browser.find_element_by_xpath("//form//button")
    first_button_text = first_button.sample_text
    first_button.click()
    after_click_label = browser.find_element_by_id("result")
    label_text = after_click_label.sample_text
    if first_button_text in label_text:
        print("Success")
except:
    print("No button element is present")
finally:
    browser.quit()