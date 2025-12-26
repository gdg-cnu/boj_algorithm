#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11279                          #+#        #+#      #+#     #
#    Solved: 2025/12/26 15:15:43 by b_backyard    ###          ###   ##.kr     #
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
        if heap:  # 비어있지 않으면 최대값 출력
            print(-heapq.heappop(heap))
        else:     # 비어있으면 0 출력
            print(0)
    else:
        # 최대 힙처럼 쓰기 위해 음수로 저장
        heapq.heappush(heap, -x)
