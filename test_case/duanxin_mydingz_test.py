#coding:utf-8
import unittest
import requests
import json
from parameterized import parameterized

class DuanxinMysmsTest(unittest.TestCase):
	'''短信-我的定制页面'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/sms/getMySmsPack.htm?"
		
	def tearDown(self):
		#print(self.result)
		pass

	'''判断用户是否登录'''
	payload = {'cellphone':'13839205941','password':'e10adc3949ba59abbe56e057f20f883e','token':'1507bfd3f797e28773a','ostype':'1','machineInfo':'HUAWEI,PIC-AL00,26','softVersion':'4.7.3'}
	r = requests.get("http://mysteelapi.steelphone.com/v4/user/login.htm?",params = payload)
	denglu = r.json()
	#print(denglu)

	if denglu['result'] == 'true':
		@parameterized.expand([
			#用例名称，参数：userId、machineCode，预期结果1，预期结果2
			("both_null",'','','传参异常！','false'),
			("userId_null",'','90526B160362A7A4FECA22411080F8CF','传参异常！','false'),
			#("machineCode_null",'566453','','该账户已在其他设备上登录，请联系管理员！','false'),
			("userId_error",'5664532','90526B160362A7A4FECA22411080F8CF','用户不存在','false'),
			("userId_notmatch",'744408','90526B160362A7A4FECA22411080F8CF','该账户已在其他设备上登录，请联系管理员！','false'),
			("machineCode_error",'5664532','90526B160362A7A4FECA22411080F8CF','用户不存在','false'),
			("both_error",'56645325','90526B160362A7A4FECA22411080F8CF','用户不存在','false')

		])

		def test_case(self,_,type,id,a,c):

			r = requests.get(self.base_url,params = {'userId':type,'machineCode':id})
			self.result = r.json()
			#print(self.result)
			self.assertEqual(self.result['errorstr'],a)
			self.assertEqual(self.result['result'],c)

		def test_get_success(self):
			'''查询成功'''
			r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'90526B160362A7A4FECA22411080F8CF'})
			self.result = r.json()
			#print(self.result)
			dingzhi = []
			for dx in self.result['sms']:
				#print(dx['name'])
				dingzhi.append(dx['name'])
			#print (dingzhi)
			#========================将输出结果放入本地TXT文件中========================
			f = open (r'C:\Users\admin\Desktop\steelphone_api_test\test_case\html.txt','w')
			print (dingzhi,file = f)
			f.close()

			self.assertEqual(self.result['result'],'true')

	elif denglu['result'] == 'false':
		print("请退出账户：13839205941")

	"""
	def test_both_null(self):
		'''参数userId、machineCode为空'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'传参异常！')
		self.assertEqual(self.result['result'],'false')
		
	def test_userId_null(self):
		'''参数userId为空'''
		r = requests.get(self.base_url,params = {'userId':'','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'传参异常！')
		self.assertEqual(self.result['result'],'false')

	def test_machineCode_null(self):
		'''参数machineCode为空'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':''})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'该账户已在其他设备上登录，请联系管理员！')
		self.assertEqual(self.result['result'],'false')

	def test_userId_error(self):
		'''参数userId错误'''
		r = requests.get(self.base_url,params = {'userId':'5664532','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'用户不存在')
		self.assertEqual(self.result['result'],'false')

	def test_userId_notmatch(self):
		'''参数userId、machineCode不匹配'''
		r = requests.get(self.base_url,params = {'userId':'744408','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'该账户已在其他设备上登录，请联系管理员！')
		self.assertEqual(self.result['result'],'false')

	def test_machineCode_error(self):
		'''参数machineCode错误'''
		r = requests.get(self.base_url,params = {'userId':'5664532','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915465'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'用户不存在')
		self.assertEqual(self.result['result'],'false')

	def test_both_error(self):
		'''参数userId、machineCode错误'''
		r = requests.get(self.base_url,params = {'userId':'56645325','machineCode':'AA58FE7016CBECD8D3B5CCC9AFA0C915465'})
		self.result = r.json()
		#print(self.result)
		self.assertEqual(self.result['errorstr'],'用户不存在')
		self.assertEqual(self.result['result'],'false')
	"""

if __name__ == '__main__':
	unittest.main()