# n은 홀수라고 가정하고 네가지 기본 통계를 구한다
# 산술평균은 n개의 수를 n으로 나눈 값이고
# 중앙값은 수를 증가하는 순서로 나열했을경우 그 중간값
# 최빈값은 n개의 수들중 가장 많은값
# 범위는 n개의 수들중 최댓값과 최솟값의 차이
# 수들은 음수들도 주어진다

import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())

arr = []
for _ in range(n):
  x = int(input())
  arr.append(x)

arr.sort()
# 평균 계산
avg = sum(arr)/n

# 중앙값 계산
median = arr[len(arr)//2]

# 최빈값 계산
cnt = Counter(arr)
max_freq = max(cnt.values())

modes = [k for k, v in cnt.items() if v == max_freq]
modes.sort()
answer = modes[0] if len(modes) == 1 else modes[1]

print(int(avg+0.5) if avg > 0 else int(avg - 0.5))
print(median)
print(answer)
print(max(arr) -  min(arr))

