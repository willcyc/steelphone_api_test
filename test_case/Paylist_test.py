#coding:utf-8
import unittest
import requests
import json
class PayList(unittest.TestCase):
	'''获取缴费记录'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/finance/payInpour/list.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_creat_success(self):
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'','size':''} 
		r = requests.get(self.base_url,params = payload)
		code = r.status_code
		self.result = r.json()
		#print(code)
		#print(self.result)

		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')


if __name__ == '__main__':
	unittest.main()