from django.http import HttpResponse
from django.shortcuts import render
from . import naver_api_exe_mod

# Create your views here.


def index(request):
    return render(request, 'index.html', {})

def naver_api(request):
    if request.method=="POST":
        client_id = request.POST['client_id']
        client_secret = request.POST['client_secret']
        naver_search = request.POST['naver_search']
        naver_search_num = request.POST['naver_search_num']

        result_json = naver_api_exe_mod.parsing(client_id, client_secret, naver_search, naver_search_num)


        result_list=[]
        for item in result_json['items']:
            temp = {}
            temp['title'] = item['title']
            temp['link'] = item['link']
            result_list.append(temp)

        return render(request, 'result.html', {'result_list': result_list})
    else:
        return render(request, 'naver_api.html', {})