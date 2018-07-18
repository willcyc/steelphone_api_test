#coding:utf-8
import unittest
import requests
import json

class MaketTest(unittest.TestCase):
	'''价格页面'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/market/getMarket.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_breedName_null(self):
		'''breedName为空'''
		payload = {'breedName':'','tableId':'','cityName':'安阳','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['toastMsg'],'对不起，没有相应行情表单，可切换其他品种或城市')
	
	def test_breedName_error(self):
		'''无相关breedName'''
		payload = {'breedName':'啦啦啦','tableId':'','cityName':'安阳','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['toastMsg'],'对不起，没有相应行情表单，可切换其他品种或城市')

	def test_breedId_null(self):
		'''breedId为空'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'安阳','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['breedId'],'010101')
	
	def test_breedId_error(self):
		'''无相关breedId'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'安阳','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'123456789','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['toastMsg'],'对不起，没有相应行情表单，可切换其他品种或城市')
	
	def test_cityId_null(self):
		'''cityId为空'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'安阳','cityId':'','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['cityName'],'上海')
	
	def test_cityId_error(self):
		'''无相关cityId'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'安阳','cityId':'8454512312156456451231321231535556','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['cityName'],'安阳')
		self.assertEqual(self.result['cityId'],'01030110')
	
	def test_cityName_null(self):
		'''cityName为空'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['cityName'],'安阳')
		self.assertEqual(self.result['cityId'],'01030110')

	def test_cityName_error(self):
		'''无相关cityName'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'啦啦啦','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		self.assertEqual(self.result['cityName'],'安阳')
		self.assertEqual(self.result['cityId'],'01030110')

	
	def test_market_success(self):
		'''参数传入均正确'''
		payload = {'breedName':'碳结圆钢','tableId':'','cityName':'安阳','cityId':'01030110','userId':'566453','deepBreedId':'',
		'machineCode':'','type':'price','isSub':'0','breedId':'01020101','marketId':''}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)

		self.assertEqual(self.result['breedName'],'碳结圆钢')    #断言查询的品种名称和选择的品种名称一致   
		self.assertEqual(self.result['cityName'],'安阳')         #断言查询的城市名称和选择的城市名称一致  
		self.assertIn(self.result['cityName'],self.result['tableName'])     #断言城市名称字段包含于当前行情表单名称中
		self.assertIn(self.result['breedName'],self.result['tableName'])    #断言品种名称字段包含于当前行情表单名称中
		self.assertEqual(self.result['breedId'],'01020101')      #断言查询的品种id与传入的品种id一致
		self.assertEqual(self.result['cityId'],'01030110')		 #断言查询的城市id与传入的城市id一致
		if self.result['toastMsg'] == []:
			self.assertEqual(self.result['toastMsg'],'')             #toastMsg为空表示当前行情不为空，否则“对不起，没有相应行情表单，可切换其他品种或城市”
		else:
			self.assertEqual(self.result['toastMsg'],'今日行情尚未发布，您可以查看其他行情')

		if self.result['markets'][0]['price'] == '****':
			self.assertEqual(self.result['hasRight'],'no')       #断言是否有权限
			print("没有权限")
		else:
			self.assertEqual(self.result['hasRight'],'yes')
			print("有权限")
	
if __name__ == '__main__':
	unittest.main()