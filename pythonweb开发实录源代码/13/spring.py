from xml.dom.minidom import Document
# ����һ��DOM�ṹ
doc = Document()
# ����һ����Ԫ�ء�����ʫ�䡱
wml = doc.createElement("����ʫ��")
doc.appendChild(wml)
# �ڸ�Ԫ�ء�����ʫ�䡱�������Ԫ�ء����족
maincard = doc.createElement("����")
maincard.setAttribute("id", "main")
wml.appendChild(maincard)
#����Ԫ�ء����족������ӽڵ㡰ӽ����
paragraph1 = doc.createElement("ӽ��")
maincard.appendChild(paragraph1)
#���ӽڵ㡰ӽ���������˵��
ptext = doc.createTextNode("����ױ��һ���ߣ�����������˿��")
paragraph1.appendChild(ptext)
#����Ԫ��"����"������ӽڵ㡰��԰��ֵ��
paragraph1 = doc.createElement("��԰��ֵ")
maincard.appendChild(paragraph1)
#���ӽڵ㡰��԰��ֵ�������˵��
ptext = doc.createTextNode("��ɫ��԰�ز�ס��һ֦���ӳ�ǽ��")
paragraph1.appendChild(ptext)
#����Ԫ�ء����족������ӽڵ㡰���ա�
paragraph1 = doc.createElement("����")
maincard.appendChild(paragraph1)
#���ӽڵ㡰���ա������˵��
ptext = doc.createTextNode("����ʶ�ö����棬����ǧ�����Ǵ�")
paragraph1.appendChild(ptext)
# ��ӡ���XML�ļ��е�����
print doc.toprettyxml(indent=" ")
