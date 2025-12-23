# 뱀이 나와서 기어다니는데 사과를 먹으면 뱀 길이가 늘어난다
# 자기자신의 몸과 부딪히면 게임이 끝남

# n*n 정사각 보드에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다 
# 보드의 상하좌우 끝에 벽이 있다

# 게임 시작할때는 맨위 좌측에 위치하고 뱀의 길이는 1
# 처음에 오른쪽을 향함

# 몸길이를 늘려 머리를 다음칸에 위치
# 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다
# 이동한 칸에 사과가 있다면 그 칸에있던 사과는 없어지고 꼬리는 움직이지 않음
# 사과가 없으면 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다 즉 몸길이는 변하지 않는다

from collections import deque
snake = deque()
# 처음 위치
snake.append((0,0))

# 보드의 크기
n = int(input())
# 사과의 개수
k = int(input())

map_size = [[0]*n for _ in range(n)]

# 사과의 위치 표시하기 
for _ in range(k):
  a, b = map(int, input().split())
  map_size[a-1][b-1] = 1


L = int(input())

# 이동하는거를 기록하기 위한 딕셔너리
turn = {}
for _ in range(L):
    x, c = input().split()
    turn[int(x)] = c

# 게임 시간 초 
time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0
x, y = 0,0

while True:
  # 뱀의 이동을 표현한다 리스트에 하나씩 더해가면서
    time +=1    
    # 다음 머리 위치 계산
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 벽 충돌 검사
    if nx<0 or nx >= n or ny <0 or ny >=n:
      print(time)
      break    
    # 자기 몸 충돌 검사 
    if (nx, ny) in snake:
      print(time)
      break
    
    # 머리 추가 
    snake.appendleft((nx, ny))

    # 사과 여부에 따른 처리 
    if map_size[nx][ny] ==1:
      map_size[nx][ny] = 0
    else:
      snake.pop()

    # 현재 위치 갱신
    x, y = nx, ny

    if time in turn:
      if turn[time] == "D":
        dir = (dir + 1) % 4
      else:
        dir = (dir -1) % 4









  # # 방향은 이렇게 이분법적으로 정해놓았다 
  # # true이면 오른쪽 false이면 아래다
  # # 즉 true이면 열번호가 증가하고 false이면 행번호가 증가한다
  # if b == "D":
  #   direct = False
  # elif b == "L":
  #   direct = True