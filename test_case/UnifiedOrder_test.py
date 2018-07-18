#coding:utf-8
import unittest
import requests
import json
class UnifiedOrder(unittest.TestCase):
	'''预支付下单'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/finance/pay/unifiedOrder.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_creat_success(self):
		payload = {'attach':'0|||0506-全品种-1200-|||1|||13839205941','coupon':'0','payFee':30000,'totalFee':30000,
		'userId':566453,'payType':0,'machineCode':'90526B160362A7A4FECA22411080F8CF','score':0,'deviceInfo':13839205941} 
		#attach:附加信息；coupon：使用抵用券 单位:分；payFee：实际支付金额，单位:分；totalFee：总金额，单位:分；payType：支付渠道 0-支付宝1-微信2-apple pay；score：使用积分
		r = requests.post(self.base_url,params = payload)
		code = r.status_code
		self.result = r.json()
		#print(code)
		print(self.result)

		self.assertEqual(code,200)
		self.assertEqual(self.result['result'],'true')

if __name__ == '__main__':
	unittest.main()