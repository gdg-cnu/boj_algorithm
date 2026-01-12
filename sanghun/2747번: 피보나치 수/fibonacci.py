
import sys
input = sys.stdin.readline

N = int(input())

D = [-1]*(N+1)
D[0] = 0
D[1] = 1

def fibo(n):
  if D[n] != -1:
    return D[n]
  
  D[n] = fibo(n-2) + fibo(n-1)
  return D[n]

fibo(N)
print(D[N])


import sys
imput = sys.stdin.readline

N = int(input())
D = [-1]*(N+1)
D[0] = 0
D[1] = 1

for i in range(2, N+1):
  D[i] = D[i-2] + D[i-1]

print(D[N])