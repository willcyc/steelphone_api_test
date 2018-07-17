#coding:utf-8
import unittest
import requests
import json

class CityTest(unittest.TestCase):
	'''价格-选择城市页面'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/market/city.htm?"

	def tearDown(self):
		#print(self.result)
		pass
		
	def test_all_null(self):
		'''参数均为空'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':'','breedId':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'传参异常！')  
		
	def test_userId_null(self):
		'''参数userId为空'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':'020301'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['citys'][0]['citys'])>0,True)   #断言选择城市页面城市列表不为空

	def test_userId_error(self):
		'''参数userId不存在'''
		r = requests.get(self.base_url,params = {'userId':'1545454151545','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':'020301'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['citys'][0]['citys'])>0,True)   #断言选择城市页面城市列表不为空

	def test_machineCode_null(self):
		'''参数machineCode为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'','breedId':'020301'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['citys'][0]['citys'])>0,True)   #断言选择城市页面城市列表不为空

	def test_machineCode_error(self):
		'''参数machineCode不存在'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'4545000000000000006155','breedId':'020301'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['citys'][0]['citys'])>0,True)   #断言选择城市页面城市列表不为空

	def test_breedId_null(self):
		'''参数breedId为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'传参异常！')  

	def test_breedId_error(self):
		'''参数breedId不存在'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':'45656562212020100000000'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['citys'],[])  

	def test_all_error(self):
		'''参数都不存在'''
		r = requests.get(self.base_url,params = {'userId':'4454565123315468','machineCode':'47544','breedId':'45656562212020100000000'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['citys'],[])

	def test_all_right(self):
		'''参数均正确'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':'01010302'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['citys'][0]['citys'])>0,True)   #断言选择城市页面城市列表不为空
		self.assertEqual(self.result['citys'][0]['citys'][0]['name'],'上海')

if __name__ == '__main__':
	unittest.main()

