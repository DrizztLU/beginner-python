from logic.jsonParser import JsonParser
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

print ("JSon parse elapsed time: "+ theTimers["json"] + "s")