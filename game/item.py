# game/item.py

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