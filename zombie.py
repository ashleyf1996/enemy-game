from enemy import *
import random

class Zombie(Enemy):
    
    def __init__(self,  health_ponts, attack_damage):
     super().__init__(type_of_enemy='Zombie', health_ponts=health_ponts, attack_damage=attack_damage)
      
    def talk(self):
       print("Grumbling")

    def spead_disease(self):
       print("Zombie is spreading disease")


    def special_attack(self):
        did_special_attack_work = random.random () < 0.50
        if did_special_attack_work:
           self.health_points += 2
           print("Zombie regenerated 2HP!")