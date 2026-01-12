# +, - 가 숫자의 구분디ㅏ 
# 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다
# 괄호를 적절히 잘 배치해서 최소값을 만들어야한다

answer = 0

# - 기준으로 쪼갠다
A = list(map(str, input().split("-")))

def mySum(i):
  sum = 0
  temp = str(i).split('+')
  for i in temp:
    sum += int(i)
  return sum

for i in range(len(A)):
  temp = mySum(A[i])
  if i == 0:
    answer += temp 
  else:
    answer -= temp

print(answer)

