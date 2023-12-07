def the_game(party_collection):
    while True:
        command = input().split(' - ')
        if command[0] == "End":
            break
        current_command = command[0]
        if current_command == "CastSpell":
            hero_name, mana_needed, spell_name = command[1], int(command[2]), command[3]
            if party_collection[hero_name]['MP'] >= mana_needed:
                party_collection[hero_name]['MP'] -= mana_needed
                mana_left = party_collection[hero_name]['MP']
                print(f"{hero_name} has successfully cast {spell_name} and now has {mana_left} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        elif current_command == "TakeDamage":
            hero_name, damage, attacker = command[1], int(command[2]), command[3]
            party_collection[hero_name]['HP'] -= damage
            if party_collection[hero_name]['HP'] > 0:
                current_hp = party_collection[hero_name]['HP']
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                del party_collection[hero_name]
        elif current_command == "Recharge":
            hero_name, amount = command[1], int(command[2])
            party_collection[hero_name]['MP'] += amount
            if party_collection[hero_name]['MP'] <= 200:
                print(f"{hero_name} recharged for {amount} MP!")
            else:
                amount_recovered = amount - (party_collection[hero_name]['MP'] - 200)
                print(f"{hero_name} recharged for {amount_recovered} MP!")
                party_collection[hero_name]['MP'] = 200
        elif current_command == "Heal":
            hero_name, amount = command[1], int(command[2])
            party_collection[hero_name]['HP'] += amount
            if party_collection[hero_name]['HP'] <= 100:
                print(f"{hero_name} healed for {amount} HP!")
            else:
                amount_recovered = amount - (party_collection[hero_name]['HP'] - 100)
                print(f"{hero_name} healed for {amount_recovered} HP!")
                party_collection[hero_name]['HP'] = 100
    return party_collection


def invite_heroes(number):
    party_collection = {}
    # party_collection = {hero_name: {'HP': hit_points, 'MP': mana_points}}
    for _ in range(number):
        current_hero, hit_points, mana_points = input().split(' ')
        party_collection[current_hero] = {'HP': int(hit_points), 'MP': int(mana_points)}
    party_collection = the_game(party_collection)
    return party_collection


number_of_heroes = int(input())
party = invite_heroes(number_of_heroes)
for hero, elements in party.items():
    print(hero)
    print(f"  HP: {elements['HP']}")
    print(f"  MP: {elements['MP']}")