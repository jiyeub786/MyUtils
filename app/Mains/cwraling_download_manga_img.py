import requests
from bs4 import BeautifulSoup
from requests import get

사이트링크 =  'https://wfwf284.com/'
헬크id= '12122'
헬크번호 = 145
베른디오id= '13909'
베른디오번호 = 69
headers = {'Referer': 'https://wfwf284.com/'}
from time import sleep

dwn_path = 'E:\python\python_project\crawlKeywords\\app\\app_web\\files\\헬크\\'

def download( file_name,url):
    with open(dwn_path + file_name +'.jpg', "wb") as file:  # open in binary mode
        response = get(url,headers = headers)  # get request
        file.write(response.content)  # write to file


def Movie(num  ,만화id):
    sleep(3)
    source = requests.get(사이트링크 + 'cv?toon='+ 만화id + '&num=' + num).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select('div.group.image-view > img')
    # print(source)

    print(elem_list)
    for e in elem_list:
        download( str(num).zfill(3)+'_'+e.get("alt") ,e.get("src") )


ID = 헬크id
번호 = 헬크번호
for i in range(15,번호):
    Movie(str(i + 1) ,ID)
