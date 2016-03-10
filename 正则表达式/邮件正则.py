import re
text='aaa@163.com chu-tian-shu_1981@heibanke2015.com abc-fff@xfd.org ccc_fd2@fff.edu aaa@111 com'

print re.findall(r'(\w+[-\w]*)@([a-zA-Z0-9]+)\.(com|org|edu)',text)

print re.findall('(\w+[-\w]*)@([a-zA-Z0-9]+)\.(com|org|edu)',text)

print re.findall(r'\w+[-\w]*@[a-zA-Z0-9]+\.com|org|edu',text)


