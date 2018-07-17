#coding:utf-8
import unittest
import requests
import json

class ContentArticalTest(unittest.TestCase):
	'''原生文章详情页：以报告页面原生文章详情页为例'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/article/getContent.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_both_null(self):
		'''文章id和频道channelId都为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'','channelId':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员') 

	def test_id_null(self):
		'''文章id为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'','channelId':'0203'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员') 

	def test_id_error(self):
		'''文章id正确，频道channelId不匹配'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'564500','channelId':'0203'})
		self.result = r.json()
		#print(self.result)
		self.assertNotEqual(self.result['id'],'559313')			#断言文章id不匹配正确的id
		self.assertEqual(self.result['channelId'],'0203')		#断言频道id与传入参数相同
		self.assertNotEqual(self.result['title'],'Mysteel：3月钢坯或呈坚挺趋强运行之势')      #断言文章标题不匹配

	def test_channelId_null(self):
		'''频道channelId为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员') 
	
	def test_channelId_error(self):
		'''频道channelId正确、文章id不匹配'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':'0604040401'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['id'],'559313')			#断言文章id与传入参数相同
		self.assertNotEqual(self.result['channelId'],'0203')	#断言频道id不匹配
		self.assertEqual(self.result['title'],'Mysteel：3月钢坯或呈坚挺趋强运行之势')

	def test_id_iserror(self):
		'''频道channelId正确、文章id错误'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'55','channelId':'0604040401'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'参数不能为空') 

	def test_channelId_iserror(self):
		'''文章id正确、频道channelId错误'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':'0604401'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员') 

	def test_both_error(self):
		'''频道channelId、文章id均错误'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559','channelId':'0604401'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'客服紧急处理中，请等待或联系管理员') 

	def test_both_right(self):
		'''文章id和频道channelId匹配'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':'559313','channelId':'0203'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['id'],'559313')            #断言文章id与传入参数相同
		self.assertEqual(self.result['channelId'],'0203')		#断言频道id与传入参数相同
		self.assertEqual(self.result['title'],'Mysteel：3月钢坯或呈坚挺趋强运行之势')

if __name__ == '__main__':
	unittest.main()