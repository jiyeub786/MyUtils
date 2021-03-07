
from app.PyClass import OracleClass as oracle
from app.PyClass import XMLClass as XML
from app.module import modules as m
xml = XML.XMLclass('statMapper')
query1 = xml.getText("./sql[@id='getRsltTablesList']")

propertyXml = XML.XMLclass('property')
outputPath = propertyXml.getText("./filePath[@id='OUTPUT']")

oracle01 = oracle.Oracle()

df =  oracle01.selectPandasDataFrame(query1)

dictList =[]

for i ,row in df.iterrows():
    print(row)
    dict = { 'theme' : str(row['THEME']),'fileNm': str(row['TABLE_NAME'])+'  '+str(row['COMMENTS'])+'    '+str(row['UNIT']) , 'sql':row['SQL01'], 'index':i }
    print(dict)
    dictList.append( dict)



#print(dictList)

m.statexcel(dictList, outputPath, oracle01.getCon())