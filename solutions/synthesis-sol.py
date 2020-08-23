from z3 import *

# Partition range [1, N) evenly into P sub-ranges

s = Solver()

N = Int('N')
s.add(N == 10)
P = 4

C = Int('C')
s.add(0 <= C, C <= 2)

K = If(C == 0, 2,
        If(C == 1, N / P, N % P))

sz = [If(i < K, N / P + 1, N / P) for i in range(P)]

# Even partitions:
for i in range(P):
  for j in range(P):
    s.add(sz[i] - sz[j] <= 1)

# Add up to N:
s.add(Sum(sz) == N)

if s.check() == sat:
  print(s.model())