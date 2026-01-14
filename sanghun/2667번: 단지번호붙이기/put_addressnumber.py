from collections import deque

N = int(input())
A = [[0] * N for _ in range(N)]
# 위 오 아 왼
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visited = [[False] * N for _ in range(N)]

for i in range(N):
  number = list(input())
  for j in range(N):
    A[i][j] = int(number[j])

# print("\n".join(map))

output = []
def BFS(i, j):
  queue = deque()
  visited[i][j] = True
  count = 1
  queue.append((i, j))
  while queue:
    now_Node = queue.popleft()
    for k in range(4):
      go_x = now_Node[0] + dx[k]
      go_y = now_Node[1] + dy[k]
      if go_x >= 0 and go_y >= 0 and go_x < N and go_y < N:
        if not visited[go_x][go_y] and A[go_x][go_y] != 0:
          visited[go_x][go_y] = True
          queue.append((go_x, go_y))
          count += 1
  return count

def BFS(i,j):
  queue = deque()
  visited[i][j] = True
  queue.append((i,j))
  count = 1
  while queue:
    now_Node = queue.popleft()
    for k in range(4):
      nx = now_Node[0] + dx[k]
      ny = now_Node[1] + dy[k]
      if nx >= 0 and nx < N and ny >= 0 and ny < N:
        if not visited[nx][ny] and A[nx][ny] == 1:
          visited[nx][ny] = True
          queue.append((nx, ny))
          count +=1
  return count









result = []

for i in range(N):
  for j in range(N):
    if A[i][j] == 1 and not visited[i][j]:
      result.append(BFS(i,j))

result.sort()
print(len(result))
for x in result:
  print(x)