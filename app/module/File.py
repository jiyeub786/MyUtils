import os

class File:
    def __init__(self, filePath):
        self.filePath = filePath

    def getFileList(self):
        return os.listdir(self.filePath)

    def getFileTextDictList(self):
        FileTextDictList = []
        for i, v in enumerate(self.getFileList()):
            if os.path.isdir(self.filePath + v) == False:
                f = open(self.filePath + "/" + v, "r", encoding="utf-8-sig")
                data = f.readlines()
                fileName = v
                fileText = ""
                for v in data:
                    fileText = fileText + v.replace(";", "")  # sql의 ;를 빼준다
                fileTextDict = {"fileName": fileName, "fileText": fileText}

                FileTextDictList.append(fileTextDict)
        return FileTextDictList



filepath = "E:\python\python_project\makeSqlToExcel\\app\\files\INPUTS\\"

f = File(filepath);




for v in f.getFileTextDictList():
    print(v)