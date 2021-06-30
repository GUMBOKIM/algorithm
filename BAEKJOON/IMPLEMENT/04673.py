self = {int(i) for i in range(1, 10001)}
not_self = set()

iter = 1
while True:
    result = iter
    quotient = iter
    each = []

    while quotient > 0:
        quotient, remainder = divmod(quotient, 10)
        if not remainder == 0:
            each.append(remainder)

    result += sum(each)

    # 10035 = 9999 + 9 + 9 + 9 + 9
    if result > 10035:
        break

    not_self.add(result)
    iter += 1

self = list(self - not_self)
self.sort()

for value in self:
    print(value)
