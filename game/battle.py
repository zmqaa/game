# game/battle.py

def battle(player, enemy):
    print(f"\n战斗开始！{player.name} VS {enemy.name}")

    while True:
        # 显示战斗状态
        print("\n" + "=" * 40)
        print(f"{player.name} HP: {player.hp}/{player.max_hp} MP: {player.mp}/{player.max_mp}")
        print(f"{enemy.name} HP: {enemy.hp}")
        print("=" * 40)

        # 玩家回合
        print("\n你的回合!")
        print("选择行动:")
        print("1. 普通攻击")
        print("2. 使用技能")
        print("3. 使用物品")

        choice = input("请选择行动 (1-3): ")

        if choice == "1":
            # 普通攻击
            player.attack_enemy(enemy)

        elif choice == "2":
            # 显示可用技能
            if not player.skills:
                print("你还没有学会任何技能！")
                continue

            print("\n可用技能:")
            for i, skill in enumerate(player.skills, 1):
                print(f"{i}. {skill.name} (MP消耗: {skill.mp_cost}) - {skill.description}")
            print("0. 返回")

            skill_choice = input(f"选择要使用的技能 (0-{len(player.skills)}): ")
            if skill_choice == "0":
                continue

            try:
                skill_index = int(skill_choice) - 1
                if 0 <= skill_index < len(player.skills):
                    if player.use_skill(player.skills[skill_index], enemy):
                        pass  # 技能使用成功
                    else:
                        continue  # MP不足，重新选择行动
                else:
                    print("无效的选择！")
                    continue
            except ValueError:
                print("请输入有效的数字！")
                continue

        elif choice == "3":
            # 使用物品
            if not player.inventory:
                print("背包里没有物品！")
                continue

            print("\n可用物品:")
            for i, item in enumerate(player.inventory, 1):
                print(f"{i}. {item.name}")
            print("0. 返回")

            item_choice = input(f"选择要使用的物品 (0-{len(player.inventory)}): ")
            if item_choice == "0":
                continue

            try:
                item_index = int(item_choice) - 1
                if 0 <= item_index < len(player.inventory):
                    player.use_item(player.inventory[item_index])
                else:
                    print("无效的选择！")
                    continue
            except ValueError:
                print("请输入有效的数字！")
                continue

        else:
            print("无效的选择！")
            continue

        # 检查敌人是否被击败
        if not enemy.is_alive():
            print(f"\n你击败了 {enemy.name}！")
            exp_reward = enemy.exp_reward
            player.gain_experience(exp_reward)
            return True

        # 更新玩家的状态效果
        player.update_status_effects()

        # 如果玩家还活着，更新敌人的状态效果
        if player.is_alive():
            enemy.update_status_effects()

        # 敌人回合
        if enemy.is_alive():
            enemy.attack_target(player)  # 使用新的方法名

        # 检查玩家是否被击败
        if not player.is_alive():
            print(f"\n你被 {enemy.name} 击败了...")
            return False

        # 每回合结束恢复少量MP
        mp_recovery = 5
        player.recover_mp(mp_recovery)