import requests,sys
class Dlitem():
    def __init__(self,link,lidx):
        self.link = link
        self.lidx=lidx
        self.flen=0
        self.csize=512*1024
        self.dlen=0
        self.strt=0
        self.filename="dlitem"
        self.checkurl(self.link)
        self.setfilename()

    def checkurl(self,url):
        try:
            r=requests.head(url)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
        else:
            # print(r.headers)
            if 'Location' in r.headers.keys():
                self.checkurl(r.headers['Location'])
            # print(r.headers['Location'])
            else:
                # print(r.url,r.headers['content-length'])
                self.link=str(r.url)
                self.flen=r.headers['content-length']

    def setfilename(self):
        temp=self.link.split("/")[-1]
        if len(temp)>100:
            temp=temp[:100]
        temp=temp.split("?")[0]
        self.filename=temp