import math

# compute next time a disk hits a wall
def wall_time(pos_a, vel_a, sigma):
    if vel_a > 0.0:
        del_t = (1.0 - sigma - pos_a) / vel_a
    elif vel_a < 0.0:
        del_t = (pos_a - sigma) / abs(vel_a)
    else:
        del_t = float('inf')
    return del_t
# compute next time two disks hit eachother
def pair_time(pos_a, vel_a, pos_b, vel_b, sigma):
    del_x = [pos_b[0] - pos_a[0], pos_b[1] - pos_a[1]]
    del_x_sq = del_x[0] ** 2 + del_x[1] ** 2
    del_v = [vel_b[0] - vel_a[0], vel_b[1] - vel_a[1]]
    del_v_sq = del_v[0] ** 2 + del_v[1] ** 2
    scal = del_v[0] * del_x[0] + del_v[1] * del_x[1]
    Upsilon = scal ** 2 - del_v_sq * ( del_x_sq - 4.0 * sigma **2)
    if Upsilon > 0.0 and scal < 0.0:
        del_t = - (scal + math.sqrt(Upsilon)) / del_v_sq
    else:
        del_t = float('inf')
    return del_t

pos = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
vel = [[0.21, 0.12], [0.71, 0.18], [-0.23, -0.79], [0.78, 0.1177]]
# an array that considers each disk individually (or as a single)
singles = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]
# an array that shows us each pair of disks
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
sigma = 0.15
t = 0.0
n_events = 100
for event in range(n_events):

    # for each disk, compute the time it takes to hit a wall
    wall_times = [wall_time(pos[k][l], vel[k][l], sigma) for k, l  in singles]
    # for each pair of disks, compute the time it takes for them to hit
    pair_times = [pair_time(pos[k], vel[k], pos[l], vel[l], sigma) for k, l in pairs]
    # for all event times, find the next (smallest)
    next_event = min(wall_times + pair_times)
    # increment time
    t += next_event
    # update position of each disk
    for k, l in singles: pos[k][l] += vel[k][l] * next_event
    # if next event was a hit on the wall,
    # extract disk that collided with the wall, along with its direction,
    # then update the disks velocity by negating the component of velocity
    # that is normal the wall.
    # note* this negation occurs because the force of wall on disk is **only**
    #       in the direction normal to the wall.
    if min(wall_times) < min(pair_times):
        collision_disk, direction = singles[wall_times.index(next_event)]
        vel[collision_disk][direction] *= -1.0
    # otherwise, collision was between disks, so update their velocities
    else:
        a, b = pairs[pair_times.index(next_event)]             # get pair of disks that collided
        del_x = [pos[b][0] - pos[a][0], pos[b][1] - pos[a][1]] # get difference in their positions
        abs_x = math.sqrt(del_x[0] ** 2 + del_x[1] ** 2)       # get absolute diff in positions
        e_perp = [c / abs_x for c in del_x]                    # get direction of difference as a unit vector.  This is the **direction** of perturbation in velocity for each disk
        del_v = [vel[b][0] - vel[a][0], vel[b][1] - vel[a][1]] # get difference in velocities
        scal = del_v[0] * e_perp[0] + del_v[1] * e_perp[1]     # get a number that is the dot product between velocity difference and unit vector of position differences.  This is the **magnitude** of velocity perturbation
        for k in range(2):                                     # update velocities for disks using
            vel[a][k] += e_perp[k] * scal
            vel[b][k] -= e_perp[k] * scal
    print 'event', event
    print 'time', t
    print 'pos', pos
    print 'vel', vel
