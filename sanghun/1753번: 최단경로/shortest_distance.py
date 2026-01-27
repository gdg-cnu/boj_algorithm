import sys
input = sys.stdin.readline
from queue import PriorityQueue

# 정점의 개수 V / 간선의 개수 E 
V, E = map(int, input().split())
# 시작 정점의 번호
K = int(input())

# K -> i 최단 거리 
distance = [sys.maxsize] * (V + 1)
# 
visited = [False] * (V+1)
myList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
  u, v, w = map(int, input().split())
  myList[u].append((v, w))

q.put((0, K)) # K를 시작점으로 설정
distance[K] = 0

while q.qsize() > 0:
  current = q.get()
  c_v = current[1]
  if visited[c_v]:
    continue
  visited[c_v] = True
  for tmp in myList[c_v]:
    next = tmp[0]
    value = tmp[1]
    if distance[next] > distance[c_v] + value:
      distance[next] = distance[c_v] + value
      q.put((distance[next], next))

for i in range(1, V+1):
  if visited[i]:
    print(distance[i])
  else:
    print("INF")

