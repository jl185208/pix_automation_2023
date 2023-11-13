from core.pixCore import *
from core.variables import *
from core.page import *
from core.elements import *
from core.db import *
from core.common import *
import time

aws_name = os.environ.get('AWS_NAME')
aws_pass = os.environ.get('AWS_PASS')

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
        # click api-wrapper-dev
        browser.find_element(By.XPATH, '/html/body/app/portal-ui/div/div/div[1]/centered-content/portal-dashboard/div/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/div/div').click()
        time.sleep(2)
        # click Manage Console
        browser.find_element(By.XPATH, '/html/body/app/portal-ui/div/div/div[1]/centered-content/portal-dashboard/div/portal-application-list/sso-expander/portal-instance-list/div[1]/portal-instance/div/sso-expander/portal-profile-list/div/portal-profile/span/span/a').click()
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(15)
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
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div/main/div/div[3]/div/div/div/div[3]/section/footer/div/div/div/div[2]').click()
        time.sleep(10)
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        return False

#create_notif_dynamodb()

#with open('logs/1680795796/logs/bdd-actual-1680795796.log', 'r+') as file:
   #data = file.read().replace('\n', '<br>')
   #data = file.readlines(1)
#myfile = open('logs/1680795796/logs/bdd-actual-1680795796.log', "r")
#with open('logs/1680795796/logs/bdd-actual-1680795796.log', 'r+') as file:
#    myline = file.readlines()
#    data = myline[line_count[0]:]
#    print(data)
