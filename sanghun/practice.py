from collections import deque
import sys
input = sys.stdin.readline


N, M, Start = map(int, input().split())

A = [[] * (N+1)]
visited = [[False] * (N+1)]

for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].append(s)

for i in range(N+1):
  A[i].sort()

def DFS(v):
  print(v, end= ' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      visited[i] = True
      DFS(i)


def DFS(v):
  print(v, end = ' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      visited[i] = True
      DFS(i)


def DFS(v):
  print(v, end = ' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      visited[i] = True
      DFS(i)



def BFS(v):
  queue = deque()
  visited[v] = True
  queue.append(v)
  while queue:
    now_Node = queue.popleft()
    print(now_Node, end = ' ')
    # 여기 방금 한거 헷갈리지 말자! 왜냐면 그 다음 while문 계속 돌리려면 이렇게 해줘야한다
    for i in A[now_Node]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)






def BFS(v):
  queue = deque()
  visited[v] = True
  queue.append(v)
  while queue:
    now_Node = queue.popleft()
    print(now_Node, end = ' ')
    for i in A[now_Node]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
print()
visited = [False] * (N+1)
BFS(Start)


D = [[0 for j in range(2)] for i in range(N+1)]

