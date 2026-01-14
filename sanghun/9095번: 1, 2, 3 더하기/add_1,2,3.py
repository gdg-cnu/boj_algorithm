import sys
input = sys.stdin.readline


n = int(input())

# 동적 프로그래밍에는 탑 다운, 바텀 업 방식이 있다
# n을 1,2,3의 합으로 나타내는 방법의 수 

# 문제에서 n<=10 이므로 미리 전부 계산

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(n):
  x = int(input())
  print(dp[x])


# 이건 조합을 만들어야한다고 생각
# 개수엔 제한이 없다
# 우선 하나씩 작은문제 부터 해결해가면, 1로서 다 더해가면서 풀기
# 2 섞기 
# 3으로 

# 이거는 탑다운이 맞을거같다. 3으로 최대한 해보고, 그 다음 하나씩 빼가면서 푸는거다


