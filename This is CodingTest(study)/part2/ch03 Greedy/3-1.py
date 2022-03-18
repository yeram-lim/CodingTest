N = 1260

def charge(N):
    coin = [500, 100, 50, 10]
    answer = 0
    while(N):
        i = 0
        answer += N / coin[i]
        N = N % coin[i]
        i += 1
    return answer

print(charge(N))