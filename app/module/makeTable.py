import pandas as pd
import os

os.getcwd()
os.chdir('..')

excelFilePath =  os.getcwd() + "\\files\\aaa.xlsx" #읽을 파일 경로
excelFilePath2 =  os.getcwd() + "\\files\\aa.xlsx" #읽을 파일 경로

data = pd.read_excel(excelFilePath)


colList = data.columns
for col in colList:
    print(col)

list = data.values.tolist()

dic = {}
for l in list:
    for i , ll in enumerate(l):
        print(len(ll[i].encode()))



#print(data.head(5))
#print(data.dtypes)
print(    data.describe())


text = 'BTS는 방탄소년단, 7인조그dfdfsdfds룹'
print(len(text.encode()))
#result = []

#result = data.dtypes

#print(result)
#
# data = pd.read_excel(excelFilePath2)
#
# print(data.head(5))
# print(data.dtypes)
# result = []
#
# result = data.dtypes
