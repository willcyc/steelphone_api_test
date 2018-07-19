#coding:utf-8
import os
import smtplib  
import time, sys
import unittest
from email.header import Header
from unittest import defaultTestLoader
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText 
from HTMLTestRunner import HTMLTestRunner
sys.path.append('./ReceiveAddress')

#===============定义发送邮件=============
def send_mail(file_new):

    #发件人
    #asender = 'leaning001@126.com' 
    asender = 'chengyc@mysteel.com'

    #发件人邮箱用户名、密码  
    #ausername = 'leaning001@126.com' 
    ausername = username 
    apassword = password 

    #多个收件人用逗号隔开  
    areceiver = 'leaning002@126.com,13839205941@163.com,yuezp@mysteel.com'  

    #抄送人
    acc = 'leaning003@126.com,leaning004@126.com,zhaopp@mysteel.com'  
    asubject = u'自动化测试报告'  
      
    #发送邮箱的服务器  
    #asmtpserver = 'smtp.126.com'  
    asmtpserver = 'smtp.exmail.qq.com'
      
    #配置发件人、收件人信息  
    msgroot = MIMEMultipart('related')
    msgroot['Subject'] = asubject  
    msgroot['to'] = areceiver  
    msgroot['Cc'] = acc  
    msgroot['from'] = asender 

    #配置邮件正文内容  
    thebody = MIMEText(u'Please check the attachment, thanks!', 'plain', 'utf-8')  
    msgroot.attach(thebody)  

    #获取最新报告作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码  
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')  
    att['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'    
    attname ='attachment; filename ="MysteelphoneapiTestReport.html"'   #附件名称
    att['Content-Disposition'] = attname     
    msgroot.attach(att)  
      
    asmtp = smtplib.SMTP()  
    asmtp.connect(asmtpserver)  
    asmtp.login(ausername, apassword) 
    asmtp.sendmail(asender, areceiver.split(',') + acc.split(','), msgroot.as_string())  
    asmtp.quit()

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
