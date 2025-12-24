#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10828                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10828                          #+#        #+#      #+#     #
#    Solved: 2025/12/24 17:35:42 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

n = int(input())
stack = []  # list로 스택 구현

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))          # push
    elif cmd[0] == "pop":
        print(stack.pop() if stack else -1)  # pop
    elif cmd[0] == "size":
        print(len(stack))                  # size
    elif cmd[0] == "empty":
        print(0 if stack else 1)           # empty
    elif cmd[0] == "top":
        print(stack[-1] if stack else -1)  # top
