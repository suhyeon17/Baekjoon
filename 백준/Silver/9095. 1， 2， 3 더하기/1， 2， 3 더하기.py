# 다이나믹 프로그래밍으로 구현
t = int(input())
test = []
for _ in range(t):
    test.append(int(input()))

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in range(t):
    print(dp[test[i]])