# game/enemy.py

from numpy import random
class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_player(self, player):
        damage = random.randint(1, self.attack)
        player.take_damage(damage)
        print(f"{self.name} 对 {player.name} 造成了 {damage} 点伤害！")