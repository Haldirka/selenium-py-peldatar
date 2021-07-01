from selenium import webdriver

PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"
URL = "http://localhost:9999"
browser = webdriver.Chrome(PATH)
all_text = []
try:
    browser.get(URL)
    all_links = browser.find_elements_by_xpath("//a")
    for i in all_links:
        all_text.append(i.sample_text)
    with open("linkek_leírva.txt", "w") as txt:
        for i in all_links:
            txt.write(i.sample_text)
            txt.write("\n")
    print(len(all_links))
except:
    print("hiba")
finally:
    browser.quit()
