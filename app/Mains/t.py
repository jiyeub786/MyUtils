
import pandas as pd
from app.PyClass import OracleClass as oracle
from app.PyClass import XMLClass as XML
from app.module import modules as m

xml = XML.XMLclass('statMapper')
query = xml.getText("./sql[@id='getRsltTablesList']")

propertyXml = XML.XMLclass('property')
outputPath = propertyXml.getText("./filePath[@id='INPUT']")

oracle01 = oracle.Oracle()

df =  oracle01.selectPandasDataFrame(query).fillna(0)

dictList =[]

for i ,row in df.iterrows():
    dict = {'fileNm': row['TABLE_NAME']+' '+row['COMMENTS'] , 'sql':row['SQL01'], 'index':i }
    print(dict)
    dictList.append( dict)


#print(dictList)

m.getSqlDictListToExcel( dictList ,outputPath ,oracle01.getCon() )