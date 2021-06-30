import time

from selenium import webdriver

URL = "https://webshop.progmasters.hu/"
PATH = "C:\\Users\Zsolt\Desktop\webdriver\chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.get(URL)
browser.maximize_window()
login_btn = browser.find_element_by_id("login")
login_btn.click()
email_input = browser.find_element_by_id("email")
password_input = browser.find_element_by_id("password")
submit_btn = browser.find_element_by_css_selector('button[type="submit"]')

email_input.send_keys("admin1@gmail.com")
password_input.send_keys("admin1")
submit_btn.click()
time.sleep(2)
product = browser.find_element_by_id("new-product-link")
product.click()
name_field = browser.find_element_by_id("from")
name_field.send_keys("Banoffee pie")
price = browser.find_element_by_id("price")
price.send_keys(4)
picture = browser.find_element_by_id("url")
picture.send_keys("https://www.browneyedbaker.com/wp-content/uploads/2020/09/banoffee-pie-3-square-500x500.jpg%22")
text_area = browser.find_element_by_id("description")
text_area.send_keys("Banoffee Pie is a classic English dessert that gets its name from the \n"
                    "ingredients used banana and toffee! It's absolutely delicious and totally \n"
                    "addicting made with a Graham cracker crust and filled with bananas, \n"
                    "dulce de leche (toffee), and a generous helping of whipped cream.")
category = browser.find_element_by_id("catId")