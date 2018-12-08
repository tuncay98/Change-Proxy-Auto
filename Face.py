from selenium import webdriver
import random
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait

file2 = open("prx.txt", "r")
Numbers = file2.read().splitlines()
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
path = "C:\chromedriver.exe"

proxy = random.choice(Numbers)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy)
browser = webdriver.Chrome(path, chrome_options=chrome_options, desired_capabilities=capa)
browser.delete_all_cookies()
wait = WebDriverWait(path, 20)
browser.get("https://www.google.com.tr")
