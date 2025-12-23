# 집합 n+1개가 있다 0~n
# 합집합 연산과
# 두 원소가 같은 집합에 포함되어있는지를 확인하는 연산 수행 

import sys
input = sys.stdin.readline

# m은 입력으로 주어지는 연산의 개수 
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(m):
  x, a, b  = map(int, input().split())
  # 합집합은 0 a b 형태로 입력이 주어진다 
  # 이는 a가 포함되어있는 집합과 b가 포함되어있는 집합을 합친다는 의미이다
  # 두 원소가 같은 집합에 포함되어있는지 확인하는 연산은 1 a b 형태로 입력이 주어짐
  # 이는 a와 b가 같은 집합에 포함되어있는지를 확인하는 연산
  def find(x):
    if parent[x] != x:
      parent[x] = find(parent[x])
    return parent[x]

  def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
      parent[rb] = ra    
  
  if x == 0:
    union(a, b)
  else:
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")
