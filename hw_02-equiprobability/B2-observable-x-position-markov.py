#Problem B1: equiprobability for observable=x-position
import random, pylab


# update disk configuration L using markov chain algorithm
# L     = current disk configuration
# delta = step for markov chain algorithm
# sigma = disk radius
def markov_disks_box_update(L,delta,sigma):
        a = random.choice(L)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in L if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2):
            a[:] = b
        return L


N      = 4
sigma  = 0.1197
delta  = 0.1
n_runs = 2000000
histo_data = []
L = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
for run in range(n_runs):
    L = markov_disks_box_update(L, delta, sigma)
    for k in range(N):
        histo_data.append(L[k][0])
pylab.hist(histo_data, bins=100, normed=True)
pylab.xlabel('x')
pylab.ylabel('frequency')
pylab.title('Markov Chain algorithm: x coordinate histogram (density eta=0.18)')
pylab.grid()
pylab.savefig('markov_disks_histo.png')
pylab.show()
