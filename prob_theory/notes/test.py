import numpy as np

N1 = 6**2 + 1
N2 = 1000000


def count_reps(roll):
    s = 0
    for i in range(N1 - 1):
        if roll[i] == roll[i + 1] and roll[i] == 6:
            s += 1
    return s


ans = []
for i in range(N2):
    roll = np.random.randint(1, 6 + 1, N1)
    ans += [count_reps(roll)]

print(np.sum(ans) / N2)
print(np.std(ans) / N2)
print((N1 - 1) / 36)
