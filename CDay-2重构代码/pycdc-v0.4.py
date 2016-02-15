#coding=utf-8

import sys,cmd
from cdtools import *

class PyCDC(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)  #initalize the base class
		self.prompt = ">" # define the prompt
	def help_EOF(self):
		print "退出程序 Quit the program"
	def do_EOF(self,line):
		sys.exit()
	def help_walk(self):
		print "扫描光盘内容 walk cd and export into *.cdc"
	def do_walk(self,filename):
		if filename=="": filename = raw_input("输入cdc文件名::")
		print "扫描光盘内容到: '%s' " %  filename
	
	def help_dir(self):
		print "指定保存/搜索目录"
	def do_dir(self,pathname):
		if pathname == "": pathname = raw_input("输入指定保存/搜索目录:")





if __name__=='__main__':
	cdc=PyCDC()
	cdc.cmdloop()
	CDROM='/exam'
	cdWalker(CDROM,'cdctools.cdc')

