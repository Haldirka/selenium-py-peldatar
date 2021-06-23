from selenium import webdriver


PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    get_objects_by_id = browser.find_elements_by_id("bmwcheck")
    get_objects_by_name = browser.find_elements_by_name("cars")
    get_objects_by_xpath = browser.find_elements_by_xpath('//input[@class="btn btn-secondary"]')

    for i in get_objects_by_xpath:
        print((i).get_attribute("class"))
except:
    print("Hiba")
finally:
    browser.quit()