#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9935                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9935                           #+#        #+#      #+#     #
#    Solved: 2026/01/01 23:53:53 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

S = input().rstrip()
B = input().rstrip()
m = len(B)

stack = []
last = B[-1]  # 마지막 글자 같을 때만 비교하면 약간 최적화됨

for ch in S:
    stack.append(ch)

    # 폭발 문자열의 마지막 글자와 같을 때만 검사 (최적화)
    if ch == last and len(stack) >= m:
        if ''.join(stack[-m:]) == B:
            del stack[-m:]  # 폭발 제거

result = ''.join(stack)
print(result if result else "FRULA")
