from logic.jsonParser import JsonParser
from logic.csvParser import CSVParser
from time import perf_counter 

theTimers = {
    "json": 0,
    "csv": 0,
    "xml": 0,
}

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