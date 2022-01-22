import requests
from bs4 import BeautifulSoup


from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from accountapp.models import MyUser
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
            temp_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
            temp_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)

            # field_list = request.POST.getlist('work2')
            # print(field_list)

            answer = []
            answer.append(resume_title)
            answer.append(resume_title.resume_title_detail)
            answer.append(resume_title.resume_date)

            school1 = Resume_ElementarySchool.objects.filter(resume_elementary=resume_title)
            school2 = Resume_MiddleSchool.objects.filter(resume_middle=resume_title)
            school3 = Resume_HighSchool.objects.filter(resume_high=resume_title)
            school4 = Resume_UniversitySchool.objects.filter(resume_university=resume_title)

            major = Resume_UniversitySchool_Major.objects.filter(resume_university_major=resume_title)

            if school1.count() >= 1:
                for temp in school1:
                    answer.append(temp.elementary_school_name)
            if school2.count() >= 1:
                for temp in school2:
                    answer.append(temp_resume.middle_school_name)
            if school3.count() >= 1:
                for temp in school3:
                    a = temp.high_school_name
                    b = temp.high_major
                c = a + '(' + b + ')'
                answer.append(c)
            if school4.count() >= 1:
                for temp in school4:
                    a = temp.university_school_name
                if major.count() >= 1:
                    for temp in major:
                        b = temp.resume_university_major_detail
                        break
                print('이거샐행중국??????')
                c = a + '(' + b + ')'
                answer.append(c)

            hope_money = Resume_Hope_Work.objects.filter(resume_hope_work=resume_title)
            for hope in hope_money:
                answer.append(hope.resume_hope_work_money)

            hope_field = Resume_Hope_Work_Field.objects.filter(resume_hope_work_field=resume_title)
            for hope in hope_field:
                answer.append(hope.resume_hope_work_field1)
            hope_work = Resume_Hope_Work_Work.objects.filter(resume_hope_work_work=resume_title)
            for hope in hope_work:
                answer.append(hope.resume_hope_work_work1)

            answer_list.append(answer)

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