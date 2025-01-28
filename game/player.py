# game/player.py

import random

class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.inventory = []
        self.experience = 0
        self.level = 1
        self.quests = []  # 玩家的任务列表

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} 对 {enemy.name} 造成了 {damage} 点伤害！")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} 获得了 {item.name}！")

    def use_item(self, item):
        if item.effect == "weapon":
            self.attack += item.attack_bonus
            print(f"{self.name} 装备了 {item.name}，攻击力增加了 {item.attack_bonus}！")
        elif item.effect == "potion":
            self.hp += item.heal_amount
            print(f"{self.name} 使用了 {item.name}，恢复了 {item.heal_amount} HP！")
        self.inventory.remove(item)

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} 获得了 {amount} 点经验值！")
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= self.level * 100:
            self.level += 1
            self.experience = 0
            self.hp += 20
            self.attack += 5
            print(f"{self.name} 升级了！现在是等级 {self.level}！")
            print(f"{self.name} 的HP增加了20点，现在是 {self.hp} HP。")
            print(f"{self.name} 的攻击力增加了5点，现在是 {self.attack} 攻击力。")

    def add_quest(self, quest):
        self.quests.append(quest)
        print(f"你接受了任务: {quest.name}")
        print(f"任务描述: {quest.description}")

    def update_quests(self, enemy_name):
        for quest in self.quests:
            if not quest.is_completed():
                if enemy_name in quest.description:  # 假设任务描述中包含敌人名称
                    quest.update_progress()
                    if quest.is_completed():
                        quest.claim_reward(self)