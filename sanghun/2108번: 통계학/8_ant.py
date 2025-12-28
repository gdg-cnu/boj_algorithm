# n은 홀수라고 가정하고 네가지 기본 통계를 구한다
# 산술평균은 n개의 수를 n으로 나눈 값이고
# 중앙값은 수를 증가하는 순서로 나열했을경우 그 중간값
# 최빈값은 n개의 수들중 가장 많은값
# 범위는 n개의 수들중 최댓값과 최솟값의 차이
# 수들은 음수들도 주어지고 

from collections import Counter

n = int(input())

arr = []
for _ in range(n):
  x = int(input())
  arr.append(x)

arr.sort()
median = arr[len(arr)//2]


print(round(sum(arr)/n, 0))
print(median)
print(max(arr) -  min(arr))