import requests
from bs4 import BeautifulSoup
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import MyUser
from profileapp.models import User_Profile
from resumeapp.models import Resume_Title, Resume_Hope_Work, Resume_Hope_Work_Field, Resume_Hope_Work_Work, \
    Resume_UniversitySchool, Resume_HighSchool, Resume_UniversitySchool_Major, Resume_MiddleSchool, \
    Resume_ElementarySchool


def main(request):
    # context = {}
    # list = []
    # resume_list = Resume_Title.objects.filter(resume_open=1)
    # for temp_resume in resume_list:
    #     list.append(temp_resume)
    # context['resume_list'] = resume_list

    context = {}
    temp_resume = Resume_Title.objects.all()
    answer_list = []
    school_list = []
    for resume_title in temp_resume:
        if resume_title.resume_open == 1:
            temp_profile = User_Profile.objects.filter(profile=resume_title.resume_title)
            answer = []
            for user_profile in temp_profile:
                if user_profile.user_name:
                    answer.append(user_profile.user_name)
                else:
                    answer.append("None")
                if user_profile.user_gender:
                    answer.append(user_profile.user_gender[:1])
                else:
                    answer.append("None")
                if user_profile.user_birthday:
                    now = datetime.now()
                    date = now.strftime("%Y")
                    date2 = user_profile.user_birthday[:4]
                    date3 = int(date) - int(date2)

                    date4 = now.strftime("%m")
                    date5 = now.strftime("%d")
                    date6 = user_profile.user_birthday[4:6]
                    date7 = user_profile.user_birthday[6:9]
                    date4 = int(date4)
                    date5 = int(date5)
                    date6 = int(date6)
                    date7 = int(date7)
                    if date4 > date6:
                        pass
                    elif date4 == date6 and date5 >= date7:
                        pass
                    else:
                        date3 = date3 - 1
                    answer.append(date3)
                else:
                    answer.append("None")
                if user_profile.profile_img:
                    answer.append(user_profile.profile_img)
                    print(user_profile.profile_img)
                else:
                    answer.append("None")

            temp_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)

            # field_list = request.POST.getlist('work2')
            # print(field_list)

            answer.append(resume_title)
            answer.append(resume_title.resume_title_detail)

            hope_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
            for hope in hope_work:
                answer.append(hope.resume_hope_work_work1)

            answer_list.append(answer)
    print(answer_list, "01-25")
    context['answer_list'] = answer_list
    context['school_list'] = school_list



    return render(request, 'main.html', context)
    # html = []
    # html2 = []
    # html3 = []
    # html4 = []
    #
    # for i in range(1, 4):
    #     url = "https://www.jobkorea.co.kr/GoodJob/Tip?schCtgr=0&TipKwrdArray=%EC%95%8C%EB%B0%94%EC%83%9D&TipKwrdArray=%EC%B7%A8%EC%A4%80%EC%83%9D&TipKwrdArray=%EC%83%81%EC%8B%9D%ED%80%B4%EC%A6%88&TipKwrdArray=%EC%A7%81%EC%9E%A5%EC%9D%B8&TipKwrdArray=%EC%A0%84%EC%97%AD%ED%95%99%EA%B5%90&TipKwrdArray=%EC%A0%95%EB%B3%B4&TipKwrdArray=%EA%B5%AC%EC%A7%81%EC%9E%90&TipKwrdArray=%EC%A4%91%EC%86%8C%EA%B8%B0%EC%97%85&Page={}".format(i)
    #     res = requests.get(url)
    #     res.raise_for_status()
    #     soup = BeautifulSoup(res.text, "lxml")
    #     hrefs = soup.find("ul", attrs={"class": "joodJobList"}).find_all("li")
    #     for idx, href in enumerate(hrefs):
    #         image_href = href.a["href"]
    #         if idx <= 2 and i == 1:
    #             html.append([image_href])
    #             html2.append([image_href])
    #         elif i == 1:
    #             html2.append([image_href])
    #         elif i == 2:
    #             html3.append([image_href])
    #         elif i == 3:
    #             html4.append([image_href])
    #
    #     images = soup.find_all("p", attrs={"class":"thumb"})
    #     for idx, image in enumerate(images):
    #         image_url = image.find("img")["src"]
    #         image_text = image.find("img")["alt"]
    #         if idx <= 2 and i == 1:
    #             html[idx].append(image_url)
    #             html[idx].append(image_text)
    #             html2[idx].append(image_text)
    #         elif i == 1:
    #             html2[idx].append(image_text)
    #         elif i == 2:
    #             html3[idx].append(image_text)
    #         elif i == 3:
    #             html4[idx].append(image_text)
    # context["html"] = html
    # context["html2"] = html2
    # context["html3"] = html3
    # context["html4"] = html4


def main2(request):
    context={}
    return render(request, 'main2.html', context)