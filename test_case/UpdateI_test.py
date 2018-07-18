#coding:utf-8
import unittest
import requests
import json
class UpdateI(unittest.TestCase):
	'''修改我的信息'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/user/info/update.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_creat_success(self):
		payload = {'address':'南极','userId':'483098','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','sex':'男','nickName':'小博','email':'zhangboqi@163.com','company':'上海钢联'}  
		r = requests.post(self.base_url,params = payload)
		code = r.status_code
		self.result = r.json()
		#print(code)
		#print(self.result)

		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')


if __name__ == '__main__':
	unittest.main()