
S = str(input())

# set로 해서 중복을 관리하기 쉽게 하고자 하였다
arr = set()

# S 문자열의 원소들 하나씩 리스트에 더해서 개개 알파벳으로 만든다 
# 
for i in len(S):
  for j in len(S):
    x = S[i:j]
    arr.add(x)


print(arr)