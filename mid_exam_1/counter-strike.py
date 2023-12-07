def counter_strike(current_energy, current_distance, won_counter, condition):
    if current_distance <= current_energy:
        won_counter += 1
        current_energy -= current_distance
    else:
        condition = True
        print(f"Not enough energy! Game ends with {won_counter} won battles and {energy} energy")
    if won_counter % 3 == 0:
        current_energy += won_counter
    return current_energy, won_counter, condition


energy = int(input())
command = input()
won_matches = 0
end_condition = False
while command != "End of battle":
    distance = int(command)
    if distance > 0:
        energy, won_matches, end_condition = counter_strike(energy, distance, won_matches, end_condition)
    if end_condition:
        break
    else:
        command = input()

if command == "End of battle":
    print(f"Won battles: {won_matches}. Energy left: {energy}")

