from core.pixCore import *
from core.variables import *
from core.page import *
from core.elements import *
from core.db import *
from core.common import *
import time

notif_time_dump = []

@step('that notifications page is accessed')
def step_impl(context):
    start_log_line(context.scenario)
    # Click notification button
    browser.find_element(By.XPATH, '/html/body/div[1]/header/nav/a[3]').click()
    logging.info('Notification button is clicked.')
    time.sleep(5)

@step('notification is open and less than 1 minute')
def step_impl(context):
    # Get time of notification
    notif_recent_time = browser.find_element(By.XPATH, '/html/body/div[1]/main/div/section/div/section[1]/div[2]/span').text
    notif_time_dump.clear()
    notif_time_dump.append(notif_recent_time)
    notif_actual = notif_time_dump[0].strip('s')
    if int(notif_actual) < 60:
        step_result.clear()
        step_result.append('Pass')
        logging.info('Actual time : ' + str(notif_recent_time))
        pass
    else:
        step_result.clear()
        step_result.append('Fail')
        loging.info('Notification is not yet displayed.')
        assert False
    # Get notification status : Expected -> OPEN
    notif_status = browser.find_element(By.XPATH, '/html/body/div[1]/main/div/section/div/section[1]/div[2]/div').text
    logging.info(notif_status)
    if notif_status == 'OPEN':
        step_result.clear()
        step_result.append('Pass')
        logging.info('Notification value : ' + str(notif_status))
        pass
    else:
        step_result.clear()
        step_result.append('Fail')
        logging.info('Notification is not OPEN.')
        logging.info('Notification value : ' + str(notif_status))

@step('the notification is clicked')
def step_impl(context):
    # Click latest notification
    browser.find_element(By.XPATH, '/html/body/div[1]/main/div/section/div/section[1]').click()
    time.sleep(2)
    pass

@step('marked as notification is solved')
def step_impl(context):
    # Click the mark notification as solved button
    browser.find_element(By.XPATH, '/html/body/div[1]/main/button').click()
    time.sleep(1)
    # Check if button is changed to archived
    archived_button = browser.find_element(By.XPATH, '/html/body/div[1]/main/button').text
    if str(archived_button) == 'NOTIFICATION ARCHIVED':
        step_result.clear()
        step_result.append('Pass')
        logging.info('Button : ' + str(archived_button))
        pass
    else:
        step_result.clear()
        step_result.append('Fail')
        logging.info('Button was not archived.')
        assert False

@step('should be listed in archived')
def step_impl(context):
    # Click Return
    browser.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div').click()
    logging.info('Return button was clicked.')
    # Click Archived
    browser.find_element(By.XPATH, '/html/body/div[1]/main/nav/ul/li[2]/a').click()
    logging.info
    ('Archived button was clicked.')
    time.sleep(1)
    browser.get_screenshot_as_file('logs/archived-notif.png')
    # Check notification 
    notif_no = browser.find_element(By.XPATH, '/html/body/div[1]/main/div/section/div/section/div[1]/h3').text
    logging.info('Notification : ' + str(notif_no))
    if notif_no != '':
        step_result.clear()
        step_result.append('Pass')
        logging.info('Notification is archived.')
    else:
        step_result.clear()
        step_result.append('Fail')
        logging.info('Notification was not archived.')
    time.sleep(5)