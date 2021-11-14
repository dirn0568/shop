# import requests
from bs4 import BeautifulSoup
from django.contrib.sites import requests

from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from accountapp.models import MyUser


def main(request):
    context = {}
    html = []
    html2 = []
    html3 = []
    html4 = []

    for i in range(1, 4):
        url = "https://www.jobkorea.co.kr/GoodJob/Tip?schCtgr=0&TipKwrdArray=%EC%95%8C%EB%B0%94%EC%83%9D&TipKwrdArray=%EC%B7%A8%EC%A4%80%EC%83%9D&TipKwrdArray=%EC%83%81%EC%8B%9D%ED%80%B4%EC%A6%88&TipKwrdArray=%EC%A7%81%EC%9E%A5%EC%9D%B8&TipKwrdArray=%EC%A0%84%EC%97%AD%ED%95%99%EA%B5%90&TipKwrdArray=%EC%A0%95%EB%B3%B4&TipKwrdArray=%EA%B5%AC%EC%A7%81%EC%9E%90&TipKwrdArray=%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85&Page={}".format(i)
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")
        hrefs = soup.find("ul", attrs={"class": "joodJobList"}).find_all("li")
        for idx, href in enumerate(hrefs):
            image_href = href.a["href"]
            if idx <= 2 and i == 1:
                html.append([image_href])
                html2.append([image_href])
            elif i == 1:
                html2.append([image_href])
            elif i == 2:
                html3.append([image_href])
            elif i == 3:
                html4.append([image_href])

        images = soup.find_all("p", attrs={"class":"thumb"})
        for idx, image in enumerate(images):
            image_url = image.find("img")["src"]
            image_text = image.find("img")["alt"]
            if idx <= 2 and i == 1:
                html[idx].append(image_url)
                html[idx].append(image_text)
                html2[idx].append(image_text)
            elif i == 1:
                html2[idx].append(image_text)
            elif i == 2:
                html3[idx].append(image_text)
            elif i == 3:
                html4[idx].append(image_text)
    context["html"] = html
    context["html2"] = html2
    context["html3"] = html3
    context["html4"] = html4
    return render(request, 'main.html', context)