'''在水木上看到有人在问到想用python去获取股票的信息，sina finance上面的那些数据的是通过js控制的，会根据股票代码去获取实时信息然后根据用户友好的方式展示出来。
首先，新浪的一个url让我们可以获取股票的信息：http://hq.sinajs.cn/?list=sh600000
然后，我简单写了个程序可以将其中有用的股票名称/当前价格/涨跌幅等信息提取出来。本来是不难的，只是在数字的处理和格式化输出这两方面，我还找了些资料看了下才实现了。
实现的输出如下：
—————————————————————
股票名称:超图软件   涨跌幅:2.07   最新价:22.73 
股票名称:浪潮信息   涨跌幅:-2.91  最新价:19.33 
股票名称:东软集团   涨跌幅:-3.93  最新价:10.52 
股票名称:涪陵电力   涨跌幅:0.0     最新价:11.31 
股票名称:中金黄金   涨跌幅:-2.01  最新价:22.41 
—————————————————————-
简单的代码实现如下：
#! /usr/bin/python3
# coding=utf-8

'''
Created on Nov 9, 2011

@author: 笑遍世界
”’

import urllib.request

def get_price(code):
       url = ‘http://hq.sinajs.cn/?list=%s’ % code
       req = urllib.request.Request(url)
#如果不需要设置代理，下面的set_proxy就不用调用了。由于公司网络要代理才能连接外网，所以这里有set_proxy…
       req.set_proxy(‘proxy.XXX.com:911′, ‘http’)
       content = urllib.request.urlopen(req).read()
       str = content.decode(‘gbk’)
       data = str.split(‘”‘)[1].split(‘,’)
       name = “%-6s” % data[0]
       price_current = “%-6s” % float(data[3])
       change_percent = ( float(data[3]) – float(data[2]) )*100 / float(data[2])
       change_percent = “%-6s” % round (change_percent, 2)
       print(“股票名称:{0} 涨跌幅:{1} 最新价:{2}”.format(name, change_percent, price_current) )

def get_all_price(code_list):
   for code in code_list:
       get_price(code)

code_list = ['sz300036', 'sz000977', 'sh600718', 'sh600452', 'sh600489']
get_all_price(code_list)

