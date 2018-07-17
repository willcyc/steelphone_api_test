#coding:utf-8
import unittest
import requests
import json

class MaketDetailTest(unittest.TestCase):
	'''价格详情页'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/market/detail.htm?"

	def tearDown(self):
		pass

	def test_breedName_null(self):
		
		payload = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF','mId':'12488915','tId':'15278','code':'CN310000ST3605220208'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['shareInfo']['channelId'],payload['tId'])
		self.assertEqual(self.result['shareInfo']['objectId'],payload['mId'])

if __name__ == '__main__':
	unittest.main()