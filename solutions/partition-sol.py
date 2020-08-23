from z3 import *

# Partition range [1, N) evenly into P sub-ranges

s = Solver()

N = 10
P = 4

sz = [Int('sz' + str(i)) for i in range(P)]

# Even partitions:
for i in range(P):
  for j in range(P):
    s.add(sz[i] - sz[j] <= 1)

# Add up to N:
s.add(Sum(sz) == N)

# print(str(s))

if s.check() == sat:
  print(s.model())













