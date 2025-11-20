class Enemy:

    def __init__(self, type_of_enemy, health_ponts, attack_damage):
      #instatiate new object with these values
      #this new object wi
      self.__type_of_enemy = type_of_enemy
      self.health_points = health_ponts
      self.attack_damage = attack_damage
      

    def talk(self):
        print(f'I am a {self.__type_of_enemy} be prepared to fight!!')

    def walk_forward(self):
     print(f'{self.__type_of_enemy} moves closer to you')

    def attack(self):
        print(f'{self.__type_of_enemy} attacks for {self.attack_damage} damage')

    def special_attack(self):
       print("Enemy has no special attack")

    def get_type_of_enemy(self):
       return self.__type_of_enemy
    x
