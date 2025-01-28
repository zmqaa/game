# game/main.py
from game.player import Player
from game.map import WorldMap, Area
from game.data import (
    MONSTERS,
    AREAS,
    QUESTS,
    SKILLS,
    get_monster_data,
    get_area_data
)
from game.enemy import Enemy
from game.skill import Skill


def create_enemy(monster_name):
    """根据怪物名称创建敌人实例"""
    data = get_monster_data(monster_name)
    if data:
        return Enemy(
            name=monster_name,
            hp=data["hp"],
            attack_power=data["attack_power"],
            defense=data["defense"],
            exp_reward=data["exp_reward"]
        )
    return None


def initialize_world():
    """初始化游戏世界"""
    world_map = WorldMap()

    # 创建并添加区域
    for area_name, area_data in AREAS.items():
        # 为该区域创建敌人列表
        enemies = [create_enemy(monster_name) for monster_name in area_data["enemies"]]
        # 过滤掉None值（无效的怪物）
        enemies = [enemy for enemy in enemies if enemy is not None]

        area = Area(
            name=area_name,
            description=area_data["description"],
            enemies=enemies,
            events=area_data["events"]
        )
        world_map.add_area(area)

    # 连接区域
    for area_name, area_data in AREAS.items():
        for connected_area in area_data["connections"]:
            world_map.connect_areas(area_name, connected_area)

    return world_map


def initialize_player(name):
    """初始化玩家角色"""
    player = Player(name, hp=100, attack_power=10)  # 改用 attack_power
    # 添加初始技能
    for skill_name, skill_data in SKILLS.items():
        if skill_data["level_requirement"] == 1:
            skill = Skill(
                name=skill_name,
                mp_cost=skill_data["mp_cost"],
                description=skill_data["description"],
                damage_multiplier=skill_data["damage_multiplier"]
            )
            player.learn_skill(skill)

    return player


def main():
    print("欢迎来到冒险世界！")
    player_name = input("请输入你的角色名: ")

    # 初始化玩家
    player = initialize_player(player_name)

    # 初始化世界地图
    world_map = initialize_world()

    # 设置初始位置（村庄）
    current_area = world_map.get_area("村庄")



    # 游戏主循环
    while player.is_alive():
        print("\n" + "=" * 50)
        print(f"当前位置: {current_area.name}")
        print(f"角色状态:")
        print(f"  {player.name} (等级 {player.level})")
        print(f"  生命值: {player.hp}/{player.max_hp}")
        print(f"  魔法值: {player.mp}/{player.max_mp}")
        print(f"  攻击力: {player.attack_power}")
        print(f"  防御力: {player.defense}")
        print(f"  经验值: {player.experience}/{player.level * 100}")
        print("=" * 50)

        print("\n可用命令:")
        print("1. 探索当前区域")
        print("2. 移动到其他区域")
        print("3. 查看背包")
        print("4. 查看任务")
        print("5. 查看技能")
        print("6. 退出游戏")

        choice = input("\n请选择操作 (1-6): ")

        if choice == "1":
            current_area.explore(player)

        elif choice == "2":
            connected_areas = world_map.get_connected_areas(current_area.name)
            if not connected_areas:
                print("当前区域没有可以移动的地方。")
                continue

            print("\n可以移动到的区域:")
            for i, area_name in enumerate(connected_areas, 1):
                area_data = get_area_data(area_name)
                print(f"{i}. {area_name} (需要等级: {area_data['level_requirement']})")

            area_choice = input(f"\n选择要移动的区域 (1-{len(connected_areas)}), 0返回: ")
            if area_choice == "0":
                continue

            try:
                area_index = int(area_choice) - 1
                if 0 <= area_index < len(connected_areas):
                    target_area_name = connected_areas[area_index]
                    area_data = get_area_data(target_area_name)

                    # 检查等级要求
                    if player.level >= area_data["level_requirement"]:
                        current_area = world_map.get_area(target_area_name)
                        print(f"\n你来到了 {target_area_name}")
                    else:
                        print(f"\n你的等级不足！需要等级 {area_data['level_requirement']}")
                else:
                    print("无效的选择！")
            except ValueError:
                print("请输入有效的数字！")

        elif choice == "3":
            if not player.inventory:
                print("\n背包是空的！")
            else:
                print("\n背包物品:")
                for i, item in enumerate(player.inventory, 1):
                    print(f"{i}. {item.name}")

        elif choice == "4":
            if not player.quests:
                print("\n当前没有任务！")
            else:
                print("\n当前任务:")
                for quest in player.quests:
                    print(f"- {quest.name}: {quest.progress}/{quest.goal}")

        elif choice == "5":
            if not player.skills:
                print("\n还没有学会任何技能！")
            else:
                print("\n已学会的技能:")
                for skill in player.skills:
                    print(f"- {skill.name}: {skill.description} (MP消耗: {skill.mp_cost})")

        elif choice == "6":
            print("\n感谢游玩！再见！")
            break

        else:
            print("无效的选择！")


if __name__ == "__main__":
    main()