from app.PyClass import OracleClass as oracle
from app.PyClass import TimeClass
from app.PyClass import XMLClass as XML
import pandas as pd

xml = XML.XMLclass('etcMapper')
ora = oracle.Oracle(connectName='oracle_DQ')
df = ora.getResultToDataFrame(xml.getData("sql02"))
workList =[ '01_서울' ,'02_부산' ,'03_대구'  ,'04_인천' ,'05_광주'  ,'06_대전' ,'07_울산' ,'08_세종' ,'09_경기' ,'10_강원'
           ,'11_충북' ,'12_충남' ,'13_전북' ,'14_전남','15_경북'  ,'16_경남' ,'17_제주'  ,'00_교육(국립)']

xml2 = XML.XMLclass('property')
filePath = xml2.getData("OUTPUT")

#df.to_excel(writer, sheet_name=work["sheetName"], encoding='utf-8', freeze_panes=(1, 0), index=False)
for work in workList:
    file = f'{filePath}/{work}_안전등급 상향시설 목록_20220921.xlsx'
    writer = pd.ExcelWriter(file, engine="xlsxwriter")
    df[df["시도"]==work].to_excel(writer, sheet_name=work, encoding='utf-8', freeze_panes=(1, 0), index=False)
    print(df[df["시도"]==work])
    writer.save()

