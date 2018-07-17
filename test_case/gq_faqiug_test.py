#coding:utf-8
import unittest
import requests
import json
import time,re
class QiuGouTest(unittest.TestCase):
	'''发布求购'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/gq/create.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_get_success(self):
		'''发布成功'''
		payload = {'breedAttr':'1-规格-sSpecification-∮10;2-材质-sMaterial-HRB335;3-产地/厂家-sFactory-申特','breedName':'二级螺纹钢','gqImgUrl':'','detailInfo':'',
		'province':'天津','userId':'744408','supplyType':'3','prodNum':'','machineCode':'90526B160362A7A4FECA22411080F8CF','id':'0','city':'天津','unit':'元/吨','price':'','breedId':'38'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)
		code = r.status_code
		self.assertEqual(code,200)

if __name__ == '__main__':
	unittest.main()