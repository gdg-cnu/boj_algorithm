import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N+1)

# 이렇게 재귀를 나타낼 수 있다 
def find(a):
  if a == parent[a]:
    return a 
  else:
    parent[a] = find(parent[a])
    return parent[a]

# 합집합 연산 
# 두개를 각각 찾는다 
# 만약 다르면 b의 부모에 a를 대입한다 
def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

# 두개가 같은지 체크한다 
def checkSame(a, b):
  # a와 b를 각각 찾고
  a = find(a)
  b = find(b)
  if a == b:
    # 같으면 true
    return True
  # 아니면 false 배출
  return False

# 처음에 부모 노드리스트에 대입해준다 
for i in range(0, N+1):
  parent[i] = i

# qusetion 기준으로 나눠주고 0이면 합집합, 1이면 두개가 같은지 체크해주느느거 
# true false 기준으로 if문 나눠준다 
for i in range(M):
  question, a, b = map(int, input().split())
  if question == 0:
    union(a,b)
  else:
    if checkSame(a,b):
      print("YES")
    else:
      print("NO")

