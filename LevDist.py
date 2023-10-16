import numpy as np


def LevDist(a, b):
    a = a.lower()
    b = b.lower()
    t = np.zeros((len(a) + 1, len(b) + 1))
    t[:, 0] = np.arange(len(a) + 1)
    t[0, :] = np.arange(len(b) + 1)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                c = 0
            else:
                c = 1
            t[i, j] = min(t[i - 1, j] + 1, t[i, j - 1] + 1, t[i - 1, j - 1] + c)
    print(t)
    return t[-1, -1]


print(LevDist('Saturday', 'Sunday'))
