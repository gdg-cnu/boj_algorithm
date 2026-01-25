import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [0]*M
visited = [False]*N

def backtrack(length):
  if length == M:
    print(' '.join(str(x + 1) for x in S))
    return
  
  for i in range(N):
    if not visited[i]:
      visited[i] = True
      S[length] = i
      backtrack(length + 1)
      visited[i] = False

backtrack(0)