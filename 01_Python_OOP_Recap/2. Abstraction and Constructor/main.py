from enemy import Enemy

# A helper function to keep the terminal output clean and sectioned
def print_separator() -> None:
    print("\n" + "-" * 40 + "\n")

# Calling the constructor
enemy1 = Enemy('Goblin', 10, 1)
enemy2 = Enemy('Zombie', 15, 2)
enemy3 = Enemy('Ogre', 25, 5)

enemies = [enemy1, enemy2 ,enemy3]

# ---> WHAT IS ABSTRACTION? <--- walk() and talk() functions.
# We don't care how the enemy walks or talks internally. 
# We just call the simple methods and the class handles the complex logic behind the scenes.

for enemy in enemies:
    print_separator()

    enemy.walk()

    print_separator()

    enemy.talk()

    print_separator()

    print("ENEMY STATS SCANNED:")
    print(enemy)
