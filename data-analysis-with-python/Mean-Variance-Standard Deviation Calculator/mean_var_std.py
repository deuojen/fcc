import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    calculations = {}
    shape = np.array(list).reshape(3, 3)

    mean = [np.mean(shape, axis=0).tolist(), np.mean(
        shape, axis=1).tolist(), np.mean(shape)]
    calculations['mean'] = mean

    variance = [np.var(shape, axis=0).tolist(), np.var(
        shape, axis=1).tolist(), np.var(shape)]
    calculations['variance'] = variance

    sd = [np.std(shape, axis=0).tolist(), np.std(
        shape, axis=1).tolist(), np.std(shape)]
    calculations['standard deviation'] = sd

    max_list = [np.max(shape, axis=0).tolist(), np.max(
        shape, axis=1).tolist(), np.max(shape)]
    calculations['max'] = max_list

    min_list = [np.min(shape, axis=0).tolist(), np.min(
        shape, axis=1).tolist(), np.min(shape)]
    calculations['min'] = min_list

    sum_list = [np.sum(shape, axis=0).tolist(), np.sum(
        shape, axis=1).tolist(), np.sum(shape)]
    calculations['sum'] = sum_list

    print(calculations)
    return calculations
