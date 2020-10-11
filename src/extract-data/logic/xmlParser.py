# xmlParser.py
from logic.abstractParser import AbstractParser
from xml.etree import ElementTree
from model.xmlNodeTypeEnum import XMLNodeTypeEnum

class XMLParser(AbstractParser):
    # Constants
    cFileExtension = "xml"

    def __init__(self):
        super().__init__()

    def ParseFiles(self):
        theResult = []

        for theFilePath in self.Files:

            with open(theFilePath, encoding='utf-8-sig') as theFile:
                theTree = ElementTree.parse(theFile)
                theRoot = theTree.getroot()
                
                theData = self.__BuildData(theRoot)

                theResult.append(theData)

        return theResult

    def __BuildData(self, pNode):
        theNodeType = self.__DetermineNodeType(pNode)

        theArrayIteration = 0

        if theNodeType == XMLNodeTypeEnum.SIMPLEOBJECT:
            return pNode.text

        elif theNodeType == XMLNodeTypeEnum.OBJECT:
            theData = {}
            for theNode in list(pNode):
                theData[theNode.tag] = self.__BuildData(theNode) 

            return theData

        elif theNodeType == XMLNodeTypeEnum.ARRAY:
            theData = {}
            theData[pNode.tag] = []
            for theNode in list(pNode):
                theData[pNode.tag].append(self.__BuildData(theNode))
            return theData


    def __DetermineNodeType(self, pNode):
        theChildren = list(pNode)

        if len(theChildren) == 0:
            return XMLNodeTypeEnum.SIMPLEOBJECT
        elif (len(theChildren) > 1 and theChildren[0].tag == theChildren[1].tag) or pNode.tag == theChildren[0].tag + 's':
            return XMLNodeTypeEnum.ARRAY
        else:
            return XMLNodeTypeEnum.OBJECT

        # unreachable code 
        return XMLNodeTypeEnum.NONE