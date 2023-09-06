import requests
import time
import re
from bs4 import BeautifulSoup

def downloadFile( save_path, file_name,url,headers):
    with open(save_path+ file_name, "wb") as file:  # open in binary mode
        try :
            response = requests.post(url,headers = headers, timeout = 15)
            file.write(response.content)  # write to file
            print(f"[{time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}] {file_name} complete")# get request

        except:
            print(f"[{time.strftime('%Y-%m-%d %I:%M:%S %p', time.localtime())}] {file_name} re try")
            downloadFile( save_path, file_name,url,headers)

def searchDownloadLinks(download_site,headers):
    source = requests.get(download_site ,headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select('div.ntc-view a')
    list =[]
    for n,i in enumerate(elem_list):
        list.append(        {'file_nm' : i.getText() , 'file_id': i.get("href").split('\'')[1],'file_sn': i.get("href").split('\'')[3]} )

    return list

def searchPost(download_site,headers,yyyy,mm):
    source = requests.get(download_site ,headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    elem_list = soup.select('table.bbs_type3 a')
    list =[]
    for n,i in enumerate(elem_list):
        pattn = re.compile(f'.*(기본개요|표제부|층별개요).*({yyyy}년 {mm}월).*' )
        if pattn.match(i.getText()) != None :
            list.append ( i.get("href").split('\'')[1] )
    print( 'download target post: ' + list)
    return list



def main():
    yyyy = '2023'
    mm = '07'
    save_path = f'D:\건축물대장 db수급/2022-06/'
    board_link = f'https://open.eais.go.kr/board/selectBoardNtcMgmList.do?viewType=C2'
    header1 = {'Referer': 'https://open.eais.go.kr'
        ,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        , 'Origin': 'https://open.eais.go.kr'
        ,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        , 'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6'
        , 'Accept-Encoding': 'gzip, deflate, br'
        , 'Content-Type': 'application/x-www-form-urlencoded'
        , 'Sec-Ch-Ua-Platform': '"Windows"'
        , 'Host': 'open.eais.go.kr'
        , 'Connection': 'keep-alive'
                }
    post_list= searchPost(board_link,header1,yyyy,mm)
    for ntcSn in post_list:
        post_link =  f'https://open.eais.go.kr/board/selectBoardNtcMgmDetail.do?viewType=C2Dtl&ntcSn={ntcSn}'
        header2 = {'Referer': f'https://open.eais.go.kr/board/selectBoardNtcMgmDetail.do?viewType=C2Dtl&ntcSn={ntcSn}'
                     ,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
                     , 'Origin': 'https://open.eais.go.kr'
                     ,'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
                     , 'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6'
                     , 'Accept-Encoding': 'gzip, deflate, br'
                     , 'Content-Type': 'application/x-www-form-urlencoded'
                     , 'Sec-Ch-Ua-Platform': '"Windows"'
                     , 'Host': 'open.eais.go.kr'
                     , 'Connection': 'keep-alive'
                    }
        file_list = searchDownloadLinks(post_link,header1)
        print(file_list)
        for i in file_list:
            file_nm = i['file_nm']
            file_id = i['file_id']
            file_sn = i['file_sn']
            attch_file_link = f'https://open.eais.go.kr/board/downNtc.do?ntcSn={ntcSn}&fileSn={file_id}&fileDetlSn={file_sn}&lgclflNm=&searchCondition=&searchKeyword=&pageIndex=1'
            downloadFile(save_path ,file_nm ,attch_file_link ,header2 )


    print('다운로드 완료')


main()

