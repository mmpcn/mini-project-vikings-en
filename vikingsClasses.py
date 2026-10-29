import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage=1):
        super().receiveDamage(damage)
        if self.health <= 0:
            return ( f"{self.name} has died in act of combat")
        else: 
            return (f"{self.name} has received {damage} points of damage")
                
  

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage=1):
        super().receiveDamage(damage)
        if self.health <= 0:
            return ( "A Saxon has died in combat")
        else: 
            return (f"A Saxon has received {damage} points of damage")
                                 

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy=[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
     self.saxonArmy.append(saxon)
      
    
    def vikingAttack(self):
        if len(self.saxonArmy)==0 or len (self.vikingArmy)==0:
            return
        outcome = self.saxonArmy[0].receiveDamage(self.vikingArmy[0].strength)
        if ("died" in outcome.split()):
          self.saxonArmy.remove(self.saxonArmy[0])
        return outcome
    
    def saxonAttack(self):
        if len(self.saxonArmy)==0 or len (self.vikingArmy)==0:
            return
        outcome =  self.vikingArmy[0].receiveDamage(self.saxonArmy[0].strength)
        if ("died" in outcome.split()):
           self.vikingArmy.remove(self.vikingArmy[0])
        return outcome

    def showStatus(self):
        #vikingHealth = sum([vik.health for vik in self.vikingArmy])
        #saxonHealth = sum([sax.health for sax in self.saxonArmy])
        #if vikingHealth > 0 and saxonHealth>0:
        #    return 'Vikings and Saxons are still in the thick of battle.'
        #elif vikingHealth <=0:
        #    return 'Saxons have fought for their lives and survive another day...'
        #else:
            #return 'Vikings have won the war of the century!'
        if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
            return 'Vikings and Saxons are still in the thick of battle.'
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) == 0:
            return  'Vikings have won the war of the century!'     