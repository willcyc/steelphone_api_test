#coding:utf-8
import unittest
import requests
import json

class ZhuCe_Checkcode_Test(unittest.TestCase):
	'''注册-核对验证码'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/user/validateCode/check.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_get_success(self):
		'''参数均正确'''
		payload = {'userId':'','machineCode':'90526B160362A7A4FECA22411080F8CF','validateCode':'0018','cellphone':'18790000004'}
		r = requests.get(self.base_url,params = payload)											
		self.result = r.json()
		print(self.result)
		#print(len(self.result))
		if len(self.result) == 1:
			self.assertEqual(self.result['result'],'true')
		else:
			self.assertEqual(self.result['errorstr'],'验证码失效！')

if __name__ == '__main__':
	unittest.main()