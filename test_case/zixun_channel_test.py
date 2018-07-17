#coding:utf-8
import unittest
import requests
import json

class ChannelTitleTest(unittest.TestCase):
	'''资讯页面标签'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/channel/zixun.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_channel_title(self):
		'''资讯页面标题'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','protocolVersion':'4.5.0'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['channels'][0]['name'],'热点')
		self.assertEqual(self.result['channels'][1]['name'],'快讯')
		self.assertEqual(self.result['channels'][2]['name'],'专题')
		self.assertEqual(self.result['channels'][3]['name'],'微谈')
		self.assertEqual(self.result['channels'][4]['name'],'国际')


if __name__ == '__main__':
	unittest.main()