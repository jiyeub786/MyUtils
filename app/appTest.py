import os

def getSqlDictList(inputFilePath):
    print("Read FileList from " + inputFilePath)
    inputFileList = os.listdir(inputFilePath)  # 읽은 파일 목록
    print("Read FileList completed")

    print(inputFileList)

    sqlList = []
    for i, v in enumerate(inputFileList):
        if os.path.isdir(inputFilePath+v) == False :
            print("Read sqlText from " + v)
            f = open(inputFilePath+"/"+v , "r",encoding="utf-8-sig")
            data = f.readlines()
            fileNm = v
            sql = ""
            for v2 in data:
                sql = sql + v2.replace(";","") # sql의 ;를 빼준다
            sqlDict = {"fileNm":fileNm, "sql":sql }
            sqlList.append(sqlDict)
    print("Make SQLList completed")
    return sqlList

#소스 경로 저장
base_dir = os.path.dirname( os.path.abspath( __file__ ) )
inputFilePath = base_dir + "/Files/INPUTS/" #읽을 파일 경로

print(getSqlDictList(inputFilePath))