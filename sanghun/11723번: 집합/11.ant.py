import sys
input = sys.stdin.readline
write = sys.stdout.write

m = int(input())

S = 0  # 비트마스크로 집합 표현 (1~20)

def add(x):
    global S
    S |= (1 << x)

def remove(x):
    global S
    S &= ~(1 << x)

def check(x):
    return 1 if (S & (1 << x)) else 0

def toggle(x):
    global S
    S ^= (1 << x)

def all_set():
    global S
    S = (1 << 21) - 2   # 1~20 비트만 1

def empty():
    global S
    S = 0

# 명령 → 함수 매핑
commands = {
    "add": add,
    "remove": remove,
    "check": check,
    "toggle": toggle,
    "all": all_set,
    "empty": empty
}

for _ in range(m):
    cmd = input().split()
    if len(cmd) == 2:
        res = commands[cmd[0]](int(cmd[1]))
        if res is not None:          # check인 경우만
            write(str(res) + "\n")   # 즉시 출력 (메모리 절약)
    else:
        commands[cmd[0]]()
