#coding:utf-8
import unittest
import requests
import json

class ArticleListTest(unittest.TestCase):
	'''资讯页面文章列表'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/article/list.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_articlelist_success(self):
		'''资讯页面'''
		list = ['0501','0101','03','0502','02']  #资讯页面：热点、快讯、微谈、国际列表，报告页面
		for al in list:
			r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','page':'1','channelId':str(al)})
			self.result = r.json()
			#print(self.result)
			code = r.status_code
			#print(code)
			self.assertEqual(code,200)

if __name__ == '__main__':
	unittest.main()