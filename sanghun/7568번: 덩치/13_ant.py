# 사람의 덩치를 키와 몸무게 이 두개의 값으로 표현하여 그 등수를 매겨보려고 한다.
#  키와 몸무게가 둘다 크면 더 크다고 한다
# 서로 다른 덩치끼리 크기를 정할 수 없는 경우가 있는데 그거는 섞여있을때
# 각 사람마다 본인의 등수를 매긴다 x, y가 둘다 나보다 크면 나보다 위 등수

people = []

n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  people.append((x, y))

output = []
for (x, y) in people:
  rank = 1
  for (a, b) in people:
    if a > x and b > y:
      rank +=1
  output.append(rank)

print(" ".join(map(str, output)))