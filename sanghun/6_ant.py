

import sys
input = sys.stdin.readline

# 첫째 줄에는 탑의 수를 나타내는 정수 N이 주어진다
n = int(input())
# 탐의 높이를 순서대로 받는다 
heights = list(map(int, input().split()))

stack = []
answer = [0]*n

for i in range(n):
  h = heights[i]

  # 나보다 작은 탑들은 전부 폐기
  while stack and stack[-1][1] < h:
    stack.pop()
  
  # 남아 있다면 가장 가까운 큰(같은) 탑
  if stack:
    answer[i] = stack[-1][0]
  else:
    answer[i] = 0
  
  # 나는 다음 탑들의 후보
  stack.append((i+1, h))

print(*answer)
