from enemy import *

class Ogre(Enemy):
    def __init__(self,  health_ponts, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_ponts=health_ponts, attack_damage=attack_damage)
      
    def talk(self):
        print("Ogre is slamming hands")
