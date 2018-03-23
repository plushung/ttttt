import xml.sax
"""
python parse xml with sax
sax :event diver,
"""
class mhander(xml.sax.ContentHandler):
    def __init__(self):
        self.curTag=""
        self.ass='';
        self.pss='';
        self.eleCount=0;
    def startDocument(self):##开始读取xml文档时调用##
        print("star Document")
    def endDocument(self):##开始读取xml文档时调用##
        print("end Document")
    def startElement(self,tag,attrs):
        self.curTag=tag;
        if tag=='movie':
            self.ass=attrs["ax"];
            self.pss=attrs['ps'];
            self.prints()
            
    def endElement(self,tag):
        self.eleCount=self.eleCount+1;
        print("read end element : %d ;name : %s"%(self.eleCount,tag))
        
    def characters(self,cont):
        cont=cont.strip()
        print("%s :%s"%(self.curTag,cont))
        
    def prints(self):
        strs="as is %s ,ps is %s "%(self.ass,self.pss)
        print(strs)
han=mhander()
xml.sax.parse('tx.xml',han);

