

m = int(input())

S = []
def add(x):
  S.append(x)

def remove(x):
  if x in S:
    S.remove(x)

def check(x):
  if x in S:
    return 1
  else:
    return 0

def toggle(x):
  if x in S:
    S.remove(x)
  else:
    S.append(x)

def all():
  S = list(range(1, 20))

def empty():
  S = []

output = []

for _ in range(m):
  command = []
  command = list(map(str, input().split()))
  if command[0] == "add":
    add(int(command[1]))
  elif command[0] == "remove":
    remove(int(command[1]))
  elif command[0] == "check":
    output.append(check(int(command[1])))
  elif command[0] == "toggle":
    toggle(int(command[1]))
  elif command[0] == "all":
    all()
  elif command[0] == "empty":
    empty

print("\n".join(map(str, output)))
