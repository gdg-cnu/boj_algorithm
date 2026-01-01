# 크기가 n*n
# 각 칸은 빈칸, 치킨집, 집 중 하나 
# 치킨 거리라는 의미 
# 집과 가장 가까운 치킨집 사이의 거리 
# 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 치킨거리의 합니다 

# 0은 빈칸, 1은 집, 2는 치킨집 
# 집의 개수는 2n개를 넘지 않는다, 적어도 1개는 존재한다. 
# 치킨집의 개수는 m보다 크거나 같고 13보다 작거나 같다 

from itertools import combinations

n, m = map(int, input().split())

city = []
house = []
chicken = [] 
for _ in range(n):
  row = list(map(int, input().split()))
  city.append(row)

# 이 도시에 있는 치킨집은 모두 같은 프렌차이즈, 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업하고자 함
# 이 도시에서 가장 수익을 많이 낼 수 잇는 치킨지브이 개수는 m개
# 수익을 최대화 할 m개의 치킨집을 고르고 나머지 치킨집은 모두 폐업 시켜야함
# 어떻게 고르면 도시의 치킨거리가 가장 작게 될까

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      house.append((i+1,j+1))
    elif city[i][j] == 2:
      chicken.append((i+1,j+1))

answer = float('inf')

for comb in combinations(chicken, m):
    city_dist = 0

    for (hx, hy) in house:
        min_dist = float('inf')
        for (cx, cy) in comb:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)

        city_dist += min_dist

    answer = min(answer, city_dist)

print(answer)




# each_chicken_average =[]
# house_chicken_total = []
# for (i,j) in chicken:
#   dist_sum = 0
#   for (a,b) in house:
#     dist_sum += abs(a-i) + abs(b-j)
  
#   avg = dist_sum / len(house)
#   each_chicken_average.append(avg)

# # print(*each_chicken_average)

# paired = list(zip(chicken, each_chicken_average))
# paired.sort(key = lambda x: x[1])
# paired = paired[:m]
# # print(paired)

# total = 0
# for i in paired:
#   total += i[1]

# # print(total)

# for (hx, hy) in house:
#   min_dist = float('inf')
#   for (pos, _) in paired:
#     cx, cy = pos
#     dist = abs(hx- cx) + abs(hy - cy)
#     min_dist = min(min_dist, dist)

#   house_chicken_total.append(min_dist)

# print(sum(house_chicken_total))
