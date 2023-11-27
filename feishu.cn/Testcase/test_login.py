#coding=utf-8
import sys,os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
import unittest
from Data_driven.login_setup import *
class login_test(unittest.TestCase):
    def test_cold_start_A(self):
        p = os.popen('adb shell pm clear com.ss.android.lark')
        p.close()
        logger.info("执行清除缓存数据")
        L = login()
        L.implicitly_wait(10)
        try:
            L.find_element_by_xpath('//*[@text="个人信息保护指引"]').is_displayed()
        except:
            pass
        else:
            L.find_element_by_xpath('//*[@text="同意"]').click()
            logger.info("同意个人信息保护指引")
        L.implicitly_wait(10)
        try:
            L.find_element_by_xpath('//*[@text="登录"]').is_displayed()
        except:
            pass
        else:
            L.find_element_by_xpath('//*[@text="登录"]').click()
            logger.info("点击登录")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="请输入你的手机号"]').send_keys('13534077215')
            logger.info("输入手机号")
            L.implicitly_wait(10)
            L.find_element_by_id('com.ss.android.lark:id/checkBoxPolicy').click()
            logger.info("勾选协议")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="下一步"]').click()
            logger.info("点击下一步")
            L.find_element_by_xpath('//*[@text="密码登录"]').click()
            logger.info("点击密码登录")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('test.1234')
            logger.info("输入密码")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="下一步"]').click()
            logger.info("点击下一步")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="测试"]').click()
            logger.info("选择测试账号")
            L.implicitly_wait(10)
            try:
                L.find_element_by_xpath('//*[@text="邀请同事共同体验飞书"]').is_displayed()
            except:
                L.find_element_by_xpath('//*[@text="通讯录"]').click()
                logger.info("点击通讯录")
                L.find_element_by_xpath('//*[@text="外部联系人"]').click()
                logger.info("点击外部联系人")
                L.find_element_by_xpath('//*[@text="test2"]').click()
                logger.info("点击test2")
                L.find_element_by_xpath('//*[@text="消息"]').click()
                L.find_element_by_xpath('//*[@text="发送给 test2"]').send_keys('hello word')
                L.find_element_by_id('com.ss.android.lark:id/btn_send').click()
                logger.info("发送消息")

    def test_hot_start_B(self):
        L = login()
        L.implicitly_wait(10)
        try:
            L.find_element_by_xpath('//*[@text="登录"]').is_displayed()
        except:
            try:
                L.find_element_by_xpath('//*[@text="邀请同事共同体验飞书"]').is_displayed()
            except:
                L.find_element_by_xpath('//*[@text="通讯录"]').click()
                logger.info("点击通讯录")
                L.find_element_by_xpath('//*[@text="外部联系人"]').click()
                logger.info("点击外部联系人")
                L.find_element_by_xpath('//*[@text="test2"]').click()
                logger.info("点击test2")
                L.find_element_by_xpath('//*[@text="消息"]').click()
                L.find_element_by_xpath('//*[@text="发送给 test2"]').send_keys('hello word')
                L.find_element_by_id('com.ss.android.lark:id/btn_send').click()
                logger.info("发送消息")
        else:
            L.find_element_by_xpath('//*[@text="登录"]').click()
            logger.info("点击登录")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="请输入你的手机号"]').send_keys('13534077215')
            logger.info("输入手机号")
            L.implicitly_wait(10)
            L.find_element_by_id('com.ss.android.lark:id/checkBoxPolicy').click()
            logger.info("勾选协议")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="下一步"]').click()
            logger.info("点击下一步")
            L.find_element_by_xpath('//*[@text="密码登录"]').click()
            logger.info("点击密码登录")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="请输入密码"]').send_keys('test.1234')
            logger.info("输入密码")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="下一步"]').click()
            logger.info("点击下一步")
            L.implicitly_wait(10)
            L.find_element_by_xpath('//*[@text="测试"]').click()
            logger.info("选择测试账号")
            L.implicitly_wait(10)
            try:
                L.find_element_by_xpath('//*[@text="邀请同事共同体验飞书"]').is_displayed()
            except:
                L.find_element_by_xpath('//*[@text="通讯录"]').click()
                logger.info("点击通讯录")
                L.find_element_by_xpath('//*[@text="外部联系人"]').click()
                logger.info("点击外部联系人")
                L.find_element_by_xpath('//*[@text="test2"]').click()
                logger.info("点击test2")
                L.find_element_by_xpath('//*[@text="消息"]').click()
                L.find_element_by_xpath('//*[@text="发送给 test2"]').send_keys('hello word')
                L.find_element_by_id('com.ss.android.lark:id/btn_send').click()
                logger.info("发送消息")


if __name__ == "__main__":
    unittest.main()
