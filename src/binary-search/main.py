import dataset
import binarySearch
import random

cSearch = random.randint(1, 200)

theDataset = dataset.generateDataset()

print("Searching for " + str(cSearch))
theSearchResult = binarySearch.binarySearch(theDataset, cSearch)

print(theSearchResult)