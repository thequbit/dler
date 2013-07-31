import urllib
import urllib2
from time import strftime
from random import randint

class DLer:

    def _fileexists(self,filename):
        exists = False
        if filename == None:
            exists = False
        else:
            try:
                with open(filename):
                    exists = True
                    pass
            except:
                exists = False
        return exists

    def _gettime(self):
        isotime = strftime("%Y-%m-%d %H:%M:%S")
        return isotime

    def _download(self,url,dest):
        success = True
        try: 
            urlfile = url[url.rfind("/")+1:]
            rndpart = randint(0,1000000000000)
            _filename = "{0}/{1}{2}.download".format(dest,urlfile,rndpart)
            while self._fileexists(_filename):
                rndpart = randint(0,1000000000000)
                _filename = "{0}/{1}{2}.download".format(dest,urlfile,rndpart)
            print _filename
            filename,_headers = urllib.urlretrieve(url,_filename)
        except:
            filename = ""
            success = False
        datetime = self._gettime()
        return (filename,datetime,success)

    def dl(self,links,destdir):
        retsuccess = True
        files = []
        for _link in links:
            link,text = _link
            filename,datetime,success = self._download(link,destdir)
            if not success:
                retsuccess = False
                break
            else:
                files.append((filename,datetime))
        return (files,retsuccess)

