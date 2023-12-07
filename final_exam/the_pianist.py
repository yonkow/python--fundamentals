def operations(pieces, command):
    current_command = command[0]
    if current_command == "Add":
        piece, composer, key = command[1:]
        if piece not in pieces:
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif current_command == "Remove":
        piece = command[1]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            del pieces[piece]
    elif current_command == "ChangeKey":
        piece, new_key = command[1:]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    return pieces


def pieces_collection(n):
    # collection type: {piece: [composer, key]}
    pieces = {}
    for _ in range(n):
        current_piece = input().split("|")
        piece, composer, key = current_piece
        pieces[piece] = [composer, key]
    while True:
        command = input().split("|")
        if command[0] == "Stop":
            break
        else:
            pieces = operations(pieces, command)
    return pieces


number_of_pieces = int(input())
collections = pieces_collection(number_of_pieces)

for print_piece, value in collections.items():
    current_composer, current_key = value
    print(f"{print_piece} -> Composer: {current_composer}, Key: {current_key}")