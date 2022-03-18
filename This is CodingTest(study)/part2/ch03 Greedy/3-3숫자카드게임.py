# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

result = 2

def NumCardGame():
    row, column = input('').split(' ')
    min_card_list = []
    for card in range(int(row)):
        row_card_list = list(map(int, input('').split(' ')))
        min_card_list.append(min(row_card_list))
    print(max(min_card_list))

# NumCardGame()

def NumCardGame2():
    row, column = input('').split(' ')
    min_card = 0
    for card in range(int(row)):
        row_card_list = list(map(int, input('').split(' ')))
        min_card = max(min_card, min(row_card_list))
    print(min_card)

NumCardGame2()