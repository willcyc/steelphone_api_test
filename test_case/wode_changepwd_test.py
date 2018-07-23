#coding:utf-8
import unittest
import requests
import json

class ChangePwdTest(unittest.TestCase):
	'''我的-修改密码'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/user/password/update.htm?"
		
	def tearDown(self):
		#print(self.result)
		pass

	def test_oldpwd_error(self):
		'''旧密码错误'''
		r = requests.get(self.base_url,params = {'newPassword':'123456','userId':'566453','oldPassword':'12345','machineCode':'4B49B9A413D01B2EB2139C82782AF1FB'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['result'],'false')

	def test_newpwd_error(self):
		'''新密码格式错误'''
		r = requests.get(self.base_url,params = {'newPassword':'123456测试','userId':'566453','oldPassword':'123456','machineCode':'4B49B9A413D01B2EB2139C82782AF1FB'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['result'],'false')

	def test_change_success(self):
		'''修改成功'''
		r = requests.get(self.base_url,params = {'newPassword':'123456','userId':'566453','oldPassword':'123456','machineCode':'4B49B9A413D01B2EB2139C82782AF1FB'})
		self.result = r.json()
		code = r.status_code
		#print(self.result)
		
		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')
		
if __name__ == '__main__':
	unittest.main()