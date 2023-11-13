from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from zipfile import ZipFile
from core.pixCore import *


binary_location = 'C:/Users/TLibres/pix_automation/chromedriver/chromedriver.exe'
driver_location = 'C:/Users/TLibres/pix_automation/chromedriver/chromedriver.exe'
conn = http.client.HTTPSConnection("api.zephyrscale.smartbear.com")

aws_name = os.environ.get('AWS_NAME')
aws_pass = os.environ.get('AWS_PASS')

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")

browser = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
browser.maximize_window()

line_count = [0]

temp_val = []
status_synced = []
step_result = []
testcycle = []
temp_logfile = []
prev_line_count = []
prev_log_file = []