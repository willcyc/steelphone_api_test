#coding:utf-8
import unittest
import requests
import json
from random import choice

class AddressList(unittest.TestCase):
	'''获取收件地址列表、设置默认地址、删除列表中地址'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/finance/address/list.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_creat_success(self):
		#=============获取收件地址列表=============
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB'}
		r = requests.get(self.base_url,params = payload)
		code = r.status_code
		self.result = r.json()
		#print(code)
		#print(self.result)
		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')
		
		#=============获取收件地址id=============
		list = []
		for i in self.result['addresses']:
			#print(i)
			list.append(i['id'])
		#print(list)
		
		#=============设置默认收件地址=============
		id01 = choice(list)   #获取随机地址
		print(id01)
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':id01}  #id从列表中获取
		r = requests.post("https://mysteelapi.steelphone.com/v4/finance/address/setDefault.htm?",params = payload)
		code = r.status_code
		self.result = r.json()
		#print(code)
		#print(self.result)

		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')
		
		#=============删除收件地址列表中随机地址=============
		'''
		for id in list:
			#print(id)   #删除所有地址
		'''
		id02 = choice(list) 
		print(id02)
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':id02}   #id从list列表中获取
		r = requests.get('https://mysteelapi.steelphone.com/v4/finance/address/delete.htm?',params = payload)
		code = r.status_code
		self.result = r.json()
		#print(code)
		#print(self.result)

		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')

if __name__ == '__main__':
	unittest.main()