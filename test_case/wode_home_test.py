#coding:utf-8
import unittest
import requests
import json

class WoDeHomeTest(unittest.TestCase):
	'''我的-首页'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/user/info/my.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_get_success(self):
		
		payload = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)

		self.assertEqual(self.result['adminName'],'程一川')
		self.assertEqual(self.result['inviteUrl'],'https://m.steelphone.com/v4/app/invite/qm/toIndex.ms?cellphone=ge2vsn22gi1dkpjwge')
		self.assertEqual(self.result['encCellphone'],'ge2vsn22gi1dkpjwge')
		self.assertEqual(self.result['registerTime'],'2017-03-06')
		self.assertEqual(self.result['userType'],'1')

if __name__ == '__main__':
	unittest.main()