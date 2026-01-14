from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
  numbers = list(input())
  for j in range(M):
    A[i][j] = int(numbers[j])

def BFS(i,j):
  queue = deque()
  queue.append((i,j))
  visited[i][j] = True
  while queue:
    now = queue.popleft()
    for k in range(4):
      x = now[0] + dx[k]
      y = now[1] + dy[k]
      if x >= 0 and y >=0 and x < N and y < M:
        if A[x][y] != 0 and not visited[x][y]:
          visited[x][y] = True
          A[x][y] = A[now[0]][now[1]] + 1
          queue.append((x,y))

BFS(0,0)
print(A[N-1][M-1])














# BFS 는 큐로 진행
from collections import deque

# 위 오 아 왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
# 이거는 총 미로를 0으로 채워준다 
A = [[0] * M for _ in range(N)]
# 각 위치마다 False를 넣어준다
visited = [[False] * M for _ in range(N)]

# number를 입력받고 미로에서 1인거는 채워주기 위해서 이런 코드 작성
for i, j in range(N):
  numbers = list(input())
  for j in range(M):
    A[i][j] = int(numbers[j])

# BFS 코드 작성 행과 열을 입력 받는다
def BFS(i, j):
  queue = deque()
  # 큐에 넣어주고
  queue.append((i,j))
  # 미로에서 방문한거는 True로 바꿔준다
  visited[i][j] = True
  # 큐가 빌 때까지
  while queue:
    # 제일 왼쪽에 있는걸 빼준다
    now = queue.popleft()
    # 위 오 아 왼을 순회하기 위한 range
    for k in range(4):
      x = now[0] + dx[k]
      y = now[1] + dy[k]
      if x >= 0 and y >= 0 and x < N and y < M:
        if A[x][y] != 0 and not visited[x][y]:
          visited[x][y]  = True
          A[x][y] = A[now[0]][now[1]] + 1
          queue.append((x, y))

BFS((0,0))
print(A[N-1][M-1])


