#-*-coding:UTF-8 -*-
#Python模板
print "===========欢迎使用窗内网网站流量统计下载系统===========";
yn=int(raw_input("您确定要下载吗？1:表示是,2:表示否！"));
if yn==1:
	files=raw_input("请输入您需要下载的本地地址");
	o=open(files+'\\files.doc','w');
	print "正在下载中，请稍后......";
	o.write('【昨天】中访问量：25624，独立访客：21301，独立IP：19813【今天】中访问量：12453，独立访客：11523，独立IP：11210');
	o.close();
	print "下载完成请查阅！"
else:
	print "欢迎使用，希望下次在来！";