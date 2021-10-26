from urllib.request import urlopen
from bs4 import BeautifulSoup

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from accountapp.models import MyUser


def main(request):
    html2_text = []
    html2_img = []
    html2_href = []
    html2 = []
    html = urlopen("https://news.naver.com/")
    bsObject = BeautifulSoup(html, "html.parser")
    # for link in bsObject.find_all('img'):
    #     # if link.text.strip().count('기사') >= 1:
    #     html2_img.append(link.get('src'))
    # for link in bsObject.find_all('a'):
    #     if bsObject.find_all('img') >= 1:
    #         html2_text.append(link.text.strip())
    #         html2_href.append(link.get('href'))
    # for link in bsObject.find_all('img'):
    #     for link2 in bsObject.find_all('a'):
    #         if link2.text.strip().count('기사') >= 1:
    #             html2_text.append(link2.text.strip())
    #             html2_img.append(link.get('src'))
    #             html2_text.append(link2.get('href'))
        # print(link.text.strip(), link.get('href'))
    for link in bsObject.select('기사'):
        html2_href.append(link.get('href'))
    context = {}
    print(html2_text, '####################################')
    print(html2_img, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(html2_href, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    context['html2_text'] = html2_text
    context['html2_img'] = html2_img
    context['html2_href'] = html2_href
    return render(request, 'main.html', context)