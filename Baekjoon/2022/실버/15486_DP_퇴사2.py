import sys
input = sys.stdin.readline

days = int(input())
period_list = [] #[3, 5, 1, 1, 2, 4, 2]
pay_list = [] #[10, 20, 10, 20, 15, 40, 200]
dp = [0] * (days + 1) #[0, 0, 0, 0, 0, 0, 0, 0]

for i in range(days):
    period, pay = map(int, input().split())
    period_list.append(period)
    pay_list.append(pay)

M = 0

for i in range(days):
    M = max(M, dp[i])
    if i + period_list[i] > days:
        continue
    dp[i + period_list[i]] = max(M + pay_list[i], dp[i + period_list[i]])

print(max(dp))