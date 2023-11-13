from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from zipfile import ZipFile
from core.pixCore import *

# Settings Page
xpath_page_ver = '/html/body/div[1]/main/h1'
xpath_fire_button = '/html/body/div[1]/main/button'
xpath_notif = '/html/body/div[2]/div[2]/div/div/div[2]'




