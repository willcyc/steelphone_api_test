#coding:utf-8
import unittest
import requests
import json

class QiHuoSqsTest(unittest.TestCase):
	'''期货-上期所'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/futures/sqs.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_get_success(self):
		'''参数id、type均正确'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)

		self.assertEqual(self.result['keys'][0]['name'],'螺纹钢rb1810')
		self.assertEqual(self.result['keys'][1]['name'],'沪铜cu1809')
		self.assertEqual(self.result['keys'][2]['name'],'热轧hc1810')
		

if __name__ == '__main__':
	unittest.main()