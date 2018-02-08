import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
filename="olx.txt"
f=open(filename,"w")

for k in range(1,501):
    my_url = "https://www.olx.com.gt/nf/all-results-p-"
    my_url=my_url + repr(k)
    uClient=uReq(my_url)
    page_html=uClient.read()
 
    page_soup=soup(page_html,"html.parser")
    page_soup.body
    containers=page_soup.findAll("li",{"class":"item"})
    container=containers[0]
    ##print(len(containers))
    ##print(container.div.h3)
    for container in containers:
        title=container.div.h3.text
        price=container.findAll("p",{"class":"items-price"})
        fecha=container.findAll("p",{"class":"items-date"})
        line=title.strip() + "|" + price[0].text.strip() + "|" + fecha[0].text.strip()+ "\r\n"
        line = re.sub('[ \t\n]+' , ' ', line)
        line = ' '.join(filter(None,line.split(' ')))
        f.write(line)
    print(k)
	uClient.close
print("close")
f.close()
