#coding:utf-8
import unittest
import requests
import json

class DuanxinMySearchTest(unittest.TestCase):
	'''短信-短信订制页面'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/sms/search.htm?"
		
	def tearDown(self):
		#print(self.result)
		pass

	def test_page_null(self):
		'''页码为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','page':'','keywords':''})
		code = r.status_code
		self.assertEqual(code,400)

	def test_get_success(self):
		'''查询成功'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','page':1,'keywords':''})
		self.result = r.json()
		#print(self.result)
		#self.assertEqual(self.result['count'],'1120')
		self.assertEqual(self.result['pagenum'],'75')
		
if __name__ == '__main__':
	unittest.main()