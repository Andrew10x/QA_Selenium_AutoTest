from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from webdriver_manager.firefox import GeckoDriverManager

#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser = webdriver.Firefox(executable_path="D:\\svtan\\Documents 2\\QA\\firefoxdriver\\\geckodriver.exe")

browser.get("https://repka.ua/")
browser.implicitly_wait(10)

browser.find_element_by_css_selector('.yes-btn').click()

search = browser.find_element_by_id("search")
search.clear()
search.send_keys("SSD 500Gb")
time.sleep(3)
search.send_keys(Keys.ENTER)
actual = browser.find_element_by_css_selector('.base').text
expected1 = "SSD накопители"
expected2 = "SSD накопичувачі"
assert actual == expected1 or actual == expected2
time.sleep(4)
browser.save_screenshot("SSD.png")
browser.close()
browser.quit()
