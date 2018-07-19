import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText 
import time, sys
sys.path.append('./ReceiveAddress')
#sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from unittest import defaultTestLoader

from email.header import Header
import os 
  
#image包可以发送图片形式的附件  
# from email.mime.image import MIMEImage  
  
# 可以查询文件对应的'Content-Type'  
# import mimetypes  
# mimetypes.guess_type('c:\\users\\adminstrator\\desktop\\ceshi.xls')  
  
def send_mail(file_new):
    
    asender = 'leaning001@126.com'  
    #多个收件人用逗号隔开  
    areceiver = 'leaning002@126.com,13839205941@163.com'  
    acc = 'leaning003@126.com,leaning004@126.com'  
    asubject = u'自动化测试报告'  
      
    #阿里云邮箱的smtp服务器  
    asmtpserver = 'smtp.126.com'  
    ausername = username
    apassword = password
      
    #下面的to\cc\from最好写上，不然只在sendmail中，可以发送成功，但看不到发件人、收件人信息  
    msgroot = MIMEMultipart('related')
    msgroot['Subject'] = asubject  
    msgroot['to'] = areceiver  
    msgroot['Cc'] = acc  
    msgroot['from'] = asender  
      
    # MIMEText有三个参数，第一个对应文本内容，第二个对应文本的格式，第三个对应文本编码  
    thebody = MIMEText(u'Please check the attachment, thanks!', 'plain', 'utf-8')  
    msgroot.attach(thebody)  
      
    # 读取xls文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码  
    # att = MIMEText(open('C:\\ceshi.xls', 'rb').read(), 'base64', 'GB2312')  
    # att['Content-Type'] = 'application/vnd.ms-excel'  
    # att['Content-Disposition'] = 'attachment; filename ="1.xls"'  
      
    # 读取xlsx文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码  
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')  
    att['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  
    #下面的filename 等号(=)后面好像不能有空格  
    attname ='attachment; filename ="MysteelphoneapiTestReport.html"'  
    att['Content-Disposition'] = attname  
      
    msgroot.attach(att)  
      
    asmtp = smtplib.SMTP()  
    asmtp.connect(asmtpserver)  
    asmtp.login(ausername, apassword)  
      
    #发送给多人时，收件人应该以列表形式，areceiver.split把上面的字符串转换成列表  
    #只要在sendmail中写好发件人、收件人，就可以发送成功  
    # asmtp.sendmail(asender, areceiver.split(','), msgroot.as_string())  
      
    #发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中  
    asmtp.sendmail(asender, areceiver.split(',') + acc.split(','), msgroot.as_string())  
    asmtp.quit()

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


'''

#===============定义发送邮件=============
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    
    asender = 'leaning001@126.com'  
	#多个收件人用逗号隔开  
    areceiver = 'leaning002@126.com,13839205941@163.com'  
    acc = 'leaning003@126.com,leaning004@126.com' 

    msgroot = MIMEText(mail_body,'html','utf-8')
    asubject = Header("自动化测试报告",'utf-8')
    
    #thebody = MIMEText(u'Please check the attachment, thanks!', 'plain', 'utf-8')  
	#msgroot.attach(thebody) 
    
    msgroot = MIMEMultipart('related')  
    msgroot['Subject'] = asubject  
    msgroot['to'] = areceiver  
    msgroot['Cc'] = acc  
    msgroot['from'] = asender  

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("leaning001@126.com", "987456321cyc")
    #smtp.sendmail(asender,areceiver,msgroot.as_string())
    smtp.sendmail(asender, areceiver.split(',') + acc.split(','), msgroot.as_string()) 
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
                            description='运行环境：Requests, unittest ')
    runner.run(testsuit)
    fp.close()

    file_path = new_report('./report/') #查找新生成的报告
    send_mail(file_path)   #调用发邮件模块
    
  '''    