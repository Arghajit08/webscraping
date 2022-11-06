from cgitb import html
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
import json

def home(request):
    url="https://tripurapolice.gov.in/WantedCriminal"
    r=requests.get(url)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    print(soup.prettify)
    x=soup.find_all('section')
    print(len(x))
    l=x[1].tbody
    l1=l.find_all("tr")
    b=len(l1)
    arr=[]
    temp=[]
    for i in range(b):
        l2=l1[i].find_all('td')
        temp.append(l2[0].a['href'])
        temp.append(l2[1].a['href'])
        temp.append(l2[1].a.string)
        temp.append(l2[2].string)
        temp.append(l2[3].string)
        temp.append(l2[4].string)
        arr.append(temp)
        temp=[]
    print(arr)

    m=len(x)
    print(m,b)
    return render(request,"index.html",context={"len_json":json.dumps(arr)})


def result(request):
    link=request.GET['link1']
    r=requests.get(link)
    htmlcontent=r.content
    soup=BeautifulSoup(htmlcontent,'html.parser')
    print(soup.prettify)
    return render(request,"index1.html")
# Create your views here.
