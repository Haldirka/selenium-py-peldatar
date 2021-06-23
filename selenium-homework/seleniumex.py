from selenium import webdriver


PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "https://index.hu/"

browser = webdriver.Chrome(PATH)
browser.get(URL)

def id_finder(given_id):
    nemletezo_div = browser.find_element_by_xpath("//div[@id ='" + given_id +"' ]")
    return nemletezo_div

try:
    id_finder("nemletezo")
    print("van ilyen div")
except:
    print("Hiba")
finally:
    browser.quit()
