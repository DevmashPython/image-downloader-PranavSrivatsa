import re
import urllib


url="http://www.pogo.com/"
a=urllib.urlopen(url)
b=a.read()


p=re.compile('<img [^>]*src="([^"]*)"[^>]*>')
c=re.findall(p,b)


f=open("ImgUrls.txt","w")
for item in c:
	f.write("%s\n" % item)
f.close()
print "\n"+"Urls successfully obtained"