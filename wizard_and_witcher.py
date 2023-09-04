""" 
Lehci domaci ukol. Zkuste vytvorit tridu kouzelnik nebo amazonka. Pridejte jim zivoty, silu, manu. Zkuste vytvorit par zbrani - treba kouzelna hul, luk atd.
Kouzelna postavicka bude moct chodit a utocit. Do chozeni a utoku dejte jenom print ( Walking, shooting atd.) To co je dulezite, abyste se spravne odebrali zivoty, manu. Zkontrovali jste jestli jde utocit atd.
Zajima me jak se s tim poperete, aby bylo videt co vam moc nejde nebo naopak jde, at vime na co se zamerit 
"""

# Ja som si to zmenil na carodejnika a zaklinaca :)
# witcher - mec + zaklinadlo
# wizard - palica + zaklinadlo
# charaktery budu mat mena wizard a witcher
# zakladne parametre charakterov budu health, strength, mana
# charakter sa pohybuje - move/walk , utoci

import random

class Character:
    def __init__(self, name, healt, strength, stamina, mana):
        self.name = name
        self.health = healt
        self.strength = strength
        self.stamina = stamina
        self.mana = mana
        self.weapon = None
        self.spell = None
    
    # metoda na vypis postavy 
    def __str__(self):
        return f"{self.name} - Health: {self.health}, Strength: {self.strength}, Stamina: {self.stamina}, Mana: {self.mana}"
    
    def move(self):
        print(f"{self.name} moves...")
        
    def attack(self, target):
        choice = random.choice(["weapon", "spell"])
        
        if choice == "weapon" and self.stamina >= self.weapon.stamina_cost:
            self.stamina -= self.weapon.stamina_cost
            target.health -= self.weapon.damage
            print(f"{self.name} attacks {target.name} with {self.weapon.name} causing {self.weapon.damage} damage!")
        elif choice == "spell" and self.mana >= self.spell.mana_cost:
            self.mana -= self.spell.mana_cost
            target.health -= self.spell.damage
            print(f"{self.name} attacks {target.name} with {self.spell} causing {self.spell.damage} damage!")
        else:
            print(f"{self.name} doesn't have enough resouces to attack")
   
            
class Weapon:
    def __init__(self, name, damage, stamina_cost):
        self.name = name 
        self.damage = damage  
        self.stamina_cost = stamina_cost
    
    # metoda na vypis zbrane 
    def __str__(self):
        return f"{self.name} - Damage: {self.damage}, Stamina_cost: {self.stamina_cost}"

class Spell:
    def __init__(self, name, damage, mana_cost):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
    
    # metoda na vypis kuzla 
    def __str__(self):
        return f"{self.name} - Damage: {self.damage}, Mana_cost: {self.mana_cost}"
        

witcher = Character("Geralt", 1500, 50, 300, 300)
wizard = Character("Gandalf", 1750, 30, 300, 300)
    
sword = Weapon("Iron sword", 100, 100)
stick = Weapon("Witch's stick", 50, 50)

witcher_spell = Spell("Aard", 40, 50)
wizzard_spell = Spell("Cruciatus", 110, 100)

witcher.weapon = sword
witcher.spell = witcher_spell
wizard.weapon = stick
wizard.spell = wizzard_spell

print(witcher)
print(wizard)
print(sword)
print(stick)
print(witcher_spell)
print(wizzard_spell)


while witcher.health > 0 and wizard.health > 0:
    if witcher.stamina >= witcher.weapon.stamina_cost or witcher.mana >= witcher.spell.mana_cost:
        witcher.attack(wizard)
        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated!")
            break
    else:
        print(f"{witcher.name} doesn't have enough resources to continue!")
        break

    if wizard.stamina >= wizard.weapon.stamina_cost or wizard.mana >= wizard.spell.mana_cost:
        wizard.attack(witcher)
        if witcher.health <= 0:
            print(f"{witcher.name} has been defeated!")
            break
    else:
        print(f"{wizard.name} doesn't have enough resources to continue!")
        break

print("\nEnd of battle!")
print(witcher)
print(wizard)
