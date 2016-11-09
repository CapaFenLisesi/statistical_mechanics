# Thomas Rapstine
# Statistical Mechanics HW01
# Problem C2: bunching method (with unkown value of pi)

import random, math

n_trials = 400000
n_hits = 0
var = 0.0
mean_obs=0.0
mean_obs_squared=0.0
for iter in range(n_trials):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    # this is the "relevant observable"
    obs = 0.0  # for estimating pi this is 4.0 inside circle and 0.0 outside
    if x**2 + y**2 < 1.0:
        n_hits += 1
        obs = 4.0
    mean_obs        +=obs
    mean_obs_squared+=obs**2.0
    
mean_obs/=n_trials
mean_obs_squared/=n_trials
mean_obs_diff=mean_obs_squared-mean_obs**2.0

print('computed mean(obs)=%f'%(mean_obs))
print('computed mean(obs^2)=%f'%(mean_obs))
print('difference mean(obs^2)-mean(obs)^2=%f'%(mean_obs_diff))
print('sqrt(mean(obs^2)-mean(obs)^2)=%f'%(math.sqrt(mean_obs_diff)))




