from sys import stdin

##규칙 : 최대값 * (n-1) * 2 - (각 항들과 최대값의 차이의 합)

card_count = int(stdin.readline())
card_list = list(map(int, stdin.readline().split(" ")))

max_card = max(card_list)
result = max_card * (card_count - 1) * 2

for card in card_list:
    if (card < max_card):
        result -= (max_card - card)

print(result)
