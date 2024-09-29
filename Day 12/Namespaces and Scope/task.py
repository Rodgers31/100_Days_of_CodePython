enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope

def drink_portion():
    portion_strenght = 2
    print(portion_strenght)
drink_portion()

#Global scope
player_health = 10