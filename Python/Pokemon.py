import random ##needed for randomizing the enemy attack
enemy = "A wild pokemon"
enemy_health = 100
enemy_turn = ["Fire breath","Ice beam","Thunderbolt","Leaf blade"]
enemy_move = random.choice(enemy_turn)
player_health = 100
player_move_1 = "hyperbeam"
player_move_2 = "dragon breath"
player_move_3 = "protect"
player_move_4 = "meteor"
while True:
    if enemy_health <= 0:
        print("Enemy defeated! Gained 30,000 souls!")
        break
    if player_health <= 0:
        print("Dude you suck, git gud nub. GAME OVER")
        break
    player_input = input("What do you do? Attack, Run, Cry, Check enemy health, Check my health, identify enemy: \n").lower()
    if player_input == "identify enemy".lower():
        print(enemy)
        continue
    if player_input == "Check enemy health".lower():
        print(enemy_health)
        continue
    elif player_input == "Check my health".lower():
        print(player_health)
        continue
    elif player_input == "Run".lower():
        print("Got away safely")
        break
    elif player_input == "Cry".lower():
        print("Your bloodline is weak and will end with you.")
        input()
    elif player_input == "Attack".lower():
        move_selection = input("Choose an attack: hyperbeam, dragon breath, protect, or meteor. \n").lower()
        if move_selection == "Hyperbeam".lower():
            enemy_health = enemy_health-40
            print("You've fucked him up! He's lost 40 hp. ")
            input()
        elif move_selection == "Dragon breath".lower():
            enemy_health = enemy_health-75
            print("That was super effective! Dragons are too OP. He's lost 75 hp. ")
            input()
        elif move_selection == "Protect".lower():
            player_health = player_health+25
            print("You've gained 25 armor")
            input()
        elif move_selection == "Meteor".lower():
            enemy_health = enemy_health-25
            print("That wasn't very effective... your enemy can tank meteors bruh. he's only lost 25 hp. ")
            input()
        else:
            print("That isn't a move you know, get fuked nerd lmao")
            input()
    if enemy_health <= 0:
        print("Enemy defeated! Gained 30,000 souls!")
        break
    enemy_move = random.choice(enemy_turn)
    if enemy_move == "Fire breath":
        player_health = player_health-30
        print("Enemy used Fire Breath! You take 30 damage")
        continue
    elif enemy_move == "Ice beam":
        player_health = player_health-50
        print("Enemy used Ice beam! You take 50 damage")
        continue
    elif enemy_move == "Thunderbolt":
        player_health = player_health-75
        print("Enemy used Thunder Bolt! You take 75 damage")
        continue
    elif enemy_move == "Leaf blade":
        player_health = player_health-15
        print("Enemy used Leaf blade! You take 15 damage")
        continue

