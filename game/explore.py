# game/explore.py

import random
from game.enemy import Enemy
from game.item import Weapon, Potion, SPECIAL_WEAPONS


def random_enemy():
    enemies = [
        Enemy("哥布林", 50, 5),
        Enemy("狼", 70, 8),
        Enemy("巨魔", 100, 12)
    ]
    return random.choice(enemies)

def random_item():
    # 添加特殊武器到可能的掉落物品中
    items = [
        Weapon("铁剑", 5),
        Potion("治疗药水", 20),
        SPECIAL_WEAPONS[0],  # 毒匕首
        SPECIAL_WEAPONS[1]   # 火焰剑
    ]
    chances = [0.4, 0.4, 0.1, 0.1]  # 设置各物品的掉落概率
    return random.choices(items, weights=chances)[0]

def explore(player):
    print("你正在探索...")
    event = random.randint(1, 4)
    if event == 1:
        print("你发现了一个宝箱！")
        item = random_item()
        player.add_item(item)
    elif event == 2:
        enemy = random_enemy()
        print(f"你遇到了一个 {enemy.name}！")
        from game.battle import battle
        battle(player, enemy)
    else:
        print("这里什么都没有...")