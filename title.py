from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
html = urlopen("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=58355126069&hvpone=&hvptwo=&hvadid=486458755421&hvpos=&hvnetw=g&hvrand=519482814099556793&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9061898&hvtargid=kwd-10573980&hydadcr=14453_2154373&gclid=CjwKCAiAl-6PBhBCEiwAc2GOVOwh6YyUJWB06I49ft4T5jOWaJ_8vZ1o_T8p91VnCjQWTxC62z788RoCeSkQAvD_BwE")
res = BeautifulSoup(html.read(),"html5lib")
print(res.prettify)
print(res.title)
print(res.find_all("a"))

