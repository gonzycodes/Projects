from player import Player
from spells import flame, risky_flame, heal
from combat import apply_spell
import random

player = Player("Nahuel", 100)
computer = Player("Cpu", 100)

while player.is_alive() and computer.is_alive():

    print(f"\nYour HP: {player.health} | Computer HP: {computer.health}\n")


    print("Choose your move:")
    print(f"1. {flame.name} (Damage)")
    print(f"2. {risky_flame.name} (Damage)")
    print(f"3. {heal.name} (Heal)")

    try:
        choice = int(input("Enter move number: "))
        if choice == 1:
            spell = flame
        elif choice == 2:
            spell = risky_flame
        elif choice == 3:
            spell = heal
        else:
            print("Invalid choice, try again.")
            continue
    except ValueError:
        print("Invalid input, try again.")
        continue

    print(apply_spell(player, computer, spell))


    if not computer.is_alive():
        print("Computer has been defeated! HP reached 0.")
        break


    if computer.health <= 35 and random.random() < 0.7:
        computer_spell = heal
    else:
        computer_spell = random.choice([flame, risky_flame])

    print(apply_spell(computer, player, computer_spell))

    if not player.is_alive():
        print("You have been defeated! HP reached 0.")
        break
