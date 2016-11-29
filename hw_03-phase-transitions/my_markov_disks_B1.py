# Thomas Rapstine
# SMAC: HW 03 B1

import random
import math
import pylab

# originally from direct_disks_multirun.py
def dist(x,y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)

# modified from markov_disks_box.py
# initialize disk centers
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma   = 0.15  # radius of disks
delta   = 0.1   # step size
n_steps = 100   # number of steps
for steps in range(n_steps):
    # choose a point in the current disk configuration
    a = random.choice(L)
    # take a step from chosen point
    b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
    # acquire minimum distance to new point
    min_dist=min(dist(c,b) for c in L if c != a )
    # only accept new point if far enough from other points
    if not (min_dist < 2*sigma):
        a[:]=b
print(L)
