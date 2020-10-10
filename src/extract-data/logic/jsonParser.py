# jsonParser.py

from logic.abstractParser import AbstractParser
import json

class JsonParser(AbstractParser):
    # Constants
    cFileExtension = "json"

    def __init__(self):
        super().__init__()

    def ParseFiles(self):
        theResult = {}
        i = 0

        for theFilePath in self.Files:
            theData = None

            with open(theFilePath) as theFile:
                theData = json.load(theFile)
                
            theResult[i] = theData
            i += 1

        return theResult