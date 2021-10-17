import matplotlib.pyplot as plt
import numpy as np
from letters import letter

word = 'skap skap dot a'

word = [letter(l) for l in word.split()]

k = 10
a = 0
m = 0.7
dt = 0.1

pen_pos = np.array([0.0, 0.0])
zero = np.array([0.0, 0.0])

pen_res_vec = []
thought_res_vec = []

plt.ion()
c = 0


for letter, n, terminate in word:
    if terminate:
        pen_pos = tp
        a = 0
    for p in np.linspace(0, 1, n):
        c += 1
        tp = letter.evaluate(p)
        tp = zero + np.array([tp[0][0], tp[1][0]])

        R = tp - pen_pos
        F = k * R
        a = F / m + m * a
        dv = a * dt
        dx = dv * dt
        pen_pos += dx

        pen_res_vec.append(pen_pos.tolist())
        thought_res_vec.append(tp.tolist())
        p = np.array(pen_res_vec)
        t = np.array(thought_res_vec)
        plt.cla()
        plt.plot(t[:, 0], t[:, 1])
        plt.plot(p[:, 0], p[:, 1], '--')
        plt.gca().set_aspect('equal')
        plt.pause(0.001)
        #plt.savefig('{}.png'.format(c))
    zero = tp
plt.ioff()
plt.plot(t[:, 0], t[:, 1])
plt.plot(p[:, 0], p[:, 1], '--')
plt.gca().set_aspect('equal')
plt.show()
