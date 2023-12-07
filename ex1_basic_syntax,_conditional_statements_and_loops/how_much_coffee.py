current_task = input()
number_of_coffee = 0
while current_task != "END":
    all_task_low = current_task.lower()
    if all_task_low == "coding" or all_task_low == "dog" or all_task_low == "cat" or all_task_low == "movie":
        if current_task.islower():
            number_of_coffee += 1
        elif current_task.isupper():
            number_of_coffee += 2
    current_task = input()
if number_of_coffee > 5:
    print("You need extra sleep")
else:
    print(number_of_coffee)