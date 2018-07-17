#coding:utf-8
import unittest
import requests
import json
import time,re
class GongYingTest(unittest.TestCase):
	'''发布供应'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/gq/create.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_get_success(self):
		'''发布成功'''
		payload = {'breedAttr':'2472-规格-sSpecification-A00;2473-产地/牌号-sFactory-西南铝','breedId':'849','breedName':'铝锭','city':'曲靖','detailInfo':'',
		'gqImgUrl':'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/gq/1530618361609.jpg','id':'0','machineCode':'90526B160362A7A4FECA22411080F8CF','price':'',
		'prodNum':'','province':'云南','supplyType':'1','unit':'元/吨','userId':'744408'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)
		code = r.status_code
		self.assertEqual(code,200)

if __name__ == '__main__':
	unittest.main()