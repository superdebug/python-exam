import string
from xml.sax import*
class QuotationHandler(ContentHandler):
    def __init__(self):
        self.string=''    
    def startDocument(self):		#��ʼ�����ĵ�ʱ����
        print '-------��ʼ����XML�ĵ�------'
        print 'name\tprice\taffect'
        print '--------------------------'
    def endDocument(self):					#�����ĵ�����ʱ����
        print '-------�������XML�ĵ�-'

    nameStr=raw_input('����������鿴XML�ĵ��еı�ǩ��title����')    
    def startElement(self, nameStr, attrs):
        print '-----------Start Element-----------'
        if nameStr == 'title':
            print '------��ǩΪtitle�µ�����-------'                     
            print attrs['name'],attrs['offer_id'],attrs['mobile_url']              
    def characters(self, ch):        
        self.string = self.string + ch
if __name__ == '__main__':   
    try:
        parser =make_parser()
        handler = QuotationHandler()
        parser.setContentHandler(handler)
        parser.parse("sample.xml")
    except:
        import traceback
        traceback.print_exc()
    
       
