# 정렬된 두 묶음의 숫자 카드가 있다 각 묵음의 카드 수 a, b
# 두 묶음을 합쳐서 하나로 만드는데 a+b의 비교를 해야함

# 두 묶음씩 골라서 서로 합쳐나가면 고르는 순서에 따라서 비교횟수가 매우 달라짐
# 이제 횟수를 줄이려면 큰거 먼저해서 순서대로 해서 횟수를 줄일 수 있다

# n개의 숫자 카드 묶음의 각각의 크기가 주어질 때 최소한 몇번의 비교가 필요한지 구해라
# 우선 숫자가 큰 순서대로 진행을 해야한다

# from collections import deque
import heapq


n = int(input())
arr = []
for _ in range(n):
  x = int(input())
  arr.append(x)

heapq.heapify(arr)

count = 0
# 적은거부터 더해가는게 최선인가?
for _ in range(len(arr)-1):
  x = heapq.heappop(arr)
  y = heapq.heappop(arr)
  new = x + y
  count += new
  heapq.heappush(arr, new)

print(count)