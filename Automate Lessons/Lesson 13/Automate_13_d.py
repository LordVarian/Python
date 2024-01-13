from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 60)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

video = 'Never gonna give you up'
# Navigate to url with video being appended to search_query
driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))

# play the video
wait.until(visible((By.ID, "video-title")))
driver.find_element(By.ID, "video-title").click()

input()
