# game/map.py
import random


class Area:
    def __init__(self, name, description, enemies, events):
        self.name = name
        self.description = description
        self.enemies = enemies  # 区域内的敌人列表
        self.events = events  # 区域内的随机事件

    def explore(self, player):
        print(f"你进入了 {self.name}。")
        print(self.description)
        event = random.choice(self.events)
        if event == "enemy":
            enemy = random.choice(self.enemies)
            print(f"你遇到了一个 {enemy.name}！")
            from game.battle import battle
            battle(player, enemy)
        elif event == "treasure":
            print("你发现了一个宝箱！")
            from game.item import random_item
            item = random_item()
            player.add_item(item)
        else:
            print("这里什么都没有...")

class WorldMap:
    def __init__(self):
        self.areas = {}  # 区域名称到区域对象的映射
        self.connections = {}  # 区域之间的连接关系

    def add_area(self, area):
        self.areas[area.name] = area
        self.connections[area.name] = []

    def connect_areas(self, area1_name, area2_name):
        if area1_name in self.areas and area2_name in self.areas:
            self.connections[area1_name].append(area2_name)
            self.connections[area2_name].append(area1_name)
        else:
            print("无法连接区域，区域不存在。")

    def get_connected_areas(self, area_name):
        return self.connections.get(area_name, [])

    def get_area(self, area_name):
        return self.areas.get(area_name)