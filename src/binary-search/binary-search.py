import math

# Will perform a binary search for the value on the provided dataset
def binarySearch(pDataset, pValue):
    _output = ""
    _processedDataset = pDataset
    _iteration = 0
    _found = False

    if len(_processedDataset) > 0:

        while not _found and len(_processedDataset) > 0:
            _iteration += 1
            theMiddlePoint = math.floor(len(_processedDataset) / 2) - 1 # 0 Based array
            theValue = _processedDataset[theMiddlePoint]

            if theValue == pValue:
                _output = "found " + pValue + " on the iteration #" + _iteration
                _found = True
            elif theValue > pValue:
                _processedDataset = _processedDataset[slice(theMiddlePoint + 1, len(_processedDataset) - 1)]
            else:
                _processedDataset = _processedDataset[slice(0, theMiddlePoint + 1)]

        
    else:
        _output = "dataset is empty"

    return _output