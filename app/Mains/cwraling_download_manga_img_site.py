import requests
from bs4 import BeautifulSoup
from requests import get

download_site =  'https://wfwf285.com/'
headers = {'Referer': download_site }
down_list ={ '헬크': ['12122', 145]
         ,'베른디오': ['13909', 69]
         ,'패래럴파라다이스': ['10236', 238]
         ,'원펀맨': ['10200', 284]
         ,'다크개더링': ['10289' , 54]
         ,'부덕의길드': ['10618', 95]
         ,'빙검의마술사': ['13766',120]
         ,'템플': ['12760',98]
             ,'만지지 말아 줘 코테사시 군': ['15505',68 ]
            }
select = '만지지 말아 줘 코테사시 군'
manga_nm = select
manga_id  = down_list[select][0]
manga_sn = down_list[select][1]

def download( save_path, file_name,url):
    with open(save_path+ file_name +'.jpg', "wb") as file:  # open in binary mode
        response = get(url,headers = headers)  # get request
        file.write(response.content)  # write to file


def collectLinks(down_addr  ,save_path , down_sn):
    source = requests.get(down_addr).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select('div.group.image-view > img')
    link_list = []
    print(down_sn + str(elem_list))
    for e in elem_list:
        link_list.append( {'title': down_sn.zfill(3)+'_'+ e.get("alt") , 'link': e.get("src") } )
    return link_list







save_path = f'C:/Users/jiyeu/OneDrive/바탕 화면/만화/{manga_nm}/'
for i in range(50,manga_sn):
    down_sn = str( i +1 )
    down_addr = download_site + 'cv?toon=' + manga_id + '&num=' + down_sn
    img_list = collectLinks(down_addr ,save_path , down_sn)
    for e in img_list:
        download(save_path, e['title'], e['link'])
