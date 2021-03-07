from app.PyClass import  OracleClass as oracle

from app.PyClass import XMLClass as XML

xml = XML.XMLclass('dqMapper')
query1 = xml.getText("./select[@id='selectTabComment']")
ttt = oracle.Oracle("oracle")

print(query1)

t = ttt.getResultToDataFrame(query1,{'owner': 'SYS'})

print(t)
for at in t:
    print(at)