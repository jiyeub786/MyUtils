import os
import time
import app.database.Oracle as oracle

class File:
    def __init__(self, filePath):
        self.filePath = filePath

    def getFileList(self):
        return os.listdir(self.filePath)

    def readFile(self):
        return  open(self.filePath , "r")

