def shooting(target: list, shoot: int, counter: int):
    shot_target = target[shoot]
    if target[shoot] != -1:
        target[shoot] = -1
        counter += 1
        for index, current_target in enumerate(target):
            if index == shoot:
                continue
            else:
                if current_target <= shot_target and current_target != -1:
                    target[index] += shot_target
                elif current_target > shot_target and current_target != -1:
                    target[index] -= shot_target
    return target, counter


shooting_targets = [int(index) for index in input().split()]
command = input()
shot_counter = 0

while command != "End":
    current_shoot = int(command)
    if current_shoot < len(shooting_targets):
        shooting_targets, shot_counter = shooting(shooting_targets, current_shoot, shot_counter)
    command = input()

if command == "End":
    print(f"Shot targets: {shot_counter} -> {' '.join(str(target) for target in shooting_targets)}")