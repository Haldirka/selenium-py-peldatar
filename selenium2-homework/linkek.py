from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999"
browser = webdriver.Chrome(PATH)
try:
    browser.get(URL)
    all_links = browser.find_elements_by_xpath("//a")
    with open("linkek_leírva.txt", "w") as txt:
        for i in all_links:
            txt.write(i.text)
            txt.write("\n")
except:
    print("hiba")
finally:
    print(len(all_links))
    browser.quit()
