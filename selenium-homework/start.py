from selenium import webdriver

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "https://www.youtube.com/"

browser = webdriver.Chrome(PATH)
browser.get(URL)

browser.quit()