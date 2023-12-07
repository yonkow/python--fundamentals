starting_deck = input().split()
turns_of_shuffle = int(input())
turns_counter = 0
current_deck = starting_deck
while turns_of_shuffle > turns_counter:
    turns_counter += 1
    first_half = []
    second_half = []

    for index, value in enumerate(current_deck):
        if index < len(current_deck)/2:
            first_half.append(value)
        else:
            second_half.append(value)

    first_deck_counter = 0
    second_deck_counter = 0
    new_deck = []
    for position in range(len(current_deck)):
        if position % 2 == 0:
            new_deck.append(first_half[first_deck_counter])
            first_deck_counter += 1
        else:
            new_deck.append(second_half[second_deck_counter])
            second_deck_counter += 1

    current_deck = new_deck
print(current_deck)