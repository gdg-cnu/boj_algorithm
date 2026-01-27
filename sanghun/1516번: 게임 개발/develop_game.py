from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]
# 진입 차수 리스트
indegree = [0] * (N+1)
# 자기 자신을 짓는데 걸리는 시간
selfBuild = [0] * (N+1)

for i in range(1, N+1):
  # 한줄씩 입력받아서 리스트로 저장한다 
  inputList = list(map(int, input().split()))
  # 지금 내거 걸리는시간 저장한다 
  selfBuild[i] = (inputList[0])
  # 처음 시작을 지정하는 인덱스 
  index = 1
  # 계속 수행
  while True:
    # 앞에거 걸리는 시간을 본다. 그리고 inputList에서 두번째 부터 앞에 걸리는 시간 저장하기 
    preTemp = inputList[index]
    # 그리고 혹시 그 다음에 있는지 확인하기 
    index += 1
    # 그 인덱스의 값이 -1이 나온다면 멈춘다 
    if preTemp == -1:
      break
    # preTemp = 선행건물
    # i = 현재 건물 
    A[preTemp].append(i)

    indegree[i] += 1

queue = deque()

for i in range(1, N+1):
  # 앞에 지어야하는게 없다면
  if indegree[i] == 0:
    # 바로 큐에 넣는다, 즉 이거부터 실행한다 
    queue.append(i)

result = [0] * (N+1)

while queue: # 위상 정렬 수행
  now = queue.popleft()
  for next in A[now]:
    indegree[next] -= 1
    # 시간 업데이트
    result[next] = max(result[next], result[now] + selfBuild[now])
    if indegree[next] == 0:
      queue.append(next)

for i in range(1, N+1):
  print(result[i] + selfBuild[i])
