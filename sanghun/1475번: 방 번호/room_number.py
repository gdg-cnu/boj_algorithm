

from collections import Counter

n = int(input())

# 다솜이의 옆집에서는 플라스틱 숫자를 한세트로 판다
# 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다

# 필요한 세트의 개수의 최솟값 
# 6과 9는 서로 뒤집어서 사용 가능

digits = list(map(int, str(n)))
count = dict(Counter(digits))

if 6 in count or 9 in count:
  six = count.get(6, 0)
  nine = count.get(9, 0)
  count[6] = (six + nine +1) // 2
  count.pop(9, None)


print(max(count.values()))

