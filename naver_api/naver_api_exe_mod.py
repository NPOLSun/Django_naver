
import urllib.request
import requests
from urllib.parse import urlparse

def parsing(client_id, client_secret, naver_search, naver_search_num):
    encText = urllib.parse.quote(naver_search)
    display = naver_search_num
    start = 1
    sort = 'sim'

    url = "https://openapi.naver.com/v1/search/blog?query=" + encText + "&display=" + str(display) + "&start=" + str(start) + "&sort=" + sort

    result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret": client_secret})
    json_obj = result.json()
    rescode = result.status_code

    if(rescode==200):
        # print(json_obj)
        # for item in json_obj['items']:
        #     print(item['title'])
        #     print(item['link'])
        return json_obj
    else:
        # print("Error Code:" + rescode)
        return None