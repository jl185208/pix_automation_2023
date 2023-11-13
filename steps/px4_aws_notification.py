from core.pixCore import *
from core.variables import *
from core.page import *
from core.elements import *
from core.db import *
from core.common import *
import time


@step('pwa is accessed')
def step_impl(context):
    browser.get('https://main.d3n66fgxolf0qz.amplifyapp.com/notifications')
    time.sleep(3)

@step('notification is fired in dynamodb')
def step_impl(context):
    try:
        browser.execute_script('''window.open("http://bings.com","_blank");''')
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[1])
        create_notif_dynamodb()
        step_result.clear()
        step_result.append('Pass')
    except Exception as e:
        step_result.clear()
        step_result.append('Fail')
        logging.info(e)    

@step('should execute {key}')
def step_impl(context, key):
    conn = http.client.HTTPSConnection("api.zephyrscale.smartbear.com")
    result = step_result[0]
    logging.info('Result : ' + str(result))
    payload = "{\n  \"projectKey\": \"OCS\",\n  \"testCaseKey\": \"" + key + "\",\n  \"testCycleKey\": \"" + testcycle[0] +"\",\n  \"statusName\": \"" + result + "\",\n  \"testScriptResults\": [\n    {\n      \"statusName\": \"" + result + "\",\n      \"actualEndDate\": \"2018-05-20T13:15:13Z\",\n      \"actualResult\": \"Articles successfully created!\"\n    }\n  ],\n  \"actualEndDate\": \"2018-05-20T13:15:13Z\",\n  \"executionTime\": 120000,\n  \"executedById\": \"61a88eb42278e7006b31eeb8\",\n  \"assignedToId\": \"61a88eb42278e7006b31eeb8\",\n  \"comment\": \"SUCCESS\",\n  \"customFields\": {\n\n  }\n\t\n}\n"
    #payload = "{\n  \"projectKey\": \"OCS\",\n  \"testCaseKey\": \"" + key + "\",\n  \"testCycleKey\": \"OCS-R620\",\n  \"statusName\": \"" + result + "\",\n  \"testScriptResults\": [\n    {\n      \"statusName\": \"" + result + "\",\n      \"actualEndDate\": \"2018-05-20T13:15:13Z\",\n      \"actualResult\": \"Articles successfully created!\"\n    }\n  ],\n  \"actualEndDate\": \"2018-05-20T13:15:13Z\",\n  \"executionTime\": 120000,\n  \"executedById\": \"61a88eb42278e7006b31eeb8\",\n  \"assignedToId\": \"61a88eb42278e7006b31eeb8\",\n  \"comment\": \"SUCCESS\",\n  \"customFields\": {\n\n  }\n\t\n}\n"
    
    headers = {
        'Content-Type': "application/json",
        'Authorization': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjb250ZXh0Ijp7ImJhc2VVcmwiOiJodHRwczovL2Nsb3VkY29uZmx1ZW5jZXBvc3Rlbm5vcmdlLmF0bGFzc2lhbi5uZXQiLCJ1c2VyIjp7ImFjY291bnRJZCI6IjYxYTg4ZWI0MjI3OGU3MDA2YjMxZWViOCJ9fSwiaXNzIjoiY29tLmthbm9haC50ZXN0LW1hbmFnZXIiLCJzdWIiOiI1MzQ0YjRjOC1mNTljLTM5MmEtYjA0NC0yMzM0MTA4MjcwYjciLCJleHAiOjE3MTAzOTQxMjYsImlhdCI6MTY3ODg1ODEyNn0.eZwOSh0ijFrvRMOvP8ztPTui1q2D6BiaE-QxDq-s11Y"
        }
    conn.request("POST", "/v2/testexecutions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    logging.info('Result : ' + str(data))


