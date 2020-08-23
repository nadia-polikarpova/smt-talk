from z3 import *

# Partition range [1, N) evenly into P sub-ranges

s = Solver()

N = Int('N')
s.add(N == 10)
P = 4

K = 2
# K = N / P
# K = N % P

sz = [If(i < K, N / P + 1, N / P) for i in range(P)]

# Even partitions:
for i in range(P):
  for j in range(P):
    s.add(sz[i] - sz[j] <= 1)

# Add up to N:
s.add(Sum(sz) == N)

if s.check() == sat:
  print(s.model())