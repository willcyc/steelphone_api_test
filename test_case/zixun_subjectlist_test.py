#coding:utf-8
import unittest
import requests
import json

class SubjectListTest(unittest.TestCase):
	'''资讯页面-专题列表'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/article/subject/list.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_keyword_in_list(self):
		'''资讯页面专题列表-输入存在的搜索关键字'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','keywords':'油价'})
		self.result = r.json()
		#print(self.result)
		self.assertIn('油价',self.result['subjects'][0]['title'])

	def test_keyword_notin_list(self):
		'''资讯页面专题列表-输入不存在的搜索关键字'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','keywords':'啦啦啦哈哈哈'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['subjects'],[])

	def test_subject_list(self):
		'''资讯页面专题列表'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','keywords':''})
		self.result = r.json()
		#print(self.result)
		
		code = r.status_code
		#print(code)
		self.assertEqual(code,200)
		print(self.result['subjects'][0]['time'])   #最新更新的时间

if __name__ == '__main__':
	unittest.main()