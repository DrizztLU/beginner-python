# xmlParser.py
from logic.abstractParser import AbstractParser

class CSVParser(AbstractParser):
    # Constants
    cFileExtension = "xml"

    def __init__(self):
        super().__init__()

    def ParseFiles(self):
        theResult = []

        for theFilePath in self.Files:

            with open(theFilePath, encoding='utf-8-sig') as theFile:
                
                

                theResult.append(theData)

        return theResult