#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1991                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: b_backyard <boj.kr/u/b_backyard>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1991                           #+#        #+#      #+#     #
#    Solved: 2026/01/05 22:52:15 by b_backyard    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

def preorder(node):
    if node == '.':
        return
    print(node, end='')
    left, right = tree[node]
    preorder(left)
    preorder(right)

def inorder(node):
    if node == '.':
        return
    left, right = tree[node]
    inorder(left)
    print(node, end='')
    inorder(right)

def postorder(node):
    if node == '.':
        return
    left, right = tree[node]
    postorder(left)
    postorder(right)
    print(node, end='')

preorder('A'); print()
inorder('A'); print()
postorder('A'); print()
