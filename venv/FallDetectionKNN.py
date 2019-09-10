import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import scipy.special
import scipy.stats as stats
import math
import pandas as pd
import operator

# load data file in Numpy
columns = ['counter', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']
data = np.genfromtxt('test01.tsv')

assert data.shape[1] == 8, 'you already ran this cell!'
data = np.concatenate([data, np.ones((data.shape[0], 1))], axis=1)  # add a column of ones
print(data.shape, "\n", data)


# load data file in Pandas
def loadData(file):
    dataFrame = pd.read_csv(file)
    return dataFrame

