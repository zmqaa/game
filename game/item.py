# game/item.py
import random

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

# game/item.py

class Weapon:
    def __init__(self, name, attack_bonus, status_effect=None):
        self.name = name
        self.attack_bonus = attack_bonus
        self.effect = "weapon"
        self.status_effect = status_effect  # 新增：武器可能带有的状态效果

    def apply_effect(self, target):
        """应用武器的状态效果"""
        if self.status_effect:
            target.apply_status_effect(self.status_effect())

from game.status_effects import PoisonEffect, BurningEffect

# 添加带特殊效果的武器
SPECIAL_WEAPONS = [
    Weapon("毒匕首", attack_bonus=3, status_effect=lambda: PoisonEffect(duration=3)),
    Weapon("火焰剑", attack_bonus=5, status_effect=lambda: BurningEffect(duration=2))
]

class Potion(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, "potion")
        self.heal_amount = heal_amount

# 添加物品池
WEAPONS = [
    Weapon("铁剑", 5),
    Weapon("青铜剑", 8),
    Weapon("精钢剑", 12)
]

POTIONS = [
    Potion("小型治疗药水", 20),
    Potion("中型治疗药水", 40),
    Potion("大型治疗药水", 60)
]

def random_item():
    """随机生成一个物品"""
    # 50%概率获得武器，50%概率获得药水
    if random.random() < 0.5:
        return random.choice(WEAPONS)
    else:
        return random.choice(POTIONS)