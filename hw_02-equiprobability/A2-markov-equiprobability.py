# Statistical Mechanics: Algorithms and Computations
# HW 2: A2
# Thomas Rapstine
#
# Problem A2: equiprobability and markov chain algorithm
# * a repeat of A1 with markov chain instead of direct sampling

import random

# update disk configuration L using markov chain algorithm
# L = current disk configuration
# delta = step for markov chain algorithm
# sigma = disk radius
def markov_disks_box_update(L,delta,sigma):
        # choose one of the disks  coordinates randomly
        a = random.choice(L)

        # take a step +/- delta from position of said disk
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]

        # for other c disks in L ( where c != a) compute their distance from eachother
        # and find the minimum distance
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)

        # is minimum of disk position after step less than sigma
        # or
        # is maximum greater than 1.0 - sigma?
        # if so, then the disk is too close to the box edges which is no bueno
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma

        # if new disk position b is far enough from the edges,
        # and far enough away from other disks,
        # then put it in a (which is really part of L)
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
        return L

def markov_disks_box_multirun_equiprobability(n_runs,delta=0.1,del_xy=0.05):
    conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
    conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
    conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
    configurations = [conf_a, conf_b, conf_c]
    hits = {conf_a: 0, conf_b: 0, conf_c: 0}
    sigma = 0.15 # disk radius

    # initial location of disks
    L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]

    for run in range(n_runs):

        # update step using markov chain algorithm
        L=markov_disks_box_update(L,delta,sigma)

        # Evaluate if configuration L is to each configuration a-c
        for conf in configurations:
            condition_hit = True
            for b in conf:
                condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in L) < del_xy
                condition_hit *= condition_b
            if condition_hit:
                hits[conf] += 1

    for conf in configurations:
        print conf, hits[conf]
    return hits

# Problem A1.2: mulitple runs and varying threshold boxes for placement
print('for n_runs=10,000')
hits1=markov_disks_box_multirun_equiprobability(10000)
hits2=markov_disks_box_multirun_equiprobability(10000)
hits3=markov_disks_box_multirun_equiprobability(10000)

print('for n_runs=100,000')
hits4=markov_disks_box_multirun_equiprobability(100000)
hits5=markov_disks_box_multirun_equiprobability(100000)
hits6=markov_disks_box_multirun_equiprobability(100000)

print('for n_runs=1,000,000')
hits7=markov_disks_box_multirun_equiprobability(1000000)
hits8=markov_disks_box_multirun_equiprobability(1000000)
hits9=markov_disks_box_multirun_equiprobability(1000000)
