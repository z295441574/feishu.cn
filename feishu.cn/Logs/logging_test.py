# -*- coding:utf-8 -*-
import sys,os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
import logging
import time
# 创建日志记录器
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 设置日志输出格式
format= logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
now = time.strftime("%Y-%m-%d-%H_%M_%S")
# 创建一个Handler用于将日志写入文件
# logFile = './log.txt'
current_work_dir = os.path.dirname(__file__)
logFile = current_work_dir+'\\log\\'+'%s_log.txt'%now
fh = logging.FileHandler(logFile, mode='a', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(format)
logger.addHandler(fh)
# 同样的，创建一个Handler用于控制台输出日志
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(format)
logger.addHandler(ch)