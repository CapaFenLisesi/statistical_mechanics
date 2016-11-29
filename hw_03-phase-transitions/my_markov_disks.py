
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

# originally from tutorial 3: prep. program 1
def show_conf(L, sigma, title, fname):
    pylab.axes()
    c=0
    for [x, y] in L:
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                cir = pylab.Circle((x + ix, y + iy), radius=sigma,  fc='r')
                pylab.gca().add_patch(cir)
                c+=1
    pylab.axis('scaled')
    pylab.title(title)
    pylab.axis([0.0, 1.0, 0.0, 1.0])
    pylab.savefig(fname)
    pylab.show()
    pylab.close()

# from markov_disks_box.py
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
sigma = 0.15 # radius of disks
sigma_sq = sigma ** 2
delta = 0.1 # step size
n_steps = 100 # number of steps
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
        
show_conf(L,sigma,'test','junk.png')
