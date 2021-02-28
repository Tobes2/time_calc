# time_calc
calculates time
(actually, converts minutes to hours, days, weeks, and years)
just something i wrote for fun

v0.1: does the thing
time taken (s):
key: (minutes: s taken)
10: 0
1000: 0.001
1000 000: 0.005
1000 000 000: 5.1
10 000 000 000: 52.4
:. time scales linearly? i think
this is bad

v0.2: the old one goes minutes to hours, hours to days, etc. the new one goes minutes to years, then leftover mins to weeks, then mins to days, etc. should be quicker
time taken (s):
key: (minutes : s taken - years returned)
10: 0                    -  0
1000: 0.001              -  0
1000 000: 0.001          -  1
1000 000 000: 0.003      -  1901
10 000 000 000: 0.01     -  19012
1000 000 000 000: 0.96   -  1901285
10 000 000 000 000: 9.1  -  19012852
conclusion: very fast, until the number of years starts going crazy. then, time directly correlates to # of years
also: fixed output looking funny
