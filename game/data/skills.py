# game/data/skills.py

SKILLS = {
    "重击": {
        "mp_cost": 15,
        "damage_multiplier": 1.5,
        "description": "造成150%的攻击伤害",
        "level_requirement": 1
    },
    "连击": {
        "mp_cost": 25,
        "damage_multiplier": 0.8,
        "hits": 3,
        "description": "进行三次攻击，每次造成80%的攻击伤害",
        "level_requirement": 3
    }
}