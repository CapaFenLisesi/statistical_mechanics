import random

# faster version of direct_pins.py with smart checking
# for spacing of pins.
N = 15
L = 10.0
sigma = 0.075
n_configs = 1000
for config in range(n_configs):
    while True:
        x = [random.uniform(sigma, L - sigma) for k in range(N)]
        x.sort()
        min_dist = min(x[k + 1] - x[k] for k in range(N - 1))
        if min_dist > 2.0 * sigma:
            print x
            break
