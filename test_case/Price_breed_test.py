#coding:utf-8
import unittest
import requests
import json
from parameterized import parameterized

class BreedTest(unittest.TestCase):
	'''价格-选择品种页面'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/market/breed.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	@parameterized.expand([
		#用例名称，参数：userId、machineCode，实际结果，预期结果
		("both_null",'','','breeds',9),
		("userId_null",'','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breeds',9),
		("machineCode_null",'566453','','breeds',9),
		("machineCode__error",'566453','4546165132','breeds',9),
		("both_right",'566453','2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breeds',9)
	])

	def test_case(self,_,type,id,a,c):

		r = requests.get(self.base_url,params = {'userId':type,'machineCode':id})
		self.result = r.json()
		#print(self.result)
		#self.assertEqual(self.result[a],c)
		self.assertEqual(len(self.result[a]),c)

	def test_userId_error(self):
		'''参数userId不存在'''
		r = requests.get(self.base_url,params = {'userId':'784541564864897489468465','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员')  

	def test_all_error(self):
		'''参数userId、machineCode不存在'''
		r = requests.get(self.base_url,params = {'userId':'784541564864897489468465','machineCode':'4546165132'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员')  

	"""
	def test_breed(self):
		'''参数均为空'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':''})
		self.result = r.json()

		#self.assertEqual(self.result['breeds'][0]['name'],'普钢')   #断言一级品种
		self.assertEqual(len(self.result['breeds']),10)

	def test_userId_null(self):
		'''参数userId为空'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'})
		self.result = r.json()
		self.assertEqual(len(self.result['breeds']),10)   #断言一级品种是10个

	def test_userId_error(self):
		'''参数userId不存在'''
		r = requests.get(self.base_url,params = {'userId':'784541564864897489468465','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员')  

	def test_machineCode_null(self):
		'''参数machineCode为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['breeds']),10)    #断言一级品种是10个
	
	def test_machineCode_error(self):
		'''参数machineCode不存在'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'4546165132'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['breeds']),10)    #断言一级品种是10个   
	
	def test_all_error(self):
		'''参数userId、machineCode不存在'''
		r = requests.get(self.base_url,params = {'userId':'784541564864897489468465','machineCode':'4546165132'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员')  

	def test_all_right(self):
		'''参数userId、machineCode均正确'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(len(self.result['breeds']),10)    #断言一级品种是10个  
	"""
	
if __name__ == '__main__':
	unittest.main()