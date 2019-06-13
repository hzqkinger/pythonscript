#! /bin/python2
#! coding:utf-8

# 1,指定解释器(且上面的东西必须写在前面，在中间插入注释都不行)
# 2,指定编码，否则可能不允许出现中文

import requests

# 一，下面爬取的是百度首页的信息############入门级####################################################################################
# url = "http://www.baidu.com"
# try:
# 	r = requests.get(url)
# 	r.raise_for_status()
# 	print(r.status_code)
# 	print(r.encoding)
# 	print(r.apparent_encoding)
# 	print(type(r))
# 	print(r.request.headers)
# 	r.encoding = r.apparent_encoding
# 	print(r.text[:1000])
# except:
# 	print("ssssssssssss")

# 二，假如有的网页仅仅只是限制爬虫去访问，那么可以把header中的user-agent字段改成某浏览器#############################################
# url = "http://www.baidu.com"
# try:
# 	# kv = {'user-agent':'SSSSSS'}   #好像这个东西可以瞎改，并不会影响什么
# 	kv = {'user-agent':'Mozilla/5.0'}
# 	r = requests.get(url,headers=kv)
# 	r.raise_for_status()
#  	print(r.status_code)
#  	print(r.encoding)
#  	print(r.apparent_encoding)
#  	print(r.request.headers)
# 	r.encoding = r.apparent_encoding
# 	print(r.text[:1000])
# except:
# 	print("ssssssssssss")

# 三，如何向百度。360提交关键字请求#################################################################################################
# 百度的关键词提交接口  http://www.baidu.com/s?wd=keyword
# 360的关键词提交接口  http://www.so.com/s?1=keyword
# try:
# 	# kv = {'wd':'我想提交的关键字'}
# 	kv = {'wd':'Python'}
# 	r = requests.get("http://www.baidu.com/s",params=kv);
# 	print(r.request.url)
# 	r.raise_for_status()
# 	print(len(r.text))
# except:
# 	print("爬取失败")

# 四，网络图片的爬取和存储 ###################################################################################
# url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1556537787621&di=77ac4a59f97a29bb6427845fa4974587&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farchive%2F0e5b2523e5b1721df6ad760a063fd4c892c52116.jpg"
# # url = "https://f10.baidu.com/it/u=69828466,1848654465&fm=72" #这张是广告图片，所以网址不像上面的
# path = "./abf.jpg"
# r = requests.get(url)
# print(r.status_code)
# with open(path,'wb') as f:
# 	f.write(r.content)
# 	f.close()
##############################
# import os
# url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1556537787621&di=77ac4a59f97a29bb6427845fa4974587&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farchive%2F0e5b2523e5b1721df6ad760a063fd4c892c52116.jpg"
# root =  "./pics/"
# path = root + url.split('/')[-1]
# try:
# 	if not os.path.exists(root):
# 		os.mkdir(root)
# 	if not os.path.exists(path):
# 		r = requests.get(url)
# 		with open(path,'wb') as f:
# 			f.write(r.content)
# 			f.close()
# 			print("文件保存成功")
# 	else:
# 		print("文件已存在")
# except:
# 	print("爬取失败")

# 五，网络视频的爬取和存储    (和第四个类似)########################################################################################
# url = "http://183.222.142.237/67734B8A61D3F71990A8A3E2E/03000A01005CC2BA1622D7C449DA9D71414EAF-243B-41FD-8C4E-6A4F811F8A4F.mp4?ccode=050F&duration=10&expire=18000&psid=d45f83888fffc8e1af6ef6b95f3f969e&ups_client_netip=6f132d8e&ups_ts=1556530975&ups_userid=&utid=8tkEFeuXD1kCAd4ZKQozMvGT&vid=XNDE1NDk1NTU3Mg%3D%3D&vkey=Aa18cc7d9761ce305f03504ece4bc0453&sp=&ali_redirect_domain=ykugc.cp31.ott.cibntv.net&ali_redirect_ex_ftag=9df3c60778f041025821648fb3b5d1310d0213785600c38f&ali_redirect_ex_tmining_ts=1556531125&ali_redirect_ex_tmining_expire=3600&ali_redirect_ex_hot=0"
url = "http://pgc.cdn.xiaodutv.com/2764761133_946245062_2019032104141120190321043429.mp4?Cache-Control=max-age%3D8640000&responseExpires=Sat%2C+29+Jun+2019+04%3A34%3A43+GMT&xcode=551c5f53e3e8142df548b06dfccd28a8ef931a7d1bd2657f&time=1556724236&_=1556637849966"
url = "ftp://ygdy8:ygdy8@yg45.dydytt.net:7445/阳光电影www.ygdy8.com.我们.BD.720p.中英双字幕.mkv"
path = "./我们.mkv"
r = requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
	f.write(r.content)
	f.close()

# 六，用代码模拟 在某网站手动提交东西的过程 （以http://www.ip138.com/ 该网站查询ip地址为例）##############################
# url = "https://www.ip138.com/ips1388.asp"
# kv = {
# 	'ip':'202.204.80.112',
# 	'actioon':'2'
# }
# try:
# 	#r = requests.get(url+'?ip=202.204.80.112&action=2')
# 	r = requests.get(url,params=kv)
# 	print(r.request.url)
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	print(r.text[-500:])
# except:
# 	print("爬取失败")
