import math

# Will perform a binary search for the value on the provided dataset
def binarySearch(pDataset, pValue):
    _output = ""
    _processedDataset = pDataset
    _iteration = 0
    _found = False

    if len(_processedDataset) > 0:

        while not _found and len(_processedDataset) > 1:
            _iteration += 1
            theMiddlePoint = math.floor(len(_processedDataset) / 2) # 0 Based array
            theValue = _processedDataset[theMiddlePoint]

            if theValue == pValue:
                _output = "found " + str(pValue) + " on the iteration #" + str(_iteration)
                _found = True
            elif theValue < pValue:
                _processedDataset = _processedDataset[slice(theMiddlePoint, len(_processedDataset))] 
            else:
                _processedDataset = _processedDataset[slice(0, theMiddlePoint - 1)] # Middle point -1 as the array is 0 based, and middle point was tested negative

            if len(_processedDataset) <= 1:
                _output = "Couldn't find the result"

        
    else:
        _output = "dataset is empty"

    return _output