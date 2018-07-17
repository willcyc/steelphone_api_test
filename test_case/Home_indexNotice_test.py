#coding:utf-8
import unittest
import requests
import json

class IndexNoticeTest(unittest.TestCase):
	'''首页我的、短信是否打点'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/indexNotice.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_indexNotice_success(self):
		''''''
		r = requests.get(self.base_url,params = {'userId':'129647','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'})   #李平平
		self.result = r.json()

		'''首页短信红点'''
		if self.result['smsNoticeCount'] == '':
			self.assertEqual(self.result['smsNotice'],'0') 	#没有红点
			print("没有红点")
		else:
			self.assertEqual(self.result['smsNotice'],'1')	#有红点
			print("有红点")
			

		'''首页“我的”红点'''
		for x in range(1,5):
			a = 0
			url = 'https://mysteelapi.steelphone.com/v4/comment/reply/replyToMe.htm?&userId=129647&machineCode=2ACCCCDC5FBDBE59ADD70F1C100FE4BB&page=' + str(x)
			ms = requests.get(url)   #李平平
			self.resultms = ms.json()
			a += int(self.result['smsNotice'])
		if a == 0:
			self.assertEqual(self.result['myNotice'],'0')
			print("没有红点")
		else:
			self.assertEqual(self.result['myNotice'],'1')
			print("有红点")
			
if __name__ == '__main__':
	unittest.main()