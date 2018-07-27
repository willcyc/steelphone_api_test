#coding:utf-8
import unittest
import requests
import json
from parameterized import parameterized

class DuanxinMyunsubTest(unittest.TestCase):
	'''短信-取消短信订制'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/sms/unsub.htm?"
		
	def tearDown(self):
		#print(self.result)
		pass

	'''判断用户是否登录'''
	payload = {'cellphone':'13839205941','password':'e10adc3949ba59abbe56e057f20f883e','token':'1507bfd3f797e28773a','ostype':'1','machineInfo':'HUAWEI,PIC-AL00,26','softVersion':'4.7.3'}
	r = requests.get("http://mysteelapi.steelphone.com/v4/user/login.htm?",params = payload)
	denglu = r.json()
	#print(denglu)

	'''
	if denglu['result'] == 'false':
		@parameterized.expand([
			#用例名称，参数：packId、userId、machineCode，实际结果，预期结果
			("all_null",'','','','errorstr','传参异常！'),
			("packId_null",'','566453','90526B160362A7A4FECA22411080F8CF','errorstr','套餐退订异常'),
			("userId_null",'201','','90526B160362A7A4FECA22411080F8CF','errorstr','传参异常！'),
			("machineCode_null",'201','566453','','errorstr','该账户已在其他设备上登录，请联系管理员！'),
			("packId_userId_null",'','','90526B160362A7A4FECA22411080F8CF','errorstr','传参异常！'),
			("packId_machineCode_null",'','566453','','errorstr','该账户已在其他设备上登录，请联系管理员！'),
			("userId_machineCode_null",'201','','','errorstr','传参异常！'),
			("packId_error",'2011','566453','90526B160362A7A4FECA22411080F8CF','errorstr','套餐退订异常'),
			("userId_error",'201','2917471','90526B160362A7A4FECA22411080F8CF','errorstr','用户不存在'),
			("machineCode_error",'201','2917471','90526B160362A7A4FECA22411080F8CF','errorstr','用户不存在'),
			("get_success",'201','566453','90526B160362A7A4FECA22411080F8CF','result','true')
		])

		def test_case(self,_,params1,params2,params3,a,b):

			r = requests.get(self.base_url,params = {'packId':params1,'userId':params2,'machineCode':params3})
			self.result = r.json()
			#print(self.result)
			self.assertEqual(self.result[a],b)
	'''

	#elif denglu['result'] == 'true':
	@parameterized.expand([
		#用例名称，参数：packId、userId、machineCode，实际结果，预期结果
		("all_null",'','','','errorstr','传参异常！'),
		("packId_null",'','566453','90526B160362A7A4FECA22411080F8CF','errorstr','套餐退订异常'),
		("userId_null",'201','','90526B160362A7A4FECA22411080F8CF','errorstr','传参异常！'),
		("machineCode_null",'201','566453','','errorstr','套餐退订异常'),
		("packId_userId_null",'','','90526B160362A7A4FECA22411080F8CF','errorstr','传参异常！'),
		("packId_machineCode_null",'','566453','','errorstr','套餐退订异常'),
		("userId_machineCode_null",'201','','','errorstr','传参异常！'),
		("packId_error",'2011','566453','90526B160362A7A4FECA22411080F8CF','errorstr','套餐退订异常'),
		("userId_error",'201','2917471','90526B160362A7A4FECA22411080F8CF','errorstr','用户不存在'),
		("machineCode_error",'201','2917471','90526B160362A7A4FECA22411080F8CF','errorstr','用户不存在'),
		("get_success",'201','566453','90526B160362A7A4FECA22411080F8CF','result','true')
	])

	def test_case(self,_,params1,params2,params3,a,b):

		r = requests.get(self.base_url,params = {'packId':params1,'userId':params2,'machineCode':params3})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result[a],b)

	"""
	def test_get_success(self):
		'''退订成功'''
		r = requests.get(self.base_url,params = {'packId':'201','userId':'566453','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915'})
		self.result = r.json()
		print(self.result)
		self.assertEqual(self.result['result'],'true')
	"""	
		
if __name__ == '__main__':
	unittest.main()