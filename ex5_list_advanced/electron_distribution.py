number_of_electrons = int(input())
shell_position = 0
shells = []
while True:
    if number_of_electrons <= 0:
        break
    shell_position += 1
    current_shell = 2 * (shell_position ** 2)
    if number_of_electrons >= current_shell:
        shells.append(current_shell)
        number_of_electrons -= current_shell
    else:
        shells.append(number_of_electrons)
        number_of_electrons -= number_of_electrons

print(shells)