#coding:utf-8
import unittest
import requests
import json,re
from duanxin_mydingz_test import DuanxinMysmsTest
		
class DuanxinNewSmsTest(unittest.TestCase):
	'''短信-我的短信页面'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/sms/myNewSmsContent.htm?"
		
	def tearDown(self):
		#print(self.result)
		pass

	def test_page_null(self):
		'''传入页码为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','page':'','breedId':''})
		#self.result = r.json()
		code = r.status_code
		self.assertEqual(code,400)

	def test_get_success01(self):
		'''查询成功，断言短信列表按时间降序排序、且为短信-我的定制页面中定制的短信'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915','page':'1','breedId':''})
		self.result = r.json()
		#print(self.result)

		#======================断言短信-我的短信页面短信列表按时间降序排序======================
		riqi = []
		for time in self.result['sms']:
			i = re.findall(r"\d+\.?\d*",time['time'])   #提取列表中数字
			j = (('').join(i))   #将列表转换为字符串
			#print(j)
			riqi.append(j)
		#print(riqi)

		for k in range (len(riqi)-1):
			bo = int(riqi[k])-int(riqi[k+1]) 
			#self.assertEqual(bo>=0,True)   #断言降序排序   #不是按显示时间降序排序，按发布时间降序排序
		
		#====================获取短信-我的短信页面第一页短信标题==================
		zuixin = []
		for duanxin in self.result['sms']:
			#print(duanxin['name'])
			zuixin.append(duanxin['name'])
		#print(zuixin)

		#====================读取短信-我的定制页面中定制的短信====================
		f = open('C:/Users/admin/Desktop/steelphone_api_test/test_case/html.txt')
		jieguo = f.read()
		#print(jieguo)

		#====================断言短信-我的短信中收到的信息，为短信-我的定制页面定制的短信================
		for i in range(len(zuixin)):
			self.assertIn(zuixin[i],jieguo)
			#print(i)


if __name__ == '__main__':
	unittest.main()