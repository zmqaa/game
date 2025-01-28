# game/data/enemies.py
from game.enemy import Enemy

ENEMY_DATA = {
    "哥布林": {
        "hp": 50,
        "attack_power": 5,
        "defense": 1,
        "exp_reward": 20
    },
    "狼": {
        "hp": 70,
        "attack_power": 8,
        "defense": 2,
        "exp_reward": 30
    },
    "巨魔": {
        "hp": 100,
        "attack_power": 12,
        "defense": 4,
        "exp_reward": 50
    }
}

def create_enemy(name):
    """根据名称创建敌人实例"""
    if name in ENEMY_DATA:
        data = ENEMY_DATA[name]
        return Enemy(
            name=name,
            hp=data["hp"],
            attack_power=data["attack_power"],
            defense=data["defense"],
            exp_reward=data["exp_reward"]
        )
    raise ValueError(f"未知的敌人类型：{name}")