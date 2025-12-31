#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2512                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2512                           #+#        #+#      #+#     #
#    Solved: 2025/12/31 22:09:38 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())

left, right = 0, max(A)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(min(a, mid) for a in A)

    if total <= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
