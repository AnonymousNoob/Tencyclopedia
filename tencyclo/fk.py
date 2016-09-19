 
from bs4 import BeautifulSoup
import requests
import string
import operator


#url = input("website :")

gsm  = requests.get("http://www.gsmarena.com/news.php3")
nine  = requests.get("http://www.91mobiles.com/top-10-mobiles-in-india")#hover_blue_link name gaclick
digit  = requests.get("http://www.digit.in/top-products/best-android-phones-2.html")#swProdcutName

gsm_data = gsm.text
nine_data = nine.text
digit_data = digit.text


gsm_soup = BeautifulSoup(gsm_data,"html.parser")
gsm_soup.prettify()

nine_soup = BeautifulSoup(nine_data,"html.parser")
nine_soup.prettify()

digit_soup = BeautifulSoup(digit_data,"html.parser")
digit_soup.prettify()



#print(gsm_soup.prettify())

try:
    mydivs = gsm_soup.find_all("nobr")
    nine_names = nine_soup.find_all("a",{"class":"hover_blue_link name gaclick"})
    digit_names = digit_soup.find_all("a",{"class":"swProdcutName"})

    mydivs = [w.replace('(2016)', '') for w in mydivs]
    
    digit_names = [w.replace('(2016)', '') for w in digit_names]
    
    prods = []
    prodDic = {}
    prodDic1 = {}
    prodDic2 = {}

    for i,mobs in enumerate(mydivs):
        print(mobs.getText())
        mob = mobs.getText()
        prods.append(mob)

       
        
        if mob in prodDic:
            prodDic[mob] = prodDic[mob]+i
        else:            
            prodDic[mob]=i

    print("91")
    for i,names in enumerate(nine_names):
        print(names.getText())
        mob = names.getText()
        prods.append(mob)

        
        
        if mob in prodDic:
            prodDic[mob] = prodDic[mob]+i
        else:            
            prodDic[mob]=i



    print("digit")
    for i,names in enumerate(digit_names):
        print(names.getText())        
        mob = names.getText()
        prods.append(mob)

        if mob in prodDic:
            prodDic[mob] = prodDic[mob]+i
        else:            
            prodDic[mob]=i

        
except:
    pass

print(prods)


prods = [w.replace('16GB', '') for w in prods]
prods = [w.replace('32GB', '') for w in prods]
prods = [w.replace('(2016)', '') for w in prods]

prods = sorted(prods, key = prods.count, reverse=True)
"""
for name in prods:
    print(name," ",prods.count(name))
"""
prodDic = sorted(prodDic.items(), key=operator.itemgetter(1))

for names in prodDic:
    print(names)

