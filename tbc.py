#Angel Blocker
#TBC Project CompSci 120
#10/13/2025
#My Very Own TBC
import random

class Character(object):
    """
    takes in object
    creates Charcter class
    defines properties
    checks integers
    prints stats
    """    
    
    def __init__(self, name = "Hero", hitPoints = 10, hitChance = 50, maxDamage = 5, armor =2):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        value = Character.testInt(self, value, min = -6, max = 100, default = 10)
        if value <= -6:
            value = 10
            self.__hitPoints = value
        else:
            self.__hitPoints = value
    
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        value = Character.testInt(self, value, min = 0, max = 100, default = 0)
        if value == 0:
            value = 50
            self.__hitChance = value
        else:
            self.__hitChance = value
        
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        value = Character.testInt(self, value, min = 0, max = 100, default = 0)
        if value == 0:
            value = 5
            self.__maxDamage = value
        else:
            self.__maxDamage = value
        
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        value = Character.testInt(self, value, min = 0, max = 100, default = 0)
        if value == 0:
            value = 0
            self.__armor = value
        else:
            self.__armor = value
    
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """

        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
    
    def printStats(Character):
        """
        prints the stats for character
        """
        print(f"{Character.name}")
        print(f"Hit Points: {Character.hitPoints}")
        print(f"Hit Chance: {Character.hitChance}")
        print(f"Max Damage: {Character.maxDamage}")
        print(f"Armor: {Character.armor}")
        print("   ")
    
    def heroHit(hero, monster):
        """
        hit function for hero hitting
        """
        hitInt = random.randrange(0, 100)
        if hitInt < hero.hitChance:
            print("Hero hits Monster...")
            damageDone = random.randrange(1, hero.maxDamage)
            if monster.armor > 0:
                damageDone = 0
                monster.armor = int(monster.armor)
                monster.armor = monster.armor - 1
                print("Monster's armor absorbed the hit this time!")
                print(f"Monster has {monster.armor} armor left")
            else:
                monster.hitPoints = int(monster.hitPoints)
                monster.hitPoints = monster.hitPoints - damageDone
                print("Monster has no armor left")
                print(f"Monster loses {damageDone} points")
        else:
            print("Hero missed Monster this time")
        print("   ")
        return monster, hero
    
    def monsterHit(monster, hero):
        """
        hit function for monster hitting
        """
        hitInt = random.randrange(0, 100)
        if hitInt < monster.hitChance:
            print("Monster hits Hero...")
            damageDone = random.randrange(1, monster.maxDamage)
            if hero.armor > 0:
                damageDone = 0
                hero.armor = int(hero.armor)
                hero.armor = hero.armor - 1
                print("Hero's armor absorbed the hit this time!")
                print(f"Hero has {hero.armor} armor left")
            else:
                hero.hitPoints = int(hero.hitPoints)
                hero.hitPoints = hero.hitPoints - damageDone
                print("Hero has no armor left")
                print(f"Hero loses {damageDone} points")
        else:
            print("Monster missed Hero this time")
        print("   ")
        return hero, monster
    
    def fight(monster, hero):
        """
        calls the hit functions
        runs the fighting until someone wins
        """
        keepGoing = True
        while keepGoing:
            Character.heroHit(hero, monster)
            if monster.hitPoints <= 0:
                keepGoing = False
                print("Hero wins!")
            else:
                Character.monsterHit(monster, hero)
            if hero.hitPoints <= 0:
                keepGoing = False
                print("Monster wins!")
            if keepGoing == True:
                print(f"Hero: {hero.hitPoints} HP")
                print(f"Monster: {monster.hitPoints} HP")
            else:
                keepGoing = False
            print("   ")
            if keepGoing == True:
                answer = input("Press for another round: ")
                if answer == "":
                    keepGoing = True
                else:
                    keepGoing = True
                    if hero.hitPoints <= 0:
                        keepGoing = False
                        print("Monster wins!")
                    if monster.hitPoints <= 0:
                        keepGoing = False
                        print("Hero wins!")
                    else:
                        keepGoing = True
            else:
                keepGoing = False
        #return monster, hero
    
def main():
    hero = Character()
    hero.name = "Hero"
    hero.hitPoints = 10
    hero.hitChance = 50
    hero.maxDamage = 5
    hero.armor = 2
    monster = Character("Monster", 20, 30, 5, 0)
    hero.printStats()
    monster.printStats()
    
    Character.fight(monster, hero)
    
if __name__ == "__main__":
    main()