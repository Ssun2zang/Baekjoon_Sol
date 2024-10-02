# 돌 N개가 있음
# 둘이 돌아가며 돌 1개 또는 3개를 가져감
# 마지막 돌을 가져가는 사람이 이김
# 완벽하게 게임을 했을 때 이기는 사람 구하기
# 게임은 상근이가 먼저 시작함 -> SK
# 창영이는 CY
import sys
input = sys.stdin.readline

N = int(input())
print("CY" if N%2 ==0 else "SK")