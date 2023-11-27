# coding=utf-8
import sys,os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
from Public import  HTMLTestReportCN as HTMLTestRunner#导入中文报告
import unittest,time
if __name__ == '__main__':
    test_dir = os.path.join(os.getcwd(),'TestCase')
    test_report = os.path.join(os.getcwd(), 'Report')
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = test_report+'/result_'+now+'.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="APP测试报告", description='用例执行情况：')
    runner.run(discover)
