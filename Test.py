import time
import random

# Starting variables
coins = 5
rizz = 0
sanity = 5
kills = 0
mercy = 0
cowardice = 0
playerLevel = 1
playerXP = 5
mcgeeLiked = False
mcgeeHealth = 3
userHealth = 5
mcGeeDead = False
bullets = 10

def tutorial():
  print("Attack: Attacks the enemy using melee or gun. This also allows the enemy to attack.")
  print("Run: Runs away. While you can't get any rewards, you also won't be in any danger.")
  print("3rd option: The third option isnt confined to anything, and is a scenario-specific option, but it won't involve combat.")
  print("List: This lists your stats.")
  print("Help: This displays all this text!")

def show_stats():
    print("Coins = " + str(coins))
    print("Sanity = " + str(sanity))
    print("Rizz = " + str(rizz))

print("The year is 2054. In 2024, a zombie apocalypse ravaged the world, decimating 95% of the human population.")
time.sleep(1.5)
print("The remaining human tribes in the USA have consolidated, forming the Dispersed States of America.")
time.sleep(1.5)
print("Your job, as a courier, is to deliver a package containing vital intel and supplies from the New York base to the California base.")
time.sleep(1.5)
print(" ")

print("Start Game?")
startGameChoice = input("Yes/No: ")
if startGameChoice.lower() == 'yes':
    print("Starting game!")
    gamestart = True
    time.sleep(0.5)
else:
    print("Ending game. Hey, what's that outside your window...?")
    exit()

time.sleep(0.5)
print("Do you have a promo code?")
promoCodeChoice = input("Promo Code: ")
if promoCodeChoice == '120%':
    print("Promo Code Redeemed!")
    time.sleep(0.5)
    print("Player level raised to 120!")
    playerLevel = playerLevel + 119
elif promoCodeChoice == 'Lucky888':
    print("You rolled the legendary hero Lucky!")
    time.sleep(0.5)
    print("Satisfied, you never embark on the journey.")
    exit()
elif promoCodeChoice == 'Jogoat':
    time.sleep(0.5)
    print("As you bow in front of your statue of Jogo, you get stronger.")
    time.sleep(0.5)
    print("Player level raised to 999!")
    time.sleep(0.5)
elif promoCodeChoice == "Hakari":
    hakariPromoChoice = random.randint(1, 239)
    if hakariPromoChoice > 237:
        print("You hit the jackpot!")
        time.sleep(0.5)
        print("You gain flight powers and fly across the DSA in just 4 minutes and 11 seconds.")
        time.sleep(0.5)
        print("Ending: stallkari")
        exit()
    else:
        time.sleep(0.5)
        print("You don't hit the jackpot.")
        time.sleep(0.5)
        print("Aw dangit")
else:
    print("Have fun!")

print("As you walk along the deserted roads of NYC, a figure lurches out of an alley.")
time.sleep(0.5)
print("Zombie McGee: 'Brains...'")
time.sleep(0.5)

while True:
    print("Choices: Attack(1) Run(2) Give Brain(3) List(4) Help(5)")
    mcgeeChoice = input("Choice: ")
    
    if mcgeeChoice == '5':
      tutorial()
    
    if mcgeeChoice == "1":
        print("Melee (1) or Gun? (2)")
        time.sleep(0.5)
        mcgeeWeaponChoice = input("Choice: ")
        time.sleep(0.5)

        if mcgeeWeaponChoice == '1':
            print("You chose to attack with melee.")
            time.sleep(0.5)
            while mcgeeHealth > 0 and userHealth > 0:
                print("Attack (1) Run (2) List(3)")
                mcgeeMelee = input("Choice: ")
                if mcgeeMelee == '1':
                    mcgeeAttackNum = random.randint(1, 5)
                    if mcgeeAttackNum > 4:
                        print("You land a black flash! 3 damage!")
                        mcgeeHealth -= 3
                    else:
                        print("1 damage!")
                        time.sleep(0.4)
                        mcgeeHealth -= 1

                    if mcgeeHealth > 0:
                        mcgeeCounterAttackNum = random.randint(1, 5)
                        if mcgeeCounterAttackNum > 4:
                            print("Zombie McGee lands a critical hit! 3 Damage!")
                            userHealth -= 3
                        else:
                            print("Zombie McGee deals 1 damage!")
                            time.sleep(0.5)
                            userHealth -= 1
                        print("Remaining health: " + str(userHealth))

                        if userHealth <= 0:
                            print("You were eaten by Zombie McGee.")
                            time.sleep(0.5)
                            print("Game over.")
                            exit()
                elif mcgeeMelee == '2':
                    print("You run away.")
                    cowardice += 1
                    break
                elif mcgeeMelee == '3':
                    show_stats()
                else:
                    print("Invalid choice. Please select again.")
            if mcgeeHealth <= 0:
                kills += 1
                playerXP += 5
                print("Kills: " + str(kills))
                print("XP: " + str(playerXP))
                mcGeeDead = True
                time.sleep(0.6)
                print("You killed Zombie McGee!")
                time.sleep(0.6)
                print("+5 XP")
                playerXP = playerXP + 5
                playerLevel = playerLevel + 1
                time.sleep(0.6)
                print("You leveled up!")
                time.sleep(0.6)
                print("New base stats:")
                userHealth = userHealth + 3
                time.sleep(0.6)
                print("Health = " + str(userHealth))
                time.sleep(0.6)
                print("Would you like to continue on, or loot the body?")
                mcgeeLoot = input("Loot(1) Continue(2): ")
                if mcgeeLoot == '1':
                    time.sleep(0.6)
                    print("You loot the body.")
                    time.sleep(0.6)
                    mcgeeLootRandom = random.randint(1, 5)
                    if mcgeeLootRandom > 4:
                        print("You found 5 bullets!")
                        bullets = bullets + 5
                    else:
                        print("You don't find anything usable.")
                else:
                    print("You continue on your way.")
            break

        elif mcgeeWeaponChoice == '2':
            print("You chose to attack with a gun.")
            time.sleep(0.5)
            while mcgeeHealth > 0 and userHealth > 0 and bullets > 0:
                print("Shoot (1) Run (2) List(3)")
                time.sleep(0.6)
                mcgeeGun = input("Choice: ")
                time.sleep(0.6)
                if mcgeeGun == '1':
                    shootMcgee = random.randint(1, 6)
                    if shootMcgee > 5:
                        print("Your aim is steady. 3 damage.")
                        time.sleep(0.6)
                        mcgeeHealth -= 3
                    elif shootMcgee == 4:
                        print("You missed!")
                    else:
                        print("Your aim is a little off. 1 damage.")
                        time.sleep(0.6)
                        mcgeeHealth -= 1
                    bullets -= 1
                    print("Bullets remaining: " + str(bullets))
                    print("McGee's health = " + str(mcgeeHealth))
                    time.sleep(0.6)

                    if mcgeeHealth > 0:
                        bulletMcgeeAttack = random.randint(1, 6)
                        if bulletMcgeeAttack > 5:
                            print("Zombie McGee lands a critical hit! 3 damage.")
                            time.sleep(0.6)
                            userHealth -= 3
                        else:
                            print("Zombie McGee attacks! 1 damage.")
                            time.sleep(0.6)
                            userHealth -= 1
                        print("Remaining health: " + str(userHealth))
                        time.sleep(0.6)

                        if userHealth <= 0:
                            print("You were eaten by Zombie McGee.")
                            time.sleep(0.6)
                            print("Game over.")
                            exit()
                    if bullets <= 0:
                        print("Out of bullets! Switching to melee.")
                        mcgeeWeaponChoice = '1'
                elif mcgeeGun == '2':
                    print("You run away.")
                    cowardice += 1
                    break
                elif mcgeeGun == '3':
                    show_stats()
                else:
                    print("Invalid choice. Please select again.")
            if mcgeeHealth <= 0:
                kills += 1
                playerXP += 5
                print("Kills: " + str(kills))
                print("XP: " + str(playerXP))
                mcGeeDead = True
                time.sleep(0.6)
                print("You killed Zombie McGee!")
                time.sleep(0.6)
                print("+5 XP")
                playerXP = playerXP + 5
                playerLevel = playerLevel + 1
                time.sleep(0.6)
                print("You leveled up!")
                time.sleep(0.6)
                print("New base stats:")
                userHealth = userHealth + 3
                time.sleep(0.6)
                print("Health = " + str(userHealth))
                time.sleep(0.6)
                print("Would you like to continue on, or loot the body?")
                mcgeeLoot = input("Loot(1) Continue(2): ")
                if mcgeeLoot == '1':
                    time.sleep(0.6)
                    print("You loot the body.")
                    time.sleep(0.6)
                    mcgeeLootRandom = random.randint(1, 5)
                    if mcgeeLootRandom > 4:
                        print("You found 5 bullets!")
                        bullets = bullets + 5
                    else:
                        print("You don't find anything usable.")
                else:
                    print("You continue on your way.")
            break

        else:
            print("Invalid choice. Ending game.")
            exit()

    elif mcgeeChoice == '2':
        print("You chose to run.")
        print("As you are faster, you easily escape.")
        mcgeeAlive = True
        break

    elif mcgeeChoice == '3':
        print("You chose to give your brain away to Zombie McGee!")
        time.sleep(0.6)
        print("You give your brain away.")
        time.sleep(0.6)
        userHealth = userHealth - 999
        print("Ending: Generosity")
        exit()

    elif mcgeeChoice == '4':
        show_stats()

    else:
        print("Invalid choice. Please select again.")

time.sleep(0.6)
print("After your encounter with Zombie McGee, you continue onward to your final destination.")
time.sleep(0.7)
print("Until...")
time.sleep(0.7)
print("End of part 1.")
print("Start part two?")
print("Y/N")
partTwoChoice = input("Choice: ")
if partTwoChoice.lower() == "y":
    partTwoStart = True
else:
    print("Ending game. Thanks for playing!")
    exit()

time.sleep(0.6)
print("Continuing on, you walk through the ruins of Aquinas College, which for plot purposes is in the USA.")
time.sleep(0.6)
print("You hear something behind you...")
time.sleep(0.6)
print("Zombie Mr. Deakin jumps at you!")
time.sleep(0.6)
deakinHealth = 6

while True:
    print("Choices: Attack(1) Run(2) Reason With(3) List(4) Help(5)")
    deakinChoice = input("Choice: ")
    
    if deakinChoice == '5':
      tutorial()
    
    if deakinChoice == "1":
        print("Melee (1) or Gun? (2)")
        time.sleep(0.5)
        deakinWeaponChoice = input("Choice: ")
        time.sleep(0.5)

        if deakinWeaponChoice == '1':
            print("You chose to attack with melee.")
            time.sleep(0.5)
            while deakinHealth > 0 and userHealth > 0:
                print("Attack (1) Run (2) List(3)")
                deakinMelee = input("Choice: ")
                if deakinMelee == '1':
                    deakinAttackNum = random.randint(1, 5)
                    if deakinAttackNum > 4:
                        print("As you raise your fist, you enter 'The Zone'.")
                        time.sleep(0.4)
                        print("Black Flash! 3 damage!")
                        deakinHealth -= 3
                    else:
                        print("As you go to punch him, his rippling muscles deflect the attack!")
                        time.sleep(0.4)

                    if deakinHealth > 0:
                        deakinCounterAttackNum = random.randint(1, 5)
                        if deakinCounterAttackNum > 4:
                            print("Zombie Mr. Deakin lands a critical hit! 3 Damage!")
                            userHealth -= 3
                        else:
                            print("Zombie Mr. Deakin deals 1 damage!")
                            time.sleep(0.5)
                            userHealth -= 1
                        print("Remaining health: " + str(userHealth))

                        if userHealth <= 0:
                            print("You were defeated by Zombie Mr. Deakin.")
                            time.sleep(0.5)
                            print("Zombie Mr Deakin: 'You never stood a chance.'")
                            time.sleep(0.5)
                            print("Game over.")
                            exit()
                elif deakinMelee == '2':
                    print("You run away.")
                    cowardice += 1
                    break
                elif deakinMelee == '3':
                    show_stats()
                else:
                    print("Invalid choice. Please select again.")
            if deakinHealth <= 0:
                kills += 1
                playerXP += 5
                print("Kills: " + str(kills))
                print("XP: " + str(playerXP))
                time.sleep(0.6)
                print("You defeated Zombie Mr. Deakin!")
                time.sleep(0.6)
                print("+5 XP")
                playerXP = playerXP + 5
                playerLevel = playerLevel + 1
                time.sleep(0.6)
                print("You leveled up!")
                time.sleep(0.6)
                print("New base stats:")
                userHealth = userHealth + 3
                time.sleep(0.6)
                print("Health = " + str(userHealth))
                time.sleep(0.6)
                print("Would you like to continue on, or loot the body?")
                deakinLoot = input("Loot(1) Continue(2): ")
                if deakinLoot == '1':
                    time.sleep(0.6)
                    print("You loot the body.")
                    time.sleep(0.6)
                    deakinLootRandom = random.randint(1, 900)
                    if deakinLootRandom > 899:
                        print("You found 293472394293475 bullets!")
                        time.sleep(0.6)
                        print("You find medical supplies!")
                        userHealth = userHealth + 203842703497209
                        time.sleep(0.6)
                        print("Health: 130942034920394")
                        bullets = bullets + 5
                    else:
                        print("You don't find anything usable.")
                else:
                    print("You continue on your way.")
            break

        elif deakinWeaponChoice == '2':
            print("You chose to attack with a gun.")
            time.sleep(0.5)
            while deakinHealth > 0 and userHealth > 0 and bullets > 0:
                print("Shoot (1) Run (2) List(3)")
                time.sleep(0.6)
                deakinGun = input("Choice: ")
                time.sleep(0.6)
                if deakinGun == '1':
                    shootDeakin = random.randint(1, 6)
                    if shootDeakin > 5:
                        print("Your aim is steady. 3 damage.")
                        time.sleep(0.6)
                        deakinHealth -= 3
                    elif shootDeakin == 4:
                        print("His radiant aura blinds you, and causes you to miss!")
                    else:
                        print("The bullet simply p-ting's off of his chest!.")
                        time.sleep(0.6)
                    bullets -= 1
                    print("Bullets remaining: " + str(bullets))
                    print("Mr. Deakin's health = " + str(deakinHealth))
                    time.sleep(0.6)

                    if deakinHealth > 0:
                        bulletDeakinAttack = random.randint(1, 6)
                        if bulletDeakinAttack > 5:
                            print("Zombie Mr. Deakin lands a critical hit! 3 damage.")
                            time.sleep(0.6)
                            userHealth -= 3
                        else:
                            print("Zombie Mr. Deakin attacks! 1 damage.")
                            time.sleep(0.6)
                            userHealth -= 1
                        print("Remaining health: " + str(userHealth))
                        time.sleep(0.6)

                        if userHealth <= 0:
                            print("You were defeated by Zombie Mr. Deakin.")
                            time.sleep(0.6)
                            print("Game over.")
                            exit()
                    if bullets <= 0:
                        print("Out of bullets! Switching to melee.")
                        deakinWeaponChoice = '1'
                elif deakinGun == '2':
                    print("You run away.")
                    cowardice += 1
                    break
                elif deakinGun == '3':
                    show_stats()
                else:
                    print("Invalid choice. Please select again.")
            if deakinHealth <= 0:
                kills += 1
                playerXP += 5
                print("Kills: " + str(kills))
                print("XP: " + str(playerXP))
                time.sleep(0.6)
                print("You defeated Zombie Mr. Deakin!")
                time.sleep(0.6)
                print("+5 XP")
                playerXP = playerXP + 5
                playerLevel = playerLevel + 1
                time.sleep(0.6)
                print("You leveled up!")
                time.sleep(0.6)
                print("New base stats:")
                userHealth = userHealth + 3
                time.sleep(0.6)
                print("Health = " + str(userHealth))
                time.sleep(0.6)
                deakinDead = True
                print("Would you like to continue on, or loot the body?")
                deakinLoot = input("Loot(1) Continue(2): ")
                if deakinLoot == '1':
                    time.sleep(0.6)
                    print("You loot the body.")
                    time.sleep(0.6)
                    deakinLootRandom = random.randint(1, 5)
                    if deakinLootRandom > 4:
                        print("You found 1248927394729348279348723947293843427943894398439843988903494380943098430984309843098439848094389438943893489438934983498043983493498 bullets!")
                        bullets = bullets + 5
                    else:
                        print("You don't find anything usable.")
                else:
                    print("You continue on your way.")
            break

        else:
            print("Invalid choice. Ending game.")
            exit()

    elif deakinChoice == '2':
        print("You chose to run.")
        time.sleep(0.6)
        print("As you try and run, Zombie Deakin catches you!.")
        time.sleep(0.6)
        print("Game over!")
        break

    elif deakinChoice == '3':
        print("You chose to reason with Zombie Mr. Deakin!")
        time.sleep(0.6)
        reasonOutcome = random.randint(1, 100)
        if reasonOutcome < 99:
            print("Being a perfect person even post-zombification, Zombie Mr Deakin allows you through.")
            break
        else:
            print("Zombie Mr. Deakin is not persuaded and attacks!")
            deakinHealth = 6
            continue

    elif deakinChoice == '4':
        show_stats()

    else:
        print("Invalid choice. Please select again.")

print("After your encounter with Zombie Mr. Deakin, you continue onward to your final destination.")
time.sleep(0.7)
print("End of part two.")
time.sleep(0.6)
print("Start part 3?")
time.sleep(0.5)
print("Y/N")
time.sleep(0.6)
part2Choice = input("Choice:")
if part2Choice == 'Y':
  part2Starting = True
else:
  time.sleep(0.6)
  print("Ending game. Thanks for playing!")
  exit()
  
print("You check your map, and realize that you're almost there!")
time.sleep(0.6)
print("You look up, and realize that you've come to a crossroads.")
time.sleep(0.6)
print("Will you go left(1), or right(2)?")
time.sleep(0.6)
crossroadChoice = input("Choice:")
if crossroadChoice == '1':
  crossroadLeft = True
  time.sleep(0.6)
  print("You go left.")
elif crossroadChoice == '2':
  crossroadRight = True 
  time.sleep(0.6)
  print("You go right.")
else:
  time.sleep(0.6)
  print("As you stand there, indecisive, a zombie horde comes and eats you.")
  time.sleep(0.6)
  print("Ending: Procrastination")
  exit()
if crossroadLeft = True:
  print("Walking down the left path, you spot Zombie Big J!")
  time.sleep(0.6)
  print("What will you do?")
  time.sleep(0.6)
  print("Attack(1) Run(2) Attempt to sneak past(3) List(4) Help(5)")
  bigJChoice = input("Choice:")
  if bigJChoice == '1':
    time.sleep(0.6)
    print("Melee(1) or Gun(2)?")
    bigJWeapon = input("Choice:")
    if bigJWeapon == '1':
      print("You chose to attack with melee.")
      time.sleep(0.6)
      
