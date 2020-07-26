# -*- encoding=utf8 -*-
__author__ = "wzq"
import pytest
from airtest.core.api import *
import allure
import os
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
connect_device("Android://192.168.1.100:5555/5631511")
allure.feature('开关wifi')
current_path = os.getcwd()
print(current_path)
def test():
    """
    wifi开关功能测试
    :return:
    """
    keyevent('home')
    with allure.step('点击设置'):
        poco(text="设置").click()
    with allure.step('打开wlan设置'):
        poco(text="WLAN").click()
    with allure.step('打开wlan开关'):
        poco("android:id/checkbox").click()
    with allure.step('关闭wlan开关'):
        poco("android:id/checkbox").click()
    snapshot(filename=r'./test.png')
    with open('./test.png',mode='rb') as f:
        file=f.read()
        allure.attach(file,'wlan页面')
if __name__ == '__main__':
    pytest.main(['-s','-q','test.py','--alluredir={}\\report'.format(current_path)])
    os.system("allure generate --clean report")