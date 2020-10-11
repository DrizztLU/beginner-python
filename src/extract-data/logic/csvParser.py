# csvParser.py
from logic.abstractParser import AbstractParser
import csv

class CSVParser(AbstractParser):
    # Constants
    cFileExtension = "csv"
    cDelimiter = ','

    def __init__(self):
        super().__init__()

    def ParseFiles(self):
        theResult = []

        for theFilePath in self.Files:

            with open(theFilePath, encoding='utf-8-sig') as theFile:
                theFileContent = csv.reader(theFile, delimiter=self.cDelimiter)
                theLineCount = 0
                theColumnCount = 0
                theHeaders = []
                theData = []

                for theRow in theFileContent:
                    
                    if(theLineCount == 0):
                        theHeaders = theRow
                        theLineCount += 1
                    else:
                        theItem = {}

                        for theColumn in theHeaders:
                            # retrieve the header for each column, and inject the line data
                            theItem[theHeaders[theColumnCount]] = theRow[theColumnCount]
                            theColumnCount += 1

                        theData.append(theItem)
                        theColumnCount = 0
                        theLineCount += 1

                theResult.append(theData)

        return theResult