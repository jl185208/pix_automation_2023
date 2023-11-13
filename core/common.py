from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from zipfile import ZipFile
from core.pixCore import *
from core.variables import *
from core.page import *
from core.elements import *
import os
import http.client
import pyotp

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

def create_testcycle_func_test(payloads):
    conn = http.client.HTTPSConnection("api.zephyrscale.smartbear.com")
    payload = payloads
    headers = {
    'Content-Type': "application/json",
    'Authorization': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczovL2Nsb3VkY29uZmx1ZW5jZXBvc3Rlbm5vcmdlLmF0bGFzc2lhbi5uZXQiLCJ1c2VyIjp7ImFjY291bnRJZCI6IjYxYTg4ZWI0MjI3OGU3MDA2YjMxZWViOCJ9fSwiaXNzIjoiY29tLmthbm9haC50ZXN0LW1hbmFnZXIiLCJzdWIiOiI1MzQ0YjRjOC1mNTljLTM5MmEtYjA0NC0yMzM0MTA4MjcwYjciLCJleHAiOjE3MTAzOTQxMjYsImlhdCI6MTY3ODg1ODEyNn0.eZwOSh0ijFrvRMOvP8ztPTui1q2D6BiaE-QxDq-s11Y"
    }
    conn.request("POST", "/v2/testcycles", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = data.decode("utf-8")
    testcycle_key_data = json.loads(response)
    testcycle_key_inside = testcycle_key_data['key']
    logging.info('Testcycle # : ' + str(testcycle_key_inside))
    return testcycle_key_inside

def add_exe_testcases(key, payloads, result):
    conn = http.client.HTTPSConnection("api.zephyrscale.smartbear.com")
    payload = payloads
    headers = {
        'Content-Type': "application/json",
        'Authorization': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczovL2Nsb3VkY29uZmx1ZW5jZXBvc3Rlbm5vcmdlLmF0bGFzc2lhbi5uZXQiLCJ1c2VyIjp7ImFjY291bnRJZCI6IjYxYTg4ZWI0MjI3OGU3MDA2YjMxZWViOCJ9fSwiaXNzIjoiY29tLmthbm9haC50ZXN0LW1hbmFnZXIiLCJzdWIiOiI1MzQ0YjRjOC1mNTljLTM5MmEtYjA0NC0yMzM0MTA4MjcwYjciLCJleHAiOjE3MTAzOTQxMjYsImlhdCI6MTY3ODg1ODEyNn0.eZwOSh0ijFrvRMOvP8ztPTui1q2D6BiaE-QxDq-s11Y"
        }
    conn.request("POST", "/v2/testexecutions", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

def start_log_line(scenario):
    logging.info("<b>Starting Automation for Scenario :</b> " + str(scenario).strip('<Scenario ">"'))
   

def get_aws_code():
    totp = pyotp.TOTP("YGDO5GRUKCAITO7WVXBW7ICIEEF5ZG5G")
    awscode = totp.now()
    return awscode

def clear_log():
    pass
    # clear the text file for new logs
    #with open('logs/' + ID + '/logs/bdd-actual-' + ID + '.log','r+') as file:
    #    file.truncate()

def create_notif_dynamodb():
    try:
        aws_link = 'https://d-9367049c0e.awsapps.com/start#/'
        browser.get(aws_link)
        logging.info('Accessed website : ' + aws_link)
        time.sleep(15)
        # user element
        username = browser.find_element('id', 'awsui-input-0')
        # send user
        username.send_keys(aws_name)
        logging.info('Send user ' + aws_name)
        # click next
        next_xpath = "//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']"
        browser.find_element('xpath', next_xpath).click()
        logging.info("Click NEXT button with XPATH : " + next_xpath)
        time.sleep(2)
        logging.info("Sleep 2 seconds to load.")
        # password element
        password = browser.find_element('id', 'awsui-input-1')
        # send password
        password.send_keys(aws_pass)
        # click next
        logging.info("Inputted Password and Clicked Nex button.")
        browser.find_element('xpath', '//button[@class="awsui-button awsui-button-variant-primary awsui-hover-child-icons"]').click()
        # code element
        time.sleep(3)
        code = browser.find_element('id', 'awsui-input-2')
        # send code
        awscode = get_aws_code()
        code.send_keys(awscode)
        logging.info("Acquired 2FA OTP from AWS : " + awscode)
        # click SIGN IN 
        sign_in_xpath = "//button[@class='awsui-button awsui-button-variant-primary awsui-hover-child-icons']"
        browser.find_element('xpath', sign_in_xpath).click()
        time.sleep(10)
        logging.info("Sleep for 8 seconds to load the page.")
        # click aws accounts
        browser.find_element(By.XPATH, '/html/body/app/portal-ui/div/div/div[1]/centered-content/portal-dashboard/div/portal-application-list/portal-application').click()
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[1])
        # click api-wrapper-dev
        browser.find_element(By.XPATH, '/html/body/app/portal-ui/div/div/div[1]/centered-content/portal-dashboard/div/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/div/div').click()
        time.sleep(2)
        # click Manage Console
        browser.find_element(By.XPATH, '/html/body/app/portal-ui/div/div/div[1]/centered-content/portal-dashboard/div/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/a').click()
        browser.close()
        browser.switch_to.window(browser.window_handles[1])
        time.sleep(20)
        # click View all services
        #browser.find_element(By.XPATH, "//*[contains(text(),'View all services')]").click()
        time.sleep(3)
        # access dynamodb
        browser.get('https://eu-north-1.console.aws.amazon.com/dynamodbv2/home?region=eu-north-1#item-explorer?table=UserNotifications')
        time.sleep(12)
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/label/span/span/span[1]/input').click()
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/button').click()
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div/ul/li[2]/span').click()
        # click JSON view
        time.sleep(3)
        #browser.find_element(By.XPATH, '<button class="awsui_segment_8cbea_1vn1n_97 awsui_selected_8cbea_1vn1n_174" type="button" tabindex="0" aria-pressed="true" data-awsui-focus-visible="true"><span>JSON view</span></button>')
        # input data
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/div/div/div/span/textarea').clear()
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/div/div/div/div/span/textarea').send_keys(str(ID))
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/div/div[2]/div/div/div/div/span/textarea').clear()
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/div/div[2]/div/div/div/div/span/textarea').send_keys("This is a sample description generated by pix_automation")
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/div/div[2]/div/div/div/div/span/textarea').clear()
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/div/div[2]/div/div/div/div/span/textarea').click()
        actions = ActionChains(browser) # focus the browser since its not detected
        actions.send_keys("AU").perform()
        #browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[4]/td[2]/div/div[2]/div/div/div/div/span/textarea').send_keys("RCP" + str(ID))
        time.sleep(1)
        # click create button 
        time.sleep(1)
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/div/div/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/div/div[2]/div/div/div/div/span/textarea').click()
        time.sleep(2)
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/footer/div/div/div/div[2]').click()
        browser.get_screenshot_as_file('logs/px5-aws-fired notif.png')
        step_result.clear()
        step_result.append('Pass')
        time.sleep(10)
        browser.switch_to.window(browser.window_handles[0])

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        step_result.clear()
        step_result.append('Fail')
        return False