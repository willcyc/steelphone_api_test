#coding:utf-8
import unittest
import requests
import json

class ZhuCe_Getcode_Test(unittest.TestCase):
	'''注册-获取验证码'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/user/validateCode/get.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_get_success(self):
		'''参数均正确'''
		payload = {'userId':'','machineCode':'90526B160362A7A4FECA22411080F8CF','validateCodeKey':'AOLjDa0EgEOzMKArSVpJnTYqf353-vVGba4Ht6EfxeAyk5LSEmjD8GiWCo3SDsao','protocolVersion':'4.3.0'}
		r = requests.get(self.base_url,params = payload)											
		self.result = r.json()									
		print(self.result)
		#print(len(self.result))
		if len(self.result) == 1:
			self.assertEqual(self.result['result'],'true')
		else:
			self.assertEqual(self.result['errorstr'],'对不起，该号码已被注册，请更换其它号码！')

if __name__ == '__main__':
	unittest.main()