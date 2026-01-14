# import sys
# input = sys.stdin.readline

# c = int(input())
# n = int(input())
# A = [[] for _ in range(c+1)]
# visited = [False] * (c+1)

# for _ in range(n):
#   s, e = map(int, input().split())
#   A[s].append(e)
#   A[e].append(s)

# def DFS(v):
#   global count
#   visited[v] = True
#   for i in A[v]:
#     if not visited[i]:
#       count +=1

#       DFS(i)

# count = 0
# DFS(1)
# print(count)









