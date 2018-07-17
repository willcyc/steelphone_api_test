#coding:utf-8
import unittest
import requests
import json

class ArticleDetailTest(unittest.TestCase):
	'''资讯页面原生文章详情页底部信息'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/article/detail.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_both_null(self):
		'''参数id、type为空'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'','type':''}
		r = requests.get(self.base_url,params = payload)
		code = r.status_code
		#print(code)	
		self.assertEqual(code,400)

	def test_id_null(self):
		'''参数id为空'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'','type':'1'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['errorstr'],'参数不能为空')

	def test_type_null(self):
		'''参数type为空'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'638280','type':''}
		r = requests.get(self.base_url,params = payload)
		code = r.status_code
		#print(code)	
		self.assertEqual(code,400)

	def test_id_error(self):
		'''参数id错误'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'6382886','type':'1'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		if self.result['result'] == 'true':
			self.assertEqual(self.result['channelName'],'')
		else:
			self.assertEqual(self.result['errorstr'],'文章不存在')

	def test_type_error(self):
		'''参数type错误'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'638280','type':'225'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['channelName'],'')

	def test_both_error(self):
		'''参数id、type均错误'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'63828230','type':'225'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['channelName'],'')


	def test_articledetail_success(self):
		'''参数id、type均正确'''
		payload = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','id':'638280','type':'1'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['id'],'638280')
		self.assertEqual(self.result['channelName'],'五元报告')
		self.assertEqual(self.result['channelId'],'0203')

if __name__ == '__main__':
	unittest.main()