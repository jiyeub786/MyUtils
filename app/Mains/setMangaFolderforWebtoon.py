import os
import shutil

filePath = 'C:/Users/jiyeu/OneDrive/바탕 화면/만화/귀환자의 마법은 특별해야 합니다'

def getFileList(filePath):
    fileList =[]
    for file in os.listdir(filePath):
        if os.path.isfile(f"{filePath}/{file}"):
            if '.jpg' in file:
                fileList.append(file)
    return fileList


def getFileLableNum(fileList):
    fileLableNumList =[]
    for f in fileList:
        fileLableNumList.append(f[0:3])
    fileLableNumList.sort()
    fileLableNumList = list(set(fileLableNumList))
    fileLableNumList.sort()
    return fileLableNumList

def setNumFolder(filePath ,fileLableNumList ):
    for num in fileLableNumList:
        dir = f"{filePath}/num/{num}"
        if not os.path.exists(dir):
            os.makedirs(dir)

def setCopyFileToNumDir(filePath,fileList,lableNumList):
    for file  in fileList:
        for lableNum in lableNumList:
            if lableNum in file:
                print(f"{filePath}/{file }   {filePath}/num/{lableNum}/{file }")
                shutil.copyfile(f"{filePath}/{file }" , f"{filePath}/num/{lableNum}/{file }")


fileList = getFileList(filePath)
lableNumList = getFileLableNum(fileList)
setNumFolder(filePath ,lableNumList )
setCopyFileToNumDir(filePath ,fileList,lableNumList )


