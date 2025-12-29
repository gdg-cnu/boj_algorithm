#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1927                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1927                           #+#        #+#      #+#     #
#    Solved: 2025/12/29 15:45:43 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    
    if x == 0:
        if heap:              # 비어있지 않으면 최소값 출력
            print(heapq.heappop(heap))
        else:                 # 비어있으면 0 출력
            print(0)
    else:
        # heapq는 기본이 최소 힙이라 그대로 넣으면 됨
        heapq.heappush(heap, x)
