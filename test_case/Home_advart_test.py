#coding:utf-8
import unittest
import requests
import json
import time,re
class AdvArrayArticleTest(unittest.TestCase):
	'''首页：顶部广告、文章、榜单'''
	def setUp(self):
		self.base_url = "https://mysteelapi.steelphone.com/v4/getAdvArrayArticle.htm?"

	def tearDown(self):
		#print(self.result)
		pass
	"""
	def test_AdvArrayArticle_null(self):
		'''广告参数为空'''    #首页顶部广告有5分钟缓存
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,1','page':'1','type':',17,6','protocolVersion':'4.6.5'})
		self.result = r.json()
		advs = self.result['advArray'][0]['adv']
		print(advs)
		self.assertEqual(advs,[])
	
	def test_AdvArrayArticle_null(self):
		'''广告参数错误'''
		r = requests.get(self.base_url,params = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,1','page':'1','type':'2,17,6','protocolVersion':'4.6.5'})
		self.result = r.json()
		advs = self.result['advArray'][0]['adv']
		print(advs)
		self.assertEqual(advs,[])
	"""
	
	def test_get_adv_success(self):
		'''顶部广告获取成功'''
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,1','page':'1','type':'5,17,6','protocolVersion':'4.6.5'}
		r = requests.get(self.base_url,params = payload)
		self.result = r.json()
		#print(self.result)
		#print(self.result['advArray'][0]['adv'])
		advs = self.result['advArray'][0]['adv']
		#print(advs)
		
		'''固定广告位置'''
		for adv in advs:
			#print(adv)
			if adv['id'] == '3448':
				adv0 = adv
				#print(adv0)
			elif adv['id'] == '3460':
				adv1 = adv
				#print(adv1)
			else:
				adv2 = adv
				#print(adv2)
		
		#顶部广告1
		self.assertEqual(adv0['id'],'3448')     #广告id
		self.assertEqual(adv0['title'],'天津友发钢管集团股份有限公司')   #广告标题
		self.assertEqual(adv0['description'],'5')   #广告位置
		self.assertEqual(adv0['src'],'http://www.yfgg.com/?hmsr=mystealSY&hmmd=&hmpl=&hmkw=&hmci=')   #广告跳转地址
		self.assertEqual(adv0['type'],'1')   #广告的频道id
		self.assertEqual(adv0['url'],'http://mfs.mysteelcdn.com/group1/M00/06/F4/rBL63lrxE6WAZr6JAABun6BtIBw900.jpg')   #广告图片路径

		#顶部广告2
		self.assertEqual(adv1['id'],'3460')     #广告id
		self.assertEqual(adv1['title'],'河南鹏达金属制品有限公司')   #广告标题
		self.assertEqual(adv1['description'],'5')   #广告位置
		self.assertEqual(adv1['src'],'')   #广告跳转地址
		self.assertEqual(adv1['type'],'1')   #广告的频道id
		self.assertEqual(adv1['url'],'http://mfs.mysteelcdn.com/group1/M00/05/AC/rBL63lqmZIiARpQaAACM3Lmobzc324.jpg')   #广告图片路径

		#顶部广告3
		self.assertEqual(adv2['id'],'3521')     #广告id
		self.assertEqual(adv2['title'],'晋城福盛钢铁有限公司')   #广告标题
		self.assertEqual(adv2['description'],'5')   #广告位置
		self.assertEqual(adv2['src'],'http://www.steelphone.com/jingang.html')   #广告跳转地址
		self.assertEqual(adv2['type'],'1')   #广告的频道id
		self.assertEqual(adv2['url'],'http://mfs.mysteelcdn.com/group1/M00/06/F4/rBL63lrxEuyATLOwAACAiJXFgRc261.jpg')   #广告图片路径

	def test_get_art_null(self):
		'''首页文章页码参数为空'''
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'','type':'5,17,6','protocolVersion':'4.6.5'}
		r = requests.get(self.base_url,params = payload)
		#self.result = r.json()
		code = r.status_code
		#print(self.result)
		self.assertEqual(code,400)
	
	def test_get_art_error(self):
		'''首页文章页码参数传入错误，大于100'''
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'101','type':'5,17,6','protocolVersion':'4.6.5'}
		r = requests.get(self.base_url,params =payload)
		self.result = r.json()
		#print(len(self.result))
		self.assertEqual(len(self.result),1)    
	

	def test_get_artfirst_success(self):
		'''首页文章第1页：榜单-好文推荐、文章排序和条数'''
		payload = {'userId':'566453','machineCode':'2ACCCCDC5FBDBE59ADD70F1C100FE4BB','id':',,2','page':'1','type':'5,17,6','protocolVersion':'4.6.5'}
		r = requests.get(self.base_url,params = payload)
		rbd = requests.get('http://mysteelapi.steelphone.com/v4/article/queryBillBoard.htm?&userId=566453&page=1&size=15&isPad=')   #榜单-好文推荐
		self.result = r.json() #首页文章
		self.resultbd = rbd.json()  #好文推荐
		#print(self.resultbd)

		#===============断言榜单-好文推荐==============
		bdlist = []      #首页榜单列表
		bddlist = []     #榜单页列表

		#获取首页榜单文章id
		for art in self.result['articles']:     
			if len(art['articlePicArray']) != 0:
				bd = art['articlePicArray']
				#print(bd)
				for bdid in bd:
					#print(len(bdid))
					bdlist.append(bdid['id'])
				#print(bdlist)

		#获取榜单详细页文章id
		for artbd in self.resultbd['articles']:   
			bddlist.append(artbd['id'])
		#print(bddlist)

		for l in range (5):
			bo = int(bdlist[l]) - int(bddlist[l])   
			#print(bo)
			self.assertEqual(bo,0)   #断言首页榜单文章为榜单详细页前五篇文章

		#====================断言非置顶文章降序排序和条数===================
		tm = []
		zd = 0
		r = time.strftime('%Y%m%d',time.localtime(time.time()))  #获取当前时间年、月、日
		y = time.strftime('%Y',time.localtime(time.time()))   #获取当前时间年
		#print(s)

		for art in self.result['articles']:
			#print(art['date2'])
			#print(art)
			i = re.findall(r"\d+\.?\d*",art['date2'])   #提取字符串中的数据
			j = (('').join(i))  #将列表转换为字符串
			#print(j)
			
			#若只显示时、分则时间格式转换为年月日时分
			if art['isTop'] == 'false':
				if len(j) == 4: 
					j = r + j     
					#print(j)
				elif len(j) == 8:
					j = y + j
				tm.append(j)
			#置顶文章数量
			elif art['isTop'] == 'true':
				zd = zd + 1  
		#print(tm)
		for k in range (len(tm)-1):
			bo = int(tm[k])-int(tm[k+1]) 
			self.assertEqual(bo>=0,True)   #断言降序排序
			
		#self.assertEqual(zd+len(tm),15)   #断言每页15条数据
	
if __name__ == '__main__':
	unittest.main()
