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
while True:
    player_input = input("What do you do? Attack, Run, Cry, check enemy health, check my health ")
    if player_input == "check enemy health":
        print(enemy_health)
    if player_input == "check my health":
        print(player_health)
    if player_input == "run":
        print("Got away safely")
        break
    if player_input == "cry":
        print("Your bloodline is weak and will end with you.")
    if player_input == "Attack":
        move_selection = input("Choose an attack: hyperbeam, dragon breath, protect, or meteor. ")
        if move_selection == "hyperbeam":
            enemy_health = enemy_health-40
            print("You've fucked him up! He's lost 40 hp. ")
            input()
        elif move_selection == "dragon breath":
            enemy_health = enemy_health-75
            print("That was super effective! Dragons are too OP. He's lost 75 hp. ")
            input()
        elif move_selection == "protect":
            player_health = player_health+25
            print("You've gained 25 armor")
            input()
        elif move_selection == "meteor":
            enemy_health = enemy_health-20
            print("That wasn't very effective... your enemy can tank meteors bruh. he's only lost 20 hp. ")
            input()
        else:
            print("That isn't a move you know, get fuked nerd lmao")
            input()
    if enemy_health <= 0 or player_health <= 0:
        break
    enemy_move = print("Enemy turn, they use "+random.choice(enemy_turn))
    if enemy_move == "fire breath":
        player_health = player_health-30
        print("Enemy used Fire Breath! You take 30 damage")
    elif enemy_move == "ice beam":
            player_health = player_health-50
            print("Enemy used ice beam! You take 50 damage")
    elif enemy_move == "thunderbolt":
            player_health = player_health-75
            print("Enemy used Thunder Bolt! You take 75 damage")
    elif enemy_move == "leaf blade":
            player_health = player_health-15
            print("Enemy used leaf blade! You take 15 damage")
    else:
            continue
