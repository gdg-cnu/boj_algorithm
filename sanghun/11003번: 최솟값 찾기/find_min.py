from collections import deque

import sys
input = sys.stdin.readline

mydeque = deque()

n, l = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
  while mydeque and mydeque[-1][0] > A[i]:
    mydeque.pop()
  mydeque.append((A[i], i))
  if mydeque[0][1] <= i - l:
    mydeque.popleft()
  
  print(mydeque[0][0], end = ' ')





N  =int(input())
A = [0]*N

for i in range(N):
  A[i] = int(input())

for i in range(N-1):
  for j in range(N-1-i):
    if A[j] > A[j+1]:
      temp = A[j]
      A[j] = A[j+1]
      A[j+1] = temp 

for i in range(N):
  print(A[i])
