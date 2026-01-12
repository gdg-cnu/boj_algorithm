
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 동전의 가치가 오름차순으로 주어진다
# 가치의 합을 K로 만들려고 하는데, 필요한 동전의 개수 구하기 
# 동전은 중복해서 사용 가능하다 

coins = {}

for _ in range(n):
  x = int(input())
  coins[x] = 0

# 동전의 종류는 1, 5, 10, 50, 500, 1000, 5000, 10000, 50000
# 일단 천의자리로 끊는다
# 그리고 백의자리 끊고, 그 다음 십의자리 끊고 일의자리 끊는다 

for coin in sorted(coins.keys(), reverse = True):
  cnt = k // coin
  coins[coin] = cnt
  k -= cnt * coin

print(sum(coins.values()))