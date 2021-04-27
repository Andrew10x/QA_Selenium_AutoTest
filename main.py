from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path="C:\\Users\\38063\\PycharmProjects\\QA\\firefoxdriver\\geckodriver.exe")
browser.get("https://repka.ua/")
browser.implicitly_wait(10)
try:
    browser.find_element_by_class_name('yes-btn').click()
finally:
    search = browser.find_element_by_id("search")
    search.clear()
    search.send_keys("SSD 500Gb")
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    actual = browser.find_element_by_css_selector('.base').text
    expected = "SSD накопители"
    assert actual == expected
    time.sleep(4)
    browser.save_screenshot("SSD.png")
    browser.close()
    browser.quit()
