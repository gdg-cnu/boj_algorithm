

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    A = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        A[y][x] = 1

    def BFS(i, j):
        queue = deque()
        visited[i][j] = True
        queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and A[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    worm = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1 and not visited[i][j]:
                BFS(i, j)
                worm += 1

    print(worm)
