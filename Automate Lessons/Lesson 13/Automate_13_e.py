from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('disable-infobars')

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.youtube.com/')

search_bar = browser.find_element(By.CLASS_NAME, 'style-scope ytd-searchbox')
searchButton = browser.find_element(By.ID, "search-icon-legacy")
search_bar.send_keys('Python learning')
searchButton.click()

input()


