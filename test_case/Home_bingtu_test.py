#coding:utf-8
import unittest
import requests
import json

class VolumeXpicIndexNoticeTest(unittest.TestCase):
	'''首页饼图及所有两侧指数'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/getVolumeXpicIndexNotice.htm?"

	def tearDown(self):
		#print(self.result)
		pass

	def test_Volume_success(self):
		'''获取首页饼图及指数'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','protocolVersion':'4.6.5'})
		self.result = r.json()
		#print(self.result)
		a = self.result['module']
		b = self.result['subBreeds']
		c = self.result['datas']
		d = self.result['xpic']
		#print(a,b,c,d)
		
		'''首页第一排饼图'''
		self.assertEqual(a[0]['name'],'价格')
		self.assertEqual(a[1]['name'],'资讯')
		self.assertEqual(a[2]['name'],'短信')
		self.assertEqual(a[3]['name'],'期货')
		self.assertEqual(a[4]['name'],'供求')
		self.assertEqual(a[0]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/price.png')
		self.assertEqual(a[1]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/zixun.png')
		self.assertEqual(a[2]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/sms_free.png')
		self.assertEqual(a[3]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/qihuo.png')
		self.assertEqual(a[4]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/gq.png')

		'''首页第二排饼图'''
		self.assertEqual(b[0]['name'],'钢铁')
		self.assertEqual(b[1]['name'],'原料')
		self.assertEqual(b[2]['name'],'有色')
		self.assertEqual(b[3]['name'],'农产品')
		self.assertEqual(b[4]['name'],'更多')
		self.assertEqual(b[0]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/01.png')
		self.assertEqual(b[1]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/09.png')
		self.assertEqual(b[2]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/02.png')
		self.assertEqual(b[3]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/04.png')
		self.assertEqual(b[4]['ico'],'http://img02.mysteelcdn.com/wz/uploaded/steelphone4/indexico/10.png')

		'''首页中部右侧-钢银指数'''
		self.assertEqual(c[0]['title'],'钢银·今日成交量')
		self.assertEqual(c[1]['title'],'钢银·城市周库存量')
		#self.assertEqual(c[2]['title'],'钢银·实时成交价')
		self.assertEqual(c[0]['url'],'https://zhushou.banksteel.com/a/#/data/msapp')
		self.assertEqual(c[1]['url'],'https://zhushou.banksteel.com/a/#/data/msapp/kucun')
		#self.assertEqual(c[2]['url'],'https://zhushou.banksteel.com/a/#/data/msapp/jiage')

		'''首页中部左侧-价格指数'''
		self.assertEqual(d[0]['name'],'钢材综合指数')
		self.assertEqual(d[1]['name'],'焦炭指数')
		self.assertEqual(d[2]['name'],'62%进口矿指数')
		self.assertEqual(d[0]['url'],'http://m.steelphone.com/app/map/index.html?zsoption=gczh_abs&UAlocal=1&zs=1#hqzs')
		self.assertEqual(d[1]['url'],'http://m.steelphone.com/app/map/index.html?zsoption=jiaotan&UAlocal=1&zs=1#hqzs')
		self.assertEqual(d[2]['url'],'https://m.steelphone.com/app/map/index.html?UAlocal=1&zs=1#hqzs')

if __name__ == '__main__':
	unittest.main()