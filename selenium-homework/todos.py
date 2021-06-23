from selenium import webdriver


PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999/todo.html"
browser = webdriver.Chrome(PATH)
try:
    browser.get(URL)

    all_todo = browser.find_elements_by_xpath('//ul//li')
    for i in all_todo:
        print(i.text)
except:
    print("hiba")
finally:
    browser.quit()
