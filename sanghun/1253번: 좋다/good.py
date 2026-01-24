import sys
input = sys.stdin.readline

result = 0
n = int(input())
A = list(map(int, input().split()))

# 정렬을 하는 이유는, 투 포인터를 쓰기 위한 전제조건
A.sort()


# 리스트의 수만큼 반복한다
for k in range(n):
  # 각 반복마다의 케이스 
  find = A[k]
  # 양끝에 포인터터를 위치시킨다
  i = 0
  j = n-1
  # i가 j 보다 작아야한다. 즉 양 끝에서 가운데로 이동하는 방향
  while i < j:
    # 두개의 포인터가 가리키는 값이 반복하는 수의 지정값이라면 
    if A[i] + A[j] == find:
      # 자기 자신을 사용하면 안된다
      if i != k and j != k:
        result += 1
        break
      elif i ==k:
        i += 1
      elif j == k:
        j -= 1
    elif A[i] + A[j] < find:
      i += 1
    else:
      j -= 1

print(result)