from core.pixCore import *
from core.variables import *
from core.page import *
from core.elements import *
from core.db import *
from core.common import *
import time

loggings()

@step('settings page is accessed')
def step_impl(context):
    start_log_line(context.scenario)
    # Acccess the settings page
    browser.get(settings_page)
    logging.info('Accessed site : ' + str(settings_page))
    time.sleep(3)
    version = browser.find_element(By.XPATH, xpath_page_ver).text
    logging.info('Version : ' + str(version))
    temp_val.clear()
    temp_val.append(version)
    

@step('welcome message is displayed')
def step_impl(context):
    if str('Welcome!') in str(temp_val[0]):
        step_result.clear()
        step_result.append('Pass')
        logging.info('Welcome message is displayed, website text : ' + str(temp_val[0]))
        pass
    else:
        step_result.clear()
        step_result.append('Fail')
        logging.info('Version is not correct!')
        logging.info(temp_val[0])
        assert False

@step('user can fire notification')
def step_impl(context):
    fire_button = browser.find_element(By.XPATH, xpath_fire_button).text
    logging.info('Button : ' + str(fire_button))
    if fire_button == 'Fire notification!':
        pass

@step('fire notification button is clicked')
def step_impl(context):
    browser.find_element(By.XPATH, xpath_fire_button).click()
    time.sleep(1)
    logging.info('Button is clicked to fire notification.')
    pass

@step('{notif} is displayed')
def step_impl(context, notif):
    actual_notif = browser.find_element(By.XPATH, xpath_notif).text
    if str(actual_notif) == str(notif):
        logging.info('Popped notification : ' + str(actual_notif))
        browser.get_screenshot_as_file('logs/px1-display-notif.png')
        step_result.clear()
        step_result.append('Pass')
        pass
    else:
        logging.info('Notifications not correctly displayed!')
        step_result.clear()
        step_result.append('Fail')
        assert False


@step('creates a {cycle_name} testcycle in zephyr')
def step_impl(context, cycle_name):
    payload_px1 = "{\n  \"projectKey\": \"OCS\",\n  \"name\": \"Pixel Functional Test\",\n  \"description\": \"\",\n  \"plannedStartDate\": \"2023-03-15T13:15:13Z\",\n  \"plannedEndDate\": \"2023-03-20T13:15:13Z\",\n  \"jiraProjectVersion\": 10000,\n  \"statusName\": \"Not Executed\",\n  \"folderId\": 7958926,\n  \"ownerId\": \"61a88eb42278e7006b31eeb8\",\n  \"customFields\": {}\n}"
    testcycle_key = create_testcycle_func_test(payload_px1)
    testcycle.clear()
    testcycle.append(testcycle_key)

@step('updates test results for {key}')
def step_impl(context, key):
    try:
        # count readlines in files
        with open('logs/' + ID + '/logs/bdd-actual-' + ID + '.log', 'r+') as file:
            for i, l in enumerate(file):
                pass
        prev_line_count.clear()
        prev_line_count.append(line_count[0])
        #logging.info('Previous line count # is : ' + str(prev_line_count[0]))
        lines =  i + 1
        #logging.info('Number of lines in Scenario: ' + str(lines))
        line_count.clear()
        line_count.append(lines)
        result = step_result[0]
        # get the row lines of each scenario and print
        with open('logs/' + ID + '/logs/bdd-actual-' + ID + '.log', 'r+') as file:
            #data = file.read().replace('\n', '<br>')
            myline = file.readlines()
            data = myline[int(prev_line_count[0]):]
        payload_tc_px1 = "{\n  \"projectKey\": \"OCS\",\n  \"testCaseKey\": \"" + key + "\",\n  \"testCycleKey\": \"" + testcycle[0] + "\",\n  \"statusName\": \"" + result + "\",\n  \"testScriptResults\": [\n    {\n      \"statusName\": \"" + result + "\",\n      \"actualEndDate\": \"2023-03-16T13:15:13Z\",\n      \"actualResult\": \"<b>Test Results :</b> " + str(data) + "  <br> <b>Screenshot :</b> TBD <br> <img src='archived-notif.png'>\"\n    }\n  ],\n  \"actualEndDate\": \"2023-03-16T13:15:13Z\",\n  \"executionTime\": 120000,\n  \"executedById\": \"61a88eb42278e7006b31eeb8\",\n  \"assignedToId\": \"61a88eb42278e7006b31eeb8\",\n  \"comment\": \"Pixel Automation\",\n  \"customFields\": {\n\n  }\n}"
        
        add_exe_testcases(key, payload_tc_px1, step_result[0])
        
    except Exception as e:
        logging.info(e)
        