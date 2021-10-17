import numpy as np
import bezier
import matplotlib.pyplot as plt

nodes = np.asfortranarray([
    [0.0, 2, -0.3, 0.2, -1],
    [0.0, 0.1, 2.5, 0.0, -3],
])
bezier.Curve(nodes, degree=len(nodes[0])-1).plot(100)
plt.gca().set_aspect('equal')
plt.scatter(nodes[0], nodes[1])
plt.show()