# game/main.py

from game.player import Player
from game.quest import Quest
from game.map import Area, WorldMap
from game.enemy import Enemy

def main():
    print("欢迎来到冒险世界！")
    player_name = input("请输入你的角色名: ")
    player = Player(player_name, 100, 10)

    # 初始化任务
    quests = [
        Quest("击败哥布林", "击败3只哥布林", 3, 50),
        Quest("击败狼", "击败2只狼", 2, 70)
    ]

    # 初始化地图
    world_map = WorldMap()

    # 创建区域
    forest = Area(
        name="森林",
        description="一片茂密的森林，充满了未知的危险。",
        enemies=[Enemy("哥布林", 50, 5), Enemy("狼", 70, 8)],
        events=["enemy", "treasure", "nothing"]
    )
    village = Area(
        name="村庄",
        description="一个宁静的小村庄，村民们友好而热情。",
        enemies=[],  # 村庄没有敌人
        events=["nothing"]
    )
    mountains = Area(
        name="山脉",
        description="高耸的山脉，寒风凛冽，隐藏着强大的敌人。",
        enemies=[Enemy("巨魔", 100, 12)],
        events=["enemy", "treasure"]
    )

    # 添加区域到地图
    world_map.add_area(forest)
    world_map.add_area(village)
    world_map.add_area(mountains)

    # 连接区域
    world_map.connect_areas("森林", "村庄")
    world_map.connect_areas("森林", "山脉")

    # 设置玩家初始位置
    current_area = village

    while player.is_alive():
        print(f"\n当前位置: {current_area.name}")
        print(f"{player.name} 等级: {player.level}, 经验值: {player.experience}/{player.level * 100}")
        action = input("你要做什么？(1: 探索, 2: 使用物品, 3: 查看任务, 4: 接受任务, 5: 移动, 6: 退出): ")
        if action == "1":
            current_area.explore(player)
        elif action == "2":
            if player.inventory:
                print("你的物品:")
                for i, item in enumerate(player.inventory):
                    print(f"{i + 1}: {item.name}")
                choice = input("选择要使用的物品: ")
                try:
                    item = player.inventory[int(choice) - 1]
                    player.use_item(item)
                except (ValueError, IndexError):
                    print("无效的选择。")
            else:
                print("你没有物品。")
        elif action == "3":
            if player.quests:
                print("你的任务:")
                for quest in player.quests:
                    print(f"{quest.name}: {quest.description} ({quest.progress}/{quest.goal})")
            else:
                print("你没有任务。")
        elif action == "4":
            if quests:
                print("可接受的任务:")
                for i, quest in enumerate(quests):
                    print(f"{i + 1}: {quest.name} - {quest.description}")
                choice = input("选择要接受的任务: ")
                try:
                    quest = quests[int(choice) - 1]
                    player.add_quest(quest)
                    quests.remove(quest)
                except (ValueError, IndexError):
                    print("无效的选择。")
            else:
                print("没有可接受的任务。")
        elif action == "5":
            connected_areas = world_map.get_connected_areas(current_area.name)
            if connected_areas:
                print("你可以移动到以下区域:")
                for i, area_name in enumerate(connected_areas):
                    print(f"{i + 1}: {area_name}")
                choice = input("选择要移动的区域: ")
                try:
                    area_name = connected_areas[int(choice) - 1]
                    current_area = world_map.get_area(area_name)
                except (ValueError, IndexError):
                    print("无效的选择。")
            else:
                print("没有可移动的区域。")
        elif action == "6":
            print("你离开了冒险世界。")
            break
        else:
            print("无效的选择。")

if __name__ == "__main__":
    main()