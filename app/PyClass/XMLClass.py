import xml.etree.ElementTree as elemTree
import os

resourcePath = '../Resource/'

xmlList = {  'property' : 'property.xml'
             ,'dataSource' : 'dataSource.xml'
             ,'statMapper' : 'mapper/stat.xml'
             ,'brMapper' : 'mapper/br.xml'
             ,'dqMapper' : 'mapper/dq.xml'
             }


class XMLclass:
    def __init__(self, xmlNameSpace):
        self.nameSpace = xmlList[xmlNameSpace]
        self.nameSpacePath = resourcePath + xmlList[xmlNameSpace]
        self.tree = elemTree.parse(self.nameSpacePath)

    def getTree(self):
        return self.tree

    def getText(self,path):
        return self.tree.find(path).text


