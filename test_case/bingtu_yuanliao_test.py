#coding:utf-8
import unittest
import requests
import json

class YuanLiaoTest(unittest.TestCase):
	'''原料饼图'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/breed/query/sonBreed.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_Volume_success(self):
		'''获取饼图'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':'09','protocolVersion':'4.6.6'})
		self.result = r.json()
		print(self.result)
		s = self.result['breeds']
		print(s)

		'''废钢'''
		self.assertEqual(s[0]['name'],'废钢')
		self.assertEqual(s[0]['hot'],'1')
		self.assertEqual(s[0]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0306.png')

		'''煤焦'''
		self.assertEqual(s[1]['name'],'煤焦')
		self.assertEqual(s[1]['hot'],'0')
		self.assertEqual(s[1]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/05.png')

		'''耐材'''
		self.assertEqual(s[2]['name'],'耐材')
		self.assertEqual(s[2]['hot'],'0')
		self.assertEqual(s[2]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0309.png')

		'''生铁'''
		self.assertEqual(s[3]['name'],'生铁')
		self.assertEqual(s[3]['hot'],'0')
		self.assertEqual(s[3]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0305.png')

		'''铁合金'''
		self.assertEqual(s[4]['name'],'铁合金')
		self.assertEqual(s[4]['hot'],'0')
		self.assertEqual(s[4]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0303.png')

		'''铁矿石'''
		self.assertEqual(s[5]['name'],'铁矿石')
		self.assertEqual(s[5]['hot'],'1')
		self.assertEqual(s[5]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0311.png')

if __name__ == '__main__':
	unittest.main()