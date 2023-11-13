from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from zipfile import ZipFile
import os
import shutil
import time
import glob
import logging
import pyotp
import requests
import json
import http.client
from os.path import exists
import requests.auth
from selenium.webdriver.support.ui import Select
import time
import sqlite3
import json
import base64
from datetime import date

conn = sqlite3.connect('shopify.db')
today = date.today()
process_time_el = time.process_time
c = conn.cursor()
ID = str(int(time.time()))
ss_count = []

def loggings():
    # timestamp
    #ID = str(int(time.time()))
    mkdir_timestamp = 'logs/' + ID 
    mkdir_logs = 'logs/' + ID + '/logs'
    mkdir_screenshots = 'logs/' + ID + '/screenshots'
    os.mkdir(mkdir_timestamp)
    os.mkdir(mkdir_logs)
    os.mkdir(mkdir_screenshots)
    with open('logs/' + ID + '/Test_Results.txt', 'w') as f:
        f.write('Please see below test results : ')
    logging.basicConfig(filename='logs/' + ID + '/logs/bdd-actual-' + ID + '.log', filemode='w', format='<br> %(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.info('Current time stamp : ' + ID)  


def ss(filename):
    fname = 'logs/' + str(ID) + '/screenshots/' + str(filename) + '.png'
    return fname