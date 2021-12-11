import random
enemy = "A wild pokemon"
enemy_health = 100
enemy_turn = ["fire breath","ice beam","thunderbolt","leaf blade"]
enemy_move_1 = "fire breath"
enemy_move_2 = "ice beam"
enemy_move_3 = "thunderbolt"
enemy_move_4 = "leaf blade"
player_health = 100
player_move_1 = "hyperbeam"
player_move_2 = "dragon breath"
player_move_3 = "protect"
player_move_4 = "meteor"
player_input = input("What do you do? Attack, Run, Cry ")
if player_input == "Attack":
    move_selection = input("Choose an attack: hyperbeam, dragon breath, protect, or meteor. ")
    if move_selection == "hyperbeam":
        print("You've fucked him up! He's at 60 hp. ")
    elif move_selection == "dragon breath":
        enemy_health == 25 and print("That was super effective! Dragons are too OP. He's at 25 hp. ") and random.choice(enemy_turn)
    elif move_selection == "protect":
        player_health == player_health*1.25 and random.choice(enemy_turn)
    elif move_selection == "meteor":
        enemy_health == 80 and print("That wasn't very effective... your enemy can tank meteors bruh. he's at 80 hp. ") and random.choice(enemy_turn)
    else:
        print("That isn't a move you know, get fuked nerd lmao")
elif player_input == "Cry":
    print("Your bloodline is weak and will end with you.")
    