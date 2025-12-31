#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1654                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1654                           #+#        #+#      #+#     #
#    Solved: 2025/12/31 22:10:05 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left, right = 1, max(lines)   # 길이는 1 이상
answer = 0

while left <= right:
    mid = (left + right) // 2  # 후보 길이
    cnt = 0
    for x in lines:
        cnt += x // mid

    if cnt >= N:              # N개 이상 만들 수 있으면 길이를 늘려본다
        answer = mid
        left = mid + 1
    else:                     # 부족하면 길이를 줄인다
        right = mid - 1

print(answer)
