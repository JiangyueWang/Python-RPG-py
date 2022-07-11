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
