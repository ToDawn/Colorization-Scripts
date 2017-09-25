from collections import OrderedDict
from copy import deepcopy
from pprint import pprint

import numpy as np

class Compose(object):
    def __init__(self, criterions):
        self.criterions = criterions

    def __call__(self, data):
        record = OrderedDict()
        for c in self.criterions:
            t_data = deepcopy(data)
            record[c.__class__.__name__] = c(t_data)
        return record


class Mean(object):
    def __init__(self, axis=0):
        self.axis = axis

    def __call__(self, data):
        return np.mean(data, axis=self.axis)


class Median(object):
    def __init__(self, axis=0):
        self.axis = axis

    def __call__(self, data):
        return np.median(data, axis=self.axis)


class Std(object):
    def __init__(self, axis=0):
        self.axis = axis

    def __call__(self, data):
        return np.std(data, axis=self.axis)


class BestK(object):
    def __init__(self, topk=0.25):
        self.topk = topk

    def __call__(self, data):
        data.sort()
        total = data.shape[0]
        return np.mean(data[: int(total * self.topk)])


class WorstK(object):
    def __init__(self, topk=0.25):
        self.topk = topk

    def __call__(self, data):
        data.sort()
        data = data[::-1]
        total = data.shape[0]
        return np.mean(data[: int(total * self.topk)])


if __name__ == "__main__":
    data = np.random.random((150,))

    metrics = Compose([
        Mean(),
        Std(),
        Median(),
        BestK(topk=0.1),
        WorstK(topk=0.1),
    ])
    # pprint.pprint()
    pprint(metrics(data))
