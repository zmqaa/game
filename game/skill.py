# game/skill.py

class Skill:
    def __init__(self, name, mp_cost, description, damage_multiplier):
        self.name = name
        self.mp_cost = mp_cost
        self.description = description
        self.damage_multiplier = damage_multiplier  # 伤害倍率