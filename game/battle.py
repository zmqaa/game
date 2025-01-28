# game/battle.py

def battle(player, enemy):
    initial_enemy_hp = enemy.hp  # 记录敌人的初始HP
    while player.is_alive() and enemy.is_alive():
        player.attack_enemy(enemy)
        if enemy.is_alive():
            enemy.attack_player(player)
        print(f"{player.name} 的HP: {player.hp}")
        print(f"{enemy.name} 的HP: {enemy.hp}")
        print("--------")

    if player.is_alive():
        print(f"{player.name} 击败了 {enemy.name}！")
        player.gain_experience(initial_enemy_hp)  # 奖励经验值为敌人的初始HP
        player.update_quests(enemy.name)  # 更新任务进度
    else:
        print(f"{player.name} 被 {enemy.name} 击败了...")