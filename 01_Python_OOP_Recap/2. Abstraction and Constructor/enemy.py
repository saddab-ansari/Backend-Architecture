class Enemy:

    # ---> THIS IS THE CONSTRUCTOR <---
    # It initializes the object and sets up its base stats when it is created.
    def __init__(self, type_of_enemy, health_point, attack_damage) -> None:
        self.type_of_enemy = type_of_enemy
        self.health_point = health_point
        self.attack_damage = attack_damage
    def __str__(self):
        return (f"Enemy Type: {self.type_of_enemy}\n" 
                f"Health:     {self.health_point} HP\n" 
                f"Damage:     {self.attack_damage} ATK")

    def talk(self) -> None:
        print(f"[{self.type_of_enemy}] groans: 'I am a {self.type_of_enemy}...'")

    def walk(self) -> None:
        print(f"--> {self.type_of_enemy} walked one step closer!")
