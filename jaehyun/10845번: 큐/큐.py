#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10845                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10845                          #+#        #+#      #+#     #
#    Solved: 2025/12/25 23:51:44 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        print(q.popleft() if q else -1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        print(0 if q else 1)
    elif cmd[0] == "front":
        print(q[0] if q else -1)
    elif cmd[0] == "back":
        print(q[-1] if q else -1)
