# jsonParser.py

from logic.abstractParser import AbstractParser
import json

class JsonParser(AbstractParser):
    # Constants
    cFileExtension = "json"

    def __init__(self):
        super().__init__()

    def ParseFiles(self):
        theResult = []

        for theFilePath in self.Files:

            with open(theFilePath, encoding='utf-8-sig') as theFile:
                theFileContent = theFile.read()
                theData = json.loads(theFileContent)
                theResult.append(theData)
                

        return theResult