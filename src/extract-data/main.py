from logic.jsonParser import JsonParser
from logic.csvParser import CSVParser
from logic.xmlParser import XMLParser
from time import perf_counter 

theTimers = {
    "json": 0,
    "csv": 0,
    "xml": 0,
}

# Extracting data for 3 different datasources

theJsonTimerStart = perf_counter()

theJsonParser = JsonParser()
theJsonData = theJsonParser.ParseFiles()

theJsonTimerStop = perf_counter()

theTimers["json"] = theJsonTimerStop - theJsonTimerStart

print ("JSon parse elapsed time: "+ str(theTimers["json"]) + "s")

theCSVTimerStart = perf_counter()

theCSVParser = CSVParser()
theCSVData = theCSVParser.ParseFiles()

theCSVTimerStop = perf_counter()

theTimers["csv"] = theCSVTimerStop - theCSVTimerStart

print ("CSV parse elapsed time: "+ str(theTimers["csv"]) + "s")

# XML doesn't have a neat parser, so I'll have to do it manually (coming later!)

# theXMLTimerStart = perf_counter()

# theXMLParser = XMLParser()
# theXMLData = theXMLParser.ParseFiles()

# theXMLTimerStop = perf_counter()

# theTimers["xml"] = theXMLTimerStop - theXMLTimerStart

# print ("XML parse elapsed time: "+ str(theTimers["xml"]) + "s")

# Data should be easily comparable

