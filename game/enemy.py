# game/enemy.py
import random

class Enemy:
    def __init__(self, name, hp, attack_power, defense=0, exp_reward=0):  # 这里也改为 attack_power
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power  # 改名
        self.defense = defense
        self.exp_reward = exp_reward

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage

    def attack_target(self, target):  # 改名为 attack_target
        damage = random.randint(1, self.attack_power)
        actual_damage = target.take_damage(damage)
        print(f"{self.name} 对 {target.name} 造成了 {actual_damage} 点伤害！")