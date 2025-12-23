
# 사이트 수, 비밀번호 수 
# 공백으로 구분되어 주어짐
# 사이트 주소는 알파벳 소문자, - . 로 이루어짐, 중복되지 않음
# 알파벳은 대문자로만 이루어짐

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# n+2 부터 m개의 줄에 거쳐 비밀번호를 찾으려는 사이트 주소가 하나씩ㅇ ㅣㅂ력된다 


dict = {}
for _ in range(n):
  site, password = input().split()
  dict[site] = password

find = []
for _ in range(m):
  x = str(input().strip())
  find.append(dict[x])

print("\n".join(find))
