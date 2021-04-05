import numpy as np
import itertools as it
from tools.decorator import memoized  # A standard memoization decorator

SIDES = 6

@memoized
def get_t_and_p(state):
    if all(s == 0 for s in state):
        return 0, 1.0
    n = len(state)
    choices = [[s - 1, s] if s > 0 else [s]
               for s in state]
    ts = []
    ps = []
    for last_state in it.product(*choices):
        if last_state == state:
            continue
        last_t, last_p = get_t_and_p(tuple(sorted(last_state)))
        if last_p == 0.0:
            continue
        transition_p = 1.0
        stay_p = 1.0
        for ls, s in zip(last_state, state):
            if ls < s:
                transition_p *= (SIDES - ls) / SIDES
            else:
                transition_p *= ls / SIDES
            stay_p *= ls / SIDES
        if transition_p == 0.0:
            continue
        transition_time = 1 / (1 - stay_p)
        ts.append(last_t + transition_time)
        ps.append(last_p * transition_p / (1 - stay_p))
    if len(ts) == 0:
        return 0, 0.0
    t = np.average(ts, weights=ps)
    p = sum(ps)
    return t, p

print(get_t_and_p((SIDES,) * 4)[0])