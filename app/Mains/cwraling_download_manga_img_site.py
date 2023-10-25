import requests
from bs4 import BeautifulSoup
import os

download_site = 'https://wfwf294.com/'
download_site_header = {'Referer': download_site}
down_list ={ '헬크': ['12122', 145]
         ,'베른디오': ['13909', 69]
         ,'패래럴파라다이스': ['10236', 238]
         ,'원펀맨': ['10200', 284]
         ,'다크개더링': ['10289' , 54]
         ,'부덕의길드': ['10618', 95]
         ,'빙검의마술사': ['13766',120]
         ,'템플': ['12760',98]
             ,'만지지 말아 줘 코테사시 군': ['15505',68 ]
             ,'최애의 아이':['13696',133]
             ,'귀축 영웅':['15590',49]
             ,'이러는 게 좋아':['14248',156]
             ,'숨은 실력자가 되고싶어서':['10422',99]
             ,'회복술사의 재시작':['12751',118]
             ,'친구게임':['10687',165]
             ,'골든카무이':['10193',313]
             ,'무직전생':['12608',120]
             ,'흑의소환사':['12138',149]
             ,'고간무쌍':['15643',32]
             ,'인싸공명':['13306',103]
             ,'성검학원의 마검사':['13725',54]
             ,'장송의 프리렌':['13697',116]
             ,'마슐':['13408',162]
             ,'너를 너무너무너무나 좋아하는 100명의 여친':['13240',170]
             ,'짐승의 길':['10754',81]
             ,'아무하고나 자는 네가 좋아':['16722',20]
             ,'귀환자의 마법은 특별해야 합니다':['2232',241]
             ,'닥터 스톤':['13953',235]


            }
select = '닥터 스톤'
manga_nm = select
manga_id  = down_list[select][0]
manga_sn_st = 66   #귀환자 143
manga_sn = down_list[select][1]

save_path = f'C:/Users/jiyeu/OneDrive/바탕 화면/만화/{manga_nm}/'




def collectLinks(downAddr, downSn):
    source = requests.get(downAddr).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select('div.group.image-view > img')
    link_list = []
    print(f'{downSn} - {str(elem_list)}')
    for e in elem_list:
        link_list.append( {'title': downSn.zfill(3)+'_'+ e.get("alt") , 'link': e.get("data-original") } )
    return link_list

def download( savePath, fileName,url):
    with open(savePath+ fileName +'.jpg', "wb") as file:  # open in binary mode
        try:
            response = requests.get(url, headers= download_site_header ,timeout = 5)  # get request
            file.write(response.content)  # write to file
        except:
            download( savePath, fileName,url)

def main():
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i in range(manga_sn_st,manga_sn):
        download_sn = str( i +1 )
        download_addr = f"{download_site}cv?toon={manga_id}&num={download_sn}"
        img_list = collectLinks(download_addr , download_sn)
        if not len(img_list) == 0 :
            for e in img_list:
                download(save_path, e['title'], e['link']  )
        else:
            print('파일없음')

main()