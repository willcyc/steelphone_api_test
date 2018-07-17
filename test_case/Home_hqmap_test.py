#coding:utf-8
import unittest
import requests
from parameterized import parameterized
#from nose.tools import assert_equal
import json


class HomePageHqmapTest(unittest.TestCase):
	'''首页广告-行情地图'''
	

	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/getAdv.htm?"

	def tearDown(self):
		#print(self.result)
		pass
	
	@parameterized.expand([
		#用例名称，参数：type、id，实际结果，预期结果
		("both_null",'','','adv',[]),
		("id_null",6,'','adv',[]),
		("type_error_null",4,1,'adv',[]),
		("id_error",6,5,'adv',[]),
		("both_error_null",5,5,'adv',[])
	])

	def test_case(self,_,type,id,a,c):

		r = requests.get(self.base_url,params = {'type':type,'id':id})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result[a],c)
		#print(a)

	def test_hqmap_type_null(self):
		'''参数type为空：启动页广告'''
		r = requests.get(self.base_url,params = {'type':'','id':1})
		self.result = r.json()
		#print(self.result)
		#self.assertEqual(self.result['adv'][0]['title'],"2018半年会--夏尊恩")

	def test_hqmap_success(self):
		'''行情地图查询成功'''
		r = requests.get(self.base_url,params = {'type':6,'id':1})
		self.result = r.json()
		#print(self.result)
		
		for val in self.result['adv']:
			#print(val)
			pass
		#print(val['id'])
		self.assertEqual(val['id'],'3685')     #广告id
		self.assertEqual(val['title'],'我的钢铁行情地图')    #广告标题
		self.assertEqual(val['description'],'6')    #广告位置
		self.assertEqual(val['src'],'https://m.steelphone.com/app/map/index.html?UAlocal=1&dt=1#hqmap')  #广告跳转地址
		self.assertEqual(val['type'],'1')    #广告的频道id
		self.assertEqual(val['url'],'http://mfs.mysteelcdn.com/group1/M00/04/DB/rBL63lpe7E6AAR0pAAA1d-l94mQ951.png')   #广告图片路径	

if __name__ == '__main__':
	unittest.main()