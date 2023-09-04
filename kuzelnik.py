class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Wizard:
    def __init__(self, name, health, strength, mana):
        self.equip = None
        self.name = name
        self.health = health
        self.strength = strength
        self.mana = mana
        self.weapon = None


    def choose_weapon(self, weapon):
        self.weapon = weapon

    def move(self):
        print(f"{self.name} move.")

    def run(self):
        print(f"{self.name} starts running and stops when he sees an enemy.")

    def take_damage(self, damage):
        self.health -= damage
        self.health -= self.weapon.damage
        print(f"{self.name} suffered damage {damage} from his life.He has {self.health} lives left.")

    def attack(self, enemy, damage=0):
        if self.weapon:
            enemy.health_before_attack = enemy.health
            damage_dealt = self.strength + self.weapon.damage + damage
            print(f"{self.name} attacks the {enemy.name} with strength {damage_dealt}.He has {self.health} lives left.")
            enemy.take_damage(damage_dealt)
            damage_after_attack = enemy.health_before_attack - damage_dealt
            print(f"{enemy.name} suffered damage {damage_after_attack} points")
        else:
            print(f"{self.name} he has no weapons.")


class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} utrpel poškodenie {damage} bodov. He has {self.health} lives left")

    def attack(self, wizard):
        self.wizard = wizard
        damage_dealt = self.strength
        print(f"{self.name} utoci na {wizard.name} za {damage_dealt} points.")
        wizard.take_damage(damage_dealt)


bow = Weapon("bow", 5)
magic_wand = Weapon("magic wand", 8)
sword = Weapon("sword", 10)

merlin = Wizard(name="Merlin", health=100, strength=13, mana=50)
gandalf = Wizard(name="Gandalf", health=150, strength=10, mana=100)
geralt = Wizard(name="Geralt", health=125, strength=15, mana=85)

dragon = Enemy(name="Dragon", health=60, strength=10)
ghoul = Enemy(name="Ghoul", health = 55, strength=12)



merlin.choose_weapon(bow)
# gandalf.choose_weapon(sword)
# geralt.choose_weapon(magic_wand)

# merlin.move()
# # gandalf.move()
# # geralt.move()
#
# merlin.run()
# gandalf.run()
# geralt.run()

# merlin.take_damage(6)

merlin.attack(dragon)
# gandalf.attack()
#
# damage_dealt = 5
# dragon.take_damage(damage_dealt)
#
# merlin.attack(dragon, damage_dealt)






