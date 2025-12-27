# 색종이 수 
n = int(input())

matrix = [[0]*100 for _ in range(100)]

for _ in range(n):
  a, b = map(int, input().split())
  # a = a-1
  # b = b-1
  # a~a+10까지 1로 전환 / b~b+10까지 1로 전환
  for i in range(a, a + 10):
      for j in range(b, b + 10):
          matrix[i][j] = 1

count = sum(row.count(1) for row in matrix)

print(count)





# 총 길이는 100*100
# 가로 세로의 크기가 각각 100, 가로 세로 크기가 각각 10 
# 붙인 위치가 주어지고 거기서 이제 겹치는 영역을 빼주면 된다 
# 이거는 빼기보다는 최종 검정 면적을 구하는게 더 쉬울듯

