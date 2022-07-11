import random


def run():
    print("You are Hercules, the greatest of the Greek Heroes! You have been tasked by King Eurystheus to slay the vicious Nemean Lion, defeat the impossible nine-headed Lernaean Hydra, and capture the guard dog of the underworld—Cerberus.")


hercules_dictionary = {
    "health": 130,

    "attack_names_dictionary": {
        "attack_1": 10,
        "attack_2": 20,
        "attack_3": 35,

    }
}

enemies_list = [

    {"enemy_name": "nemean_lion",
     "health": 100,
     "attack_names_dictionary": {
         "1": 5,
         "2": 10,
         "3": 40,
     }
     },
    {"enemy_name": "nine_headed_lernaean_hydra",
     "health": 140,
     "attack_names_dictionary": {
         "1": 10,
         "2": 5,
         "3": 50,
         "4": 6
     }
     },

    {"enemy_name": "guard_dog",
     "health": 120,
     "attack_names_dictionary": {
         "1": 15,
         "2": 38,
         "3": 12,
         "4": 9,
         "5": 21,
     }
     },
]


def utility_rand_list_item(list_input):
    # return an random item from a list
    random_list_item_index = random.randint(0, (len(list_input)-1))
    return random_list_item_index


def select_hercules_attack(attack_names_dictionary):
    # asked user to select an attack for hercules
    print(
        f'here are the attackes your choose for hercules {attack_names_dictionary}')
    user_choose_attack = input(
        "Eneter 1 or 2 or 3 to select attach for hercules: ")
    if user_choose_attack == "1":
        selected_hercules_attack = "attack_1"
        selected_hercules_attack_power = attack_names_dictionary[selected_hercules_attack]
        return selected_hercules_attack, selected_hercules_attack_power
    elif user_choose_attack == "2":
        selected_hercules_attack = "attack_2"
        selected_hercules_attack_power = attack_names_dictionary[selected_hercules_attack]
        return selected_hercules_attack, selected_hercules_attack_power
    else:
        selected_hercules_attack = "attack_3"
        selected_hercules_attack_power = attack_names_dictionary[selected_hercules_attack]
        return selected_hercules_attack, selected_hercules_attack_power


rand_enemy_list = []


def rand_enemy():
    # random generate an enemy from enemy list
    # ensure the random generated enemy only occurred once
    has_enemy_occured = True
    while has_enemy_occured:
        rand_enemy_index = utility_rand_list_item(enemies_list)
        rand_enemy = enemies_list[rand_enemy_index]

        if rand_enemy in rand_enemy_list:
            has_enemy_occured = True
        else:
            rand_enemy_list.append(rand_enemy)
            rand_enemy = rand_enemy
            has_enemy_occured = False
    return rand_enemy


print("----------choosing attack for hercules----------")
user_selected_hercules_attack = select_hercules_attack(
    hercules_dictionary["attack_names_dictionary"])
user_selected_hercules_attack_power = user_selected_hercules_attack[1]
print(
    f'you have selected attack {user_selected_hercules_attack[0]} for hercules with attack power {user_selected_hercules_attack_power} ')
print("---------------------------------------------------")


print("----------generating enemy----------")
generated_enemy = rand_enemy()

print("----------generating enemy attack----------")
generated_enemy_attack_list = []
for i in generated_enemy["attack_names_dictionary"].keys():
    if i not in generated_enemy_attack_list:
        generated_enemy_attack_list.append(i)


def rand_enemy_attack_info(generated_enemy_attack_list):
    # generated the attack name for the enemy randomly
    rand_enemy_attack_index = utility_rand_list_item(
        generated_enemy_attack_list)
    rand_enemy_attack_name = generated_enemy_attack_list[rand_enemy_attack_index]
    # find the attack power for random generated enemy
    rand_enemy_rand_attack_power = generated_enemy["attack_names_dictionary"][rand_enemy_attack_name]
    return rand_enemy_attack_name, rand_enemy_rand_attack_power


generated_enemy_attack_name = rand_enemy_attack_info(
    generated_enemy_attack_list)[0]
generated_enemy_rand_attack_power = rand_enemy_attack_info(
    generated_enemy_attack_list)[1]

print(f'enemy {generated_enemy["enemy_name"]} has selected')
print(
    f'enemy attack name {generated_enemy_attack_name} has choosen with attack power {generated_enemy_rand_attack_power}')
