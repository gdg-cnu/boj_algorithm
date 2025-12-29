
import sys
input = sys.stdin.readline

# 학점 * 과목 평점의 합을 학점의 총합으로 나눠야함
total = []
score = []

GPA = {}
GPA['A+'] = 4.5
GPA['A0'] = 4.0
GPA['B+'] = 3.5
GPA['B0'] = 3.0
GPA['C+'] = 2.5
GPA['C0'] = 2.0
GPA['D+'] = 1.5
GPA['D0'] = 1.0
GPA['F'] = 0


for _ in range(20):
  a, b, c = map(str, input().split())
  if c != 'P':
    total.append(float(b))
    score.append(float(b)*GPA[c])

print(sum(score)/sum(total))