from enemy import *
from zombie import *
from ogre import *

zombie = Zombie(10,1)
ogre = Ogre(20,3)

print(zombie.get_type_of_enemy())
zombie.talk()
zombie.spead_disease()
print(ogre.get_type_of_enemy())

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do an attack of {zombie.attack_damage} damage')
print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do an attack of {ogre.attack_damage} damage')