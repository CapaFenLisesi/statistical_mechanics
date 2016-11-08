import random, math, pylab

 
def direct_pi(N):
  '''
  Compute the number of hits when N-runs are performed on the Monte Carlo
  children's game pebble algorithm
  '''
  n_hits = 0
  for i in range(N):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    if x ** 2 + y ** 2 < 1.0:
      n_hits += 1
  return n_hits

 
n_runs   = 500
n_trials_list = [] # for storing number of trials, with corresponding rms_deviation
rms_deviation = [] # for storing rms_deviation as a function of trial numbers

# run n_runs for each varying number of trials
for power in range(4,13):
  n_trials = 2 ** power
  sigsq  = 0
  
  # for a specified number of runs, estimate pi, then accumulate rms error estimate
  for run in range(n_runs):

    # estimate pi
    pi_i_est = 4.0 * direct_pi(n_trials) / float(n_trials)
  
    # accumulate sum for rms deviation
    sigsq+=(pi_i_est-math.pi)**2

  rms_deviation.append(math.sqrt(sigsq/n_runs))
  n_trials_list.append(n_trials)

pylab.plot(n_trials_list,rms_deviation,'+r')
pylab.xscale('log')
pylab.yscale('log')
pylab.title('Direct sampling of pi: rms deviation vs. number of trials')
pylab.xlabel('number of trials')
pylab.ylabel('rms deviation')
pylab.show() 


