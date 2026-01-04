
from datetime import date, datetime

n = int(input())

people = []
for _ in range(n):
  name, day, month, year = input().split()
  birthday = date(int(year), int(month), int(day))
  people.append((name,birthday))

youngest = max(people, key= lambda x: x[1])
print(youngest[0])

oldest = min(people, key= lambda x: x[1])
print(oldest[0])