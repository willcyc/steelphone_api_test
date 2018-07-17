#coding:utf-8
import unittest
import requests
import json

class GangTieTest(unittest.TestCase):
	'''钢铁饼图'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/breed/query/sonBreed.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_Volume_success(self):
		'''获取饼图'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','breedId':'01','protocolVersion':'4.6.6'})
		self.result = r.json()
		#print(self.result)
		s = self.result['breeds']
		#print(s)

		'''不锈钢'''
		self.assertEqual(s[0]['name'],'不锈钢')
		self.assertEqual(s[0]['hot'],'1')
		self.assertEqual(s[0]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010216.png')

		'''带钢'''
		self.assertEqual(s[1]['name'],'带钢')
		self.assertEqual(s[1]['hot'],'0')
		self.assertEqual(s[1]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010108.png')

		'''硅钢'''
		self.assertEqual(s[2]['name'],'硅钢')
		self.assertEqual(s[2]['hot'],'0')
		self.assertEqual(s[2]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010106.png')

		'''钢管'''
		self.assertEqual(s[3]['name'],'钢管')
		self.assertEqual(s[3]['hot'],'0')
		self.assertEqual(s[3]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010109.png')

		'''钢坯'''
		self.assertEqual(s[4]['name'],'钢坯')
		self.assertEqual(s[4]['hot'],'0')
		self.assertEqual(s[4]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/0307.png')

		'''结构钢'''
		self.assertEqual(s[5]['name'],'结构钢')
		self.assertEqual(s[5]['hot'],'0')
		self.assertEqual(s[5]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010201.png')

		'''建筑钢材'''
		self.assertEqual(s[6]['name'],'建筑钢材')
		self.assertEqual(s[6]['hot'],'1')
		self.assertEqual(s[6]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010101.png')

		'''冷镦拉丝'''
		self.assertEqual(s[7]['name'],'冷镦拉丝')
		self.assertEqual(s[7]['hot'],'0')
		self.assertEqual(s[7]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010210.png')

		'''冷轧'''
		self.assertEqual(s[8]['name'],'冷轧')
		self.assertEqual(s[8]['hot'],'0')
		self.assertEqual(s[8]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010104.png')

		'''热轧'''
		self.assertEqual(s[9]['name'],'热轧')
		self.assertEqual(s[9]['hot'],'1')
		self.assertEqual(s[9]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010103.png')

		'''特钢其他'''
		self.assertEqual(s[10]['name'],'特钢其他')
		self.assertEqual(s[10]['hot'],'0')
		self.assertEqual(s[10]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010202.png')

		'''涂镀'''
		self.assertEqual(s[11]['name'],'涂镀')
		self.assertEqual(s[11]['hot'],'0')
		self.assertEqual(s[11]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010105.png')

		'''型钢'''
		self.assertEqual(s[12]['name'],'型钢')
		self.assertEqual(s[12]['hot'],'0')
		self.assertEqual(s[12]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010107.png')

		'''硬线'''
		self.assertEqual(s[13]['name'],'硬线')
		self.assertEqual(s[13]['hot'],'0')
		self.assertEqual(s[13]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/01021201.png')

		'''中板'''
		self.assertEqual(s[14]['name'],'中板')
		self.assertEqual(s[14]['hot'],'0')
		self.assertEqual(s[14]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexSonBreedIco/010102.png')

if __name__ == '__main__':
	unittest.main()