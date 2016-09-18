from django.shortcuts import render
 
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse
from django.template.response import TemplateResponse


# Create your views here.
def index(request):
	r  = requests.get("http://www.gsmarena.com/news.php3")

	data = r.text

	soup = BeautifulSoup(data,"html.parser")
	soup.prettify()
	mydivs = soup.find_all("nobr")

	names=[]
	for name in mydivs:
		names.append(name.getText())
	    

	return HttpResponse(names)