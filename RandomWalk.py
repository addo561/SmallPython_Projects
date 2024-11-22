import numpy as np 
import matplotlib.pyplot as plt

def random_w(steps):
    walk = np.zeros(steps)
    for i in range(1,1000):
        step = np.random.choice([-1,1])
        walk[i] = walk[i - 1] + step
    return walk
steps = 1000
walk = random_w(steps)

fig = plt.figure(figsize=(10,8))
plt.title('Random walk')
plt.plot(walk,label = '1D random walk')
plt.xlabel('Steps')
plt.ylabel('Position')
plt.legend()
plt.show       