# Mann-Whitney U test
import numpy as np
from numpy.random import seed
from numpy.random import randn
from scipy.stats import mannwhitneyu

# seed the random number generator
seed(1)

list_of_clients = [i for i in range(20, 1000)]
list_of_p = []


def counter():
    for i in list_of_clients:# generate two independent samples
        data1 = np.random.randint(0, 20, size=i,)
        data2 = np.random.randint(0, 20, size=i,) + 2*np.random.randn(i)
        stat, p = mannwhitneyu(data1, data2, alternative='two-sided')
        print('Statistics=%.3f, p=%.4f' % (stat, p))
        alpha = 0.01
        # compare samples
        if p > alpha:
            print('Same distribution (fail to reject H0)')
        else:
            print('Different distribution (reject H0)')

        if p > alpha:
            print(p)
            continue
        if p <= alpha:
            list_of_p.extend([p, i])
    print(list_of_p)


# interpret


# data10 = np.random.randint(1, 20, size=50) + randn(50)

counter()
