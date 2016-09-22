from __future__ import print_function
import mechanize
from BeautifulSoup import BeautifulSoup 



browser = mechanize.Browser()
browser.open('http://www.gsmarena.com')

browser.form = list(browser.forms())[0]
browser['sName']='iphone7'
response = browser.submit()

soup = BeautifulSoup(response)
div = soup.findAll('div', {"class":"makers"})

ul = div[0].findAll("ul")
li = ul[0].findAll("li")

a = li[0].find("a")



# for i,lis in enumerate(li):
    
#     txt = li[i].find("a")
#     # names = txt[0].findAll("span")

#     # print names[0].getText()
#     print txt['href']

response = browser.open(str(a['href']))
soup = BeautifulSoup(response)
div = soup.findAll('div', {"id":"specs-list"})

tables = div[0].findAll("table")

for i,table in enumerate(tables):
    th = tables[i].find("th")
    
    print (th.getText(),end="-")

    tr = tables[i].findAll("tr")

    for j,row in enumerate(tr):

        td = tr[j].findAll("td",{"class":"ttl"})
        try:
            try:
                a = td[0].find("a")
            except:
                pass                
            print (a.getText(),end='-')

        except AttributeError,IndexError:
            try:
                print(td[0].getText())
            except:
                pass                

        nfo = tr[j].findAll("td",{"class":"nfo"})
        try:
            a = nfo[0].find("a")
            print (a.getText())

        except AttributeError:
            print(nfo[0].getText())
        except:
            pass            

    


