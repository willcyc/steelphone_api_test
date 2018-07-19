#coding:utf-8
import time, sys
sys.path.append('./ReceiveAddress')
#sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from unittest import defaultTestLoader

from email.mime.text import MIMEText
from email.header import Header
import smtplib
import os
#from db_fixture import test_data

#===============定义发送邮件=============
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    
    #发送邮箱
    sender = 'leaning001@126.com'
    
    #接收邮箱
    receiver = 'leaning002@126.com,13839205941@163.com'

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    
    msg['From'] = sender    
    msg['To'] = receiver

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('email has send out!')

#=========查找测试报告目录，找到最新生成的测试报告文件=========
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './ReceiveAddress'
#discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    #test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Mysteelphoneapi接口自动化测试',
                            description='运行环境：Python, Requests, unittest ')
    runner.run(testsuit)
    fp.close()

    file_path = new_report('./report/') #查找新生成的报告
    send_mail(file_path)   #调用发邮件模块


