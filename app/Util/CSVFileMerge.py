import csv

#filePath = "D:\db_svn\##2022운영관리사업/61_GIS DB관리/06_GIS_DB구축\위치정보 구축/202202_위치정보요약DB_전체분/"
filePath = "D:\gis\소상공인진흥공단_상가\소상공인시장진흥공단_상가(상권)정보_20230331/"

fileNm = ['소상공인시장진흥공단_상가(상권)정보_강원_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_경기_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_경남_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_경북_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_광주_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_대구_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_대전_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_부산_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_서울_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_세종_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_울산_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_인천_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_전남_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_전북_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_제주_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_충남_202303.csv',
                '소상공인시장진흥공단_상가(상권)정보_충북_202303.csv']


wf = open(filePath+'total.txt', 'a',encoding='UTF-8')

for f in fileNm:
    rf = open(filePath + f, 'r',encoding='UTF-8')

    lines = rf.readlines()

    for line in lines:
        wf.write(line)

        #wf.write(line[6]+'|'+line[8]+'|'+line[9]+'|'+line[10]+'|'+line[16]+'|'+line[17]+'\n')
    rf.close()

print ('done!')


# import csv
#
# filePath = "D:\db_svn\##2022운영관리사업/61_GIS DB관리/06_GIS_DB구축\위치정보 구축/202202_위치정보요약DB_전체분/"
# fileNm = ['entrc_busan.txt', 'entrc_chungbuk.txt', 'entrc_chungnam.txt', 'entrc_daegu.txt', 'entrc_daejeon.txt', 'entrc_gangwon.txt', 'entrc_gwangju.txt'
#          , 'entrc_gyeongbuk.txt', 'entrc_gyeongnam.txt', 'entrc_gyunggi.txt', 'entrc_incheon.txt', 'entrc_jeju.txt', 'entrc_jeonbuk.txt', 'entrc_jeonnam.txt'
#          , 'entrc_sejong.txt', 'entrc_seoul.txt', 'entrc_ulsan.txt']
#
#
# wf = open(filePath+'total.txt', 'a',encoding='UTF-8')
#
# for f in fileNm:
#     rf = open(filePath + f, 'r')
#     csv_rf = csv.reader(rf, delimiter='|')
#
#     for line in csv_rf:
#
#         wf.write(line[6]+'|'+line[8]+'|'+line[9]+'|'+line[10]+'|'+line[16]+'|'+line[17]+'\n')
#     rf.close()
#
# print ('done!')