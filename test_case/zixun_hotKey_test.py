#coding:utf-8
import unittest
import requests
import json

class HotKeyTest(unittest.TestCase):
	'''首页文章热门搜索'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/article/hotKey.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_hotkey_list(self):
		'''首页文章热门搜索词'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':''})
		self.result = r.json()
		hotkey = self.result['hotTitle']
		print(hotkey)
		hot = ['废钢','钢坯','唐山','钢铁','沙钢','唐山钢市快报','铁矿石','煤焦','库存']
		for i in range(len(hotkey)):
			self.assertEqual(hotkey[i]['title'],hot[i])

if __name__ == '__main__':
	unittest.main()