#! /bin/python
#! coding utf-8

######################################################
#import requests
#r = requests.get("https://www.baidu.com")
#print(r.status_code)
#print(r.encoding)
#print(r.apparent_encoding)
#r.encoding = r.apparent_encoding
## print(r.text)
#
#demo = r.text
#from bs4 import BeautifulSoup
#soup = BeautifulSoup(demo,"html.parser")
# 1,漂亮的打印出来
# print(soup.prettify())

# 2,打印出所有的a标签
# print(soup.find_all('a'))
#
# for tag in soup.find_all('a'):
# 	print(tag)
# 
# for tag in soup.find_all('a','mnav'):
# 	print(tag)
# 

# 3,打印出所有标签的名字
# for tag in soup.find_all(True):
# 	print(tag.name)

######################################################
## 中国大学排名定向爬虫 的实例编写
#import requests
#from bs4 import BeautifulSoup
#import bs4
#
#url = 'http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type='
#r = requests.get(url) #先把这个网页爬取下来
#soup = BeautifulSoup(r.text,"html.parser") #再把这个网页变成soup类
## print(soup.prettify())
#
#ulist = []
#ulist.append(["排名","学校","分数","类别`"])
#for tr in soup.find('tbody').children: #找到tbody标签，打印她的所有孩子
#	if isinstance(tr,bs4.element.Tag):
#		tds = tr('td')
#		ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
#		print(tds[0].string)
#		print(tds[1].string)
#		print(tds[2].string)
#		print("{0:{1}^5}".format(tds[3].string,chr(12288)))
#
#print(ulist[0:])
#print(ulist)
#tplt = "{0:^5}\t {1:{4}^15}\t {2:^5}\t {3:^10}"
#for i in range(len(ulist)):
#	u = ulist[i]
#	print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))
#
######################################################
import requests
import re

def getHTMLText(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		print(t.text)
		return r.text
	except:
		print("get nothing")

def parsePage(ilt,html):
	try:
		plt = re.findall(r'\"p-price\"\:\"[\d.]*\"',html)
		tlt = re.findall(r'\"p-name\"\:\".*\?"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price,title])
	except:
		print(ilt)

def printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print(tplt.format("序号","价格","商品名称"))
	count = 0
	for g in ilt:
		count += 1
		print(tplt.format(count,g[0],g[1]))

def main():
	goods = '休闲运动鞋'
	depth = 2
	start_url = 'https://search.jd.com/search?keyword=' + goods + '&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=休闲运动鞋&cid2=11730'
	#start_url = 'https://search.jd.com/search?keyword=%E4%BC%91%E9%97%B2%E8%BF%90%E5%8A%A8%E9%9E%8B&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E4%BC%91%E9%97%B2%E8%BF%90%E5%8A%A8%E9%9E%8B&cid2=11730'
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&page='+ str(i+1) + '&s=' + str(27*i+1)
			print(url)
			html = getHTMLText(url)
			parsePage(infoList,html)
			print(len(infoList))
		except:
			continue
	printGoodsList(infoList)
main()
