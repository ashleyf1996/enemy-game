from enemy import *
from zombie import *
from ogre import *

def battle(e: Enemy):
    e.talk()
    e.attack()


zombie = Zombie(10,1)
ogre = Ogre(20,3)

battle(zombie)
battle(ogre)
