#coding:utf-8
import time, sys
sys.path.append('./test_case')
from HTMLTestRunner import HTMLTestRunner
import unittest
from unittest import defaultTestLoader




# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './test_case'
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


