import random

# will generate either an odd or even dataset
def generateDataset():
    _dataset = []
    _theStartingPoint = random.randint(1,2)

    for i in range(100):
        _dataset.append(i)
        i += 2

    return _dataset
