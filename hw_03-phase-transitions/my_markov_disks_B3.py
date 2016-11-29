# Thomas Rapstine
# SMAC: HW 03 B2

import os, random
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

# originally from hw 3: prep. program 1
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


# initialize disk configuration
N   = 64      # number of disks
eta = 0.72    # area of circles / total area = density
N_sqrt    =int(math.sqrt(N))
filename  ='disk_configuration_N%i_eta%.2f.txt' % (N, eta)
sigma     = math.sqrt(eta/(N*math.pi))
tiny_shift=(1-2*sigma*N_sqrt)/float(2.0*N_sqrt)
delxy     =tiny_shift+sigma
two_delxy =2.0*delxy
delta     =sigma # step size
n_steps   =1000000     # number of steps

# note: delxy is achieved by
# 0.) delxy is shift in x and y each iteration of forming L
# 1.) length occupied by N_sqrt-disks next to eachother = 2*sigma*N_sqrt
# 2.) remaining length along unit square side = 1-2*sigma*N_sqrt
# 3.) for delxy, this length is split N_sqrt times between N_sqrt disks:
#     (1-2*sigma*N_sqrt)/N_sqrt
# 4.) this length is too large by a factor of *two* since we add 2*delxy each
#     iteration of loop when forming L:
#     (1-2*sigma*N_sqrt)/N_sqrt/2
# 5.) the total shift each iteration between disk centers is then:
#     sigma + (1-2*sigma*N_sqrt)/N_sqrt/2

# originally from hw 3: prep. program 2
if os.path.isfile(filename):
    f = open(filename, 'r')
    L = []
    for line in f:
        a, b = line.split()
        L.append([float(a), float(b)])
    f.close()
    print 'starting from file', filename
else:
    # initialize disk centers if none were provided
    L = [[delxy + i * two_delxy, delxy + j * two_delxy] for i in range(N_sqrt) for j in range(N_sqrt)]

#show_conf(L,sigma,'Initial 2D disk configuration: \eta=%f, N=%d'%(eta,N),'my_markov_disks_B4_initial.png')
# Markov chain algorithm
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

# display final configuration
show_conf(L,sigma,'Final 2D disk configuration: \eta=%f, N=%d'%(eta,N),'my_markov_disks_B4_end.png')

# save final configuration as text file
f = open(filename, 'w')
for a in L:
   f.write(str(a[0]) + ' ' + str(a[1]) + '\n')
f.close()
