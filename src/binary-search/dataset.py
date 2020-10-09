import random

# will generate either an odd or even dataset
def generateDataset():
    _dataset = []
    _data = random.randint(1,2)

    for i in range(100):
        _dataset.append(_data)
        _data += 2

    return _dataset
