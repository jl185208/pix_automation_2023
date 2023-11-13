from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from zipfile import ZipFile
from credentials.variables import *
from features.core.core import *
import os
import shutil
import time
import glob
import logging
import pyotp
import requests
from requests_oauthlib import OAuth1
import json
import http.client
import requests.auth
