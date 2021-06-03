coin_count, sum = map(int, input().split(' '))

coin = list()
for i in range(0, coin_count):
    coin.append(int(input()))


result = 0
idx = coin_count - 1
while sum != 0:
    if sum >= coin[idx]:
        quotient = sum // coin[idx]
        if quotient != 0:
            result += quotient
            sum -= coin[idx]*quotient
    idx -= 1

print(result)
