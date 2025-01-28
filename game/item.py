# game/item.py
import random

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

class Weapon(Item):
    def __init__(self, name, attack_bonus):
        super().__init__(name, "weapon")
        self.attack_bonus = attack_bonus

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