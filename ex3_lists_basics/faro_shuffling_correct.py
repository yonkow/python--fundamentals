starting_deck = input().split()
turns_of_shuffle = int(input())
current_deck = starting_deck

for shuffle in range(turns_of_shuffle):
    new_deck = []
    half_deck = len(current_deck) // 2
    left_half = current_deck[:half_deck]
    right_half = current_deck[half_deck:]

    for index in range(len(left_half)):
        new_deck.append(left_half[index])
        new_deck.append(right_half[index])

    current_deck = new_deck
print(current_deck)