from xml.dom.minidom import *
root=parse('shangji.xml')

def traverSal (node):
	if not node.childNodes:
		return
	for child in node.childNodes:
		print child
		traverSal(child)
print '---------XML�ĵ�ȫ����ʾ��Ч��-----------'
print traverSal(root)
print '-----------��ѯXML�ĵ���Ч��------------'
names= root.getElementsByTagName("Name")
for name in names:
	print name.toxml()

print '-----------��XML�ĵ������ӽڵ�--------------'
goods=root.createElement('goods')
tests=root.createElement('tests')
text=root.createTextNode('food is my best')
tests.appendChild(text)
goods.appendChild(tests)
print goods.toxml()

print '---------��XML�ĵ���ɾ���ڵ�-----------'
#goods.removeChild(tests)
#print goods.toxml()
print '----------�滻XML�ĵ��еĽڵ�------------'	
ceshi=root.createElement('ceshi')
text=root.createTextNode('wo shi ceshi')
ceshi.appendChild(text)
goods.replaceChild(ceshi,tests)
print goods.toxml()
