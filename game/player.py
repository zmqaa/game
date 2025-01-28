# game/player.py

import random

from game.skill import Skill


class Player:
    def __init__(self, name, hp, attack_power):
        # 保留现有的初始化属性
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power  # 改名
        self.defense = 5
        self.inventory = []
        self.experience = 0
        self.level = 1
        self.quests = []

        # 添加新的技能相关属性
        self.skills = []
        self.mp = 50  # 魔法值
        self.max_mp = 50

        # 初始技能
        self.learn_skill(Skill("重击", 15, "造成150%的攻击伤害", 1.5))

    def is_alive(self):
        return self.hp > 0

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} 获得了 {item.name}！")

    def use_item(self, item):
        if item.effect == "weapon":
            self.attack_power += item.attack_bonus
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
            self.attack_power += 5
            print(f"{self.name} 升级了！现在是等级 {self.level}！")
            print(f"{self.name} 的HP增加了20点，现在是 {self.hp} HP。")
            print(f"{self.name} 的攻击力增加了5点，现在是 {self.attack_power} 攻击力。")

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

    def take_damage(self, damage):
        # 计算实际伤害，将防御计算在内
        actual_damage = max(1, damage - self.defense)  # 确保至少造成1点伤害
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage  # 返回实际造成的伤害

    # 在升级时同时提升防御力
    def check_level_up(self):
        if self.experience >= self.level * 100:
            self.level += 1
            self.experience = 0
            self.hp += 20
            self.max_hp += 20
            self.attack += 5
            self.defense += 2  # 每次升级增加2点防御力
            print(f"{self.name} 升级了！现在是等级 {self.level}！")
            print(f"{self.name} 的HP增加了20点，现在是 {self.hp}/{self.max_hp} HP。")
            print(f"{self.name} 的攻击力增加了5点，现在是 {self.attack_power} 攻击力。")
            print(f"{self.name} 的防御力增加了2点，现在是 {self.defense} 防御力。")

    def learn_skill(self, skill):
        """学习新技能"""
        self.skills.append(skill)
        print(f"{self.name} 学会了技能: {skill.name}!")

    def use_skill(self, skill, target):
        """使用技能"""
        if self.mp >= skill.mp_cost:
            self.mp -= skill.mp_cost
            damage = int(self.attack_power * skill.damage_multiplier)
            actual_damage = target.take_damage(damage)
            print(
                f"{self.name} 使用了 {skill.name}，消耗 {skill.mp_cost} MP，对 {target.name} 造成了 {actual_damage} 点伤害！")
            return True
        else:
            print(f"MP不足！需要 {skill.mp_cost} MP！")
            return False

    # 添加MP恢复方法
    def recover_mp(self, amount):
        """恢复MP"""
        self.mp = min(self.max_mp, self.mp + amount)

    def attack_enemy(self, target):  # 攻击方法
        damage = random.randint(1, self.attack_power)
        actual_damage = target.take_damage(damage)
        print(f"{self.name} 对 {target.name} 造成了 {actual_damage} 点伤害！")

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage