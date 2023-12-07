fires_n_cells = input().split("#")
amount_of_water = int(input())
counter = 0
cells_list = []

while counter < len(fires_n_cells):
    current_fire = counter
    fire = fires_n_cells[current_fire].split(" = ")
    type_of_fire = fire[0]
    cell_range = int(fire[1])
    if amount_of_water < cell_range:
        counter += 1
        continue
    if type_of_fire == "High" and 81 <= cell_range <= 125:
        amount_of_water -= cell_range
        cells_list.append(cell_range)
    elif type_of_fire == "Medium" and 51 <= cell_range <= 80:
        amount_of_water -= cell_range
        cells_list.append(cell_range)
    elif type_of_fire == "Low" and 1 <= cell_range <= 50:
        amount_of_water -= cell_range
        cells_list.append(cell_range)
    counter += 1

effort = sum(cells_list) * 0.25
print("Cells:", *cells_list, sep="\n- ")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells_list)}")