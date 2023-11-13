from core.pixCore import *
from core.variables import *
from core.page import *
from core.elements import *
from core.db import *
from core.common import *
import time

@step('dashboard page is accessed')
def step_impl(context):
    start_log_line(context.scenario)
    # access dashboard using button
    browser.find_element(By.XPATH, '/html/body/div[1]/header/nav/a[1]').click()
    pass

@step('welcome back is displayed in dashboard')
def step_impl(context):
    # access dashboard using button
    time.sleep(2)
    db_wlcm_txt =  browser.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/h2').text
    logging.info('Welcome text in dashboard page : ' + str(db_wlcm_txt))
    if "Welcome Back" in str(db_wlcm_txt):
        step_result.clear()
        step_result.append('Pass')
        browser.get_screenshot_as_file('logs/dashboard.png')
        logging.info('Welcome back message is displayed in dashboard.')
        pass
    else:
        step_result.clear()
        step_result.append('Fail')
        logging.info('Welcome message was not displayed')

@step('recent order is clicked')
def step_impl(context):
    # access dashboard using button
    logging.info('PX3 Dashboard Page Validation')
    browser.find_element(By.XPATH, '/html/body/div[1]/header/nav/a[1]').click()
    pass

