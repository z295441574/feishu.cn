#coding=utf-8
import sys,os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)

from appium import webdriver
from YAML.yaml import *
from Logs.logging_test import *

def login():

    data = get_yaml_load_all("config.yaml")
    desired_caps = {
        'platformName': data['desired_caps']['platformName'],
        'deviceName': data['desired_caps']['deviceName'],
        'platformVersion': data['desired_caps']['platformVersion'],
        'appPackage': data['desired_caps']['appPackage'],
        'appActivity': data['desired_caps']['appActivity'],
        'unicodeKeyboard': data['desired_caps']['unicodeKeyboard'],
        'resetKeyboard': data['desired_caps']['resetKeyboard'],
        'automationName': data['desired_caps']['automationName'],
        'newCommandTimeout': data['desired_caps']['newCommandTimeout'],
        'noReset': data['desired_caps']['noReset']
    }

    driver = webdriver.Remote(data['desired_caps']['URL'], desired_caps)
    driver.implicitly_wait(10)
    driver.get_window_size()
    logger.info("启动APP...")

    return driver

