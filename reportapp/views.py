from django.shortcuts import render

# Create your views here.
from accountapp.models import MyUser
from reportapp.models import Report_Data


def report_user(request, user1, user2):
    context = {}

    context['user1'] = user1
    context['user2'] = user2
    temp_user1 = MyUser.objects.filter(pk=user1)
    temp_user2 = MyUser.objects.filter(pk=user2)
    print(temp_user1, 'temp_user1테스트')
    print(temp_user2, 'temp_user2테스트')

    # report_submit = request.GET.get('report_submit', None)

    # if report_submit != None:
    #     print('자바스크립트로 실행중일까요0603')
    #     for temp1 in temp_user1:
    #         for temp2 in temp_user2:
    #             report_test = Report_Data.objects.filter(report_send_user=temp1, report_receive_user=temp2)
    #             if report_test:
    #                 print('그냥 넘어가욧')
    #                 pass
    #             else:
    #                 print('실행해욧')
    #                 model = Report_Data(report_send_user=temp1,
    #                                     report_receive_user=temp2,
    #                                     report_title=request.POST.get('report_subject'),
    #                                     report_detail=request.POST.get('report_data'))
    #                 model.save()
    #                 temp2.sos_report += 1
    #                 temp2.save()
    # print('이거는 실행이 가능한가1155')
    if request.method == "POST" and request.POST.get("report_submit"):
        print('실행되고 있을까요99000')
        for temp1 in temp_user1:
            for temp2 in temp_user2:
                print('실행해욧')
                model = Report_Data(report_send_user=temp1,
                                    report_receive_user=temp2,
                                    report_title=request.POST.get('report_subject'),
                                    report_detail=request.POST.get('report_data'))
                model.save()
                temp2.sos_report += 1
                temp2.save()

    return render(request, 'report_page.html', context)
