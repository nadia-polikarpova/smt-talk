from z3 import *

# Partition range [1, N) evenly into P sub-ranges

s = Solver()

N = Int('N')
P = 4

# K = 2
# K = N / P
K = N % P

sz = [If(i < K, N / P + 1, N / P) for i in range(P)]

# Even partitions:
for i in range(P):
  for j in range(P):
    s.push()    
    s.add(Not(sz[i] - sz[j] <= 1))
    if s.check() == sat:
      print('Uneven partitions!')
      print(s.model())
      exit()
    s.pop()

# Add up to N:
s.add(Not(Sum(sz) == N))
if s.check() == sat:
  print('Does not add up to N')
  print(s.model())
  print([s.model().evaluate(x) for x in sz])
  exit()

print('Verified for all N!')  













