from selenium import webdriver

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/editable-table.html"
browser = webdriver.Chrome(PATH)

browser.get(URL)
browser.maximize_window()

button = browser.find_element_by_xpath('//button')
row_count = len(browser.find_elements_by_xpath('//tbody//tr'))

for i in range(2):
    button.click()
    last_row = browser.find_elements_by_xpath('//tbody//tr[last()]//td//input')
    for k in last_row:
        k.send_keys("iajfad")
row_count2 = len(browser.find_elements_by_xpath('//tbody//tr'))

if row_count2 > row_count:
    print("sikeres hozzáadás")


### clear() után törlődnek a sorok valamiért, a kód többi része nem fut le
# search_field = browser.find_element_by_xpath('//div//input[@placeholder="Search..."]')
# search_field.clear()
# search_field.send_keys("football")
# search_field.clear()


update_field = browser.find_elements_by_xpath('//tbody//tr//td//input')
update_field[0].clear()
update_field[0].send_keys("football2")
if update_field[0].text == update_field[0].get_attribute("value"):
    print("sikeres DOM struktúra frissítés")
else:
    print("sikertelen DOM struktúra frissítés")
browser.quit()
