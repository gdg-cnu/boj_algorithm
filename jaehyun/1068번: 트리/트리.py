#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1068                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1068                           #+#        #+#      #+#     #
#    Solved: 2026/01/02 23:02:13 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
d = int(input())

child = [[] for _ in range(n)]
root = -1
for i, par in enumerate(p):
    if par == -1:
        root = i
    else:
        child[par].append(i)

if d == root:
    print(0)
    sys.exit()

ans = 0
def dfs(u):
    global ans
    if u == d:
        return
    # 삭제 노드를 제외한 실제 자식들
    kids = [v for v in child[u] if v != d]
    if not kids:
        ans += 1
        return
    for v in kids:
        dfs(v)

dfs(root)
print(ans)
