#!D:/Program Files/Python/python.exe
reshtml="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>����CGI</title>
<style>
.bg{
	background-image:url(/img/http_imgload12.jpg);
	background-repeat:no-repeat;
	width:600px;
	height:450px;	
}
.bground{
	padding-left:90px;
	padding-top:40px;}
body,td,th {
	font-size: 16px;
}
</style>
</head>
<body class="bg">

<div class="bground">
<h3>�����ѵĶ��ٿ��Բ�����Ժ������:<I>������</I></h3>
<form action="friend.py">
<B>������������:</B>
<input name="person" value="" size="15"/>
<p><B>���ж��ٸ����ѣ�</B></p>
<input  type="radio" name="howmany" value="0" checked="checked"/>�Һ�լ��û������<br /><br />
<input  type="radio" name="howmany" value="10" />�Ҳ��ó����ʣ���ֻ��10�����ѣ�������֪�ĵ�Ŷ<br /><br />
<input  type="radio" name="howmany" value="23" />����Ϊ����ɣ���23������
<br /><br />
<input  type="radio" name="howmany" value="50" />�Һܺ�Ŷ����������50�������
<br /><br />
<input  type="radio" name="howmany" value="100" />����Ե�غã���������100�����ѣ��Գ����������
<p align="center"><input  type="submit" value=" �� �� "/></p>

</form>
</div>
</body>
</html>
"""
print reshtml
