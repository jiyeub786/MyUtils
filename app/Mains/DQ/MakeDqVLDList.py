from app.PyClass import  OracleClass as oracle
from app.PyClass import  TimeClass
from app.PyClass import XMLClass as XML
import pandas as pd


t = TimeClass.Time()

xml = XML.XMLclass('dqMapper')
xml2 = XML.XMLclass('property')
filePath = xml2.getData("OUTPUT")


workList = [
        { 'SQL' : xml.getData("selectColVldList") ,'sheetName' : '적용규칙목록' }
       ,{ 'SQL' : xml.getData("selectVldList") ,'sheetName' : '규칙목록' }

      ]
file = f'{filePath}/dq_vldList{t.getStrYMD2()}.xlsx'
print(file)
writer = pd.ExcelWriter(file, engine="xlsxwriter")



ora = oracle.Oracle(connectName='oracle_DQ')
for work in  workList:
   df = ora.getResultToDataFrame(work["SQL"])
   df.to_excel(writer, sheet_name=work["sheetName"],encoding='utf-8' , freeze_panes = (1, 0), index=False)

writer.save()


