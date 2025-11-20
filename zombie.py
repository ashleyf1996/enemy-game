from enemy import *

class Zombie(Enemy):
    
    def __init__(self,  health_ponts, attack_damage):
     super().__init__(type_of_enemy='Zombie', health_ponts=health_ponts, attack_damage=attack_damage)
      
    def talk(self):
       print("Grumbling")

    def spead_disease(self):
       print("Zombie is spreading disease")

