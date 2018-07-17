#coding:utf-8
import unittest
import requests
import json

class ChannelSonTitleTest(unittest.TestCase):
	'''资讯页面子标签'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/channel/getSon.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_channel_son_title(self):
		'''资讯页面子标题'''
		list = ['01','0502']
		for al in list:
			r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','channelId':str(al)})
			self.result = r.json()
			#print(self.result)
			if al == '01':
				self.assertEqual(self.result['channels'][0]['name'],'宏观')
				self.assertEqual(self.result['channels'][1]['name'],'行情')
				self.assertEqual(self.result['channels'][2]['name'],'库存')
				self.assertEqual(self.result['channels'][3]['name'],'钢厂')
			else:
				self.assertEqual(self.result['channels'][0]['name'],'全部')
				self.assertEqual(self.result['channels'][1]['name'],'热点评述')
				self.assertEqual(self.result['channels'][2]['name'],'反倾销')
				self.assertEqual(self.result['channels'][3]['name'],'市场汇总')
				self.assertEqual(self.result['channels'][4]['name'],'出口报价')
				self.assertEqual(self.result['channels'][5]['name'],'国际新闻')

if __name__ == '__main__':
	unittest.main()