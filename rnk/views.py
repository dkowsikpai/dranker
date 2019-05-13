from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
# from django.views.decorators.csrf import csrf_exempt
import re
import csv
# Create your views here.
def login(request):
    return render(request, 'acc/loginpg.html')
#


def authen(request):
    username = request.POST['ucode']
    password = request.POST['pcode']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        return HttpResponse('/home/')
    else:
        return HttpResponse("Check username and password")

def extmrk(i):
    try:
        mrk = round(list(map(float, re.findall(r'\d+', str(i))))[0], 3)
    except IndexError:
        mrk = 0
    return mrk


def home(request):
    return render(request, 'home/home.html')


def dload(request):
    scode = str(int(extmrk(request.POST['scode'])))
    return HttpResponse('media/csv/'+scode+'.csv')

def printw(request):
    data = request.POST['d']
    std = []
    scode = str(int(extmrk(request.POST['scode'])))
    print(scode)
    # print(data)
    #data = data.strip(' ')
    data = data.replace(u'\xa0', ' ')
    data = data.split('-!-')
    # f = open('temp1.txt', 'w')
    for i in data[:-1]:
        i = i.split('\n')
        dic = {}

        dic['regno'] = int(i[1].strip(' '))
        dic['name'] = i[2].strip(' ')
        dic['bth'] = i[3].strip(' ')
        dic['s1'] = extmrk(i[4])
        dic['s2'] = extmrk(i[5])
        dic['s3'] = extmrk(i[6])
        dic['s4'] = extmrk(i[7])
        dic['s5'] = extmrk(i[8])
        dic['s6'] = extmrk(i[9])
        dic['tot'] = float(dic['s1'] + dic['s2'] + dic['s3'] + dic['s4'] + dic['s5'] + dic['s6'])
        dic['percent'] = round(dic['tot'] / 12, 3)
        dic['result'] = i[10].strip(' ')
        # print(dic)
        std.append(dic)
    sortstd = sorted(std, key=lambda dic: dic['tot'], reverse=True)
    # for i in sortstd:
    #     f.write(str(i))
    # print(sortstd)
    rank = 1
    for dic in sortstd:
        dic['rank'] = rank
        rank += 1
    csv_columns = ['rank', 'regno', 'name', 'bth', 's1', 's2', 's3', 's4', 's5', 's6', 'tot', 'percent', 'result']
    with open('media/csv/'+scode+'.csv', 'w') as output:
        writer = csv.writer(output)
        writer = csv.DictWriter(output, fieldnames=csv_columns)
        writer.writeheader()
        for data in sortstd:
            writer.writerow(data)  # Writing to CSV

    # f.close()
    return HttpResponse("Success")