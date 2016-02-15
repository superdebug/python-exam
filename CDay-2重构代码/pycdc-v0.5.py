#coding=utf-8

import sys,cmd
from cdtools import *

class PyCDC(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)  #initalize the base class
		self.prompt = "(PYCDC)"   #定义提示符
		self.CDROM = '/exam'
		self.CDDIR = '/exam/cdc/'
		self.intro = ''' PYCDC 0.5 使用说明
		dir 目录名 #指定保存和搜索的目录 默认是"cdc"
		walk 文件名 #指定光盘信息，使用 *.cdc
		find 关键词 #使用在保存和搜索目录中遍历所有的cdc文件 输出含有关键词的行
		EOF #退出系统
		'''
	def help_EOF(self):
		print "退出程序 Quit the program"
	def do_EOF(self,line):
		sys.exit()
	def help_walk(self):
		print "扫描光盘内容 walk cd and export into *.cdc"
	def do_walk(self,filename):
		if filename=="":
			filename = raw_input("输入cdc文件名::")
		print "扫描光盘内容到: '%s' " %  filename
		cdWalker(self.CDROM,self.CDDIR+filename)	
	
	def help_dir(self):
		print "指定保存/搜索目录"
	def do_dir(self,pathname):
		if pathname == "": pathname = raw_input("输入指定保存/搜索目录:")


if __name__=='__main__':
	cdc=PyCDC()
	cdc.cmdloop()
	CDROM='/exam'
	cdWalker(CDROM,'cdctools.cdc')
