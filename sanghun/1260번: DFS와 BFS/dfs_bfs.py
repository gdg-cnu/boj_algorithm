# 정점의 개수 n 
# 간선의 개수 m
# 탐색을 시작할 정점의 번호 v

# 일단 노드들을 다 넣고
# 노드 사이의 간선도 넣는다 
# 연결된것을 인지를 해야한다 
# 간선을 어떤 노드 사이인지 구분해서 잘 넣어야할듯 하다
# 일단 노드가 연결된 것을 표현하는게 맞다
# 어떤 자료구조로 표현할까
# 리스트 딕셔너리 
# 각 노드마다 연결된 거를 추가해주는게 좋을거같긴하다

from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N+1)]


for _ in range(M):
  s, e = map(int, input().split())
  A[s].append(e)
  A[e].apppend(s)

for i in range(N + 1):
  A[i].sort()

def DFS(v):
  print(v, end = ' ')
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      DFS(i)

visited = [False] * (N + 1)
DFS(Start)


def BFS(v):
  queue = deque()
  queue.append(v)
  visited[v] = True
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

