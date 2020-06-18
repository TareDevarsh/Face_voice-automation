from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def web_test(text):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option("detach", True)
    join_var = ' '
    def chrome_init(website):
        driver = webdriver.Chrome('/home/dev/Desktop/face_voice_automation/face_voice/bin/chromedriver', options = chrome_options)    
        driver.get(website)
        driver.maximize_window()
        sleep(2)
        return driver

    if text[0] == 'search':
        driver = chrome_init('http://www.google.com/')
        actions = ActionChains(driver)
        actions.send_keys(join_var.join(text[2:])).perform()
        webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()

    elif text[0] == 'play':
        join_var = '+'
        
        driver = chrome_init('https://www.youtube.com/results?search_query='+ join_var.join(text[1:]))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[(@id='video-title')]"))).click()

    elif join_var.join(text) == 'f*** you':
        print("FUCK YOU TOO")
    elif text[0] == 'UnknownValueError':
        pass

    else :
        print("No can do")


def google_search():
    pass
    