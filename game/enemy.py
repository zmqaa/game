# game/enemy.py

class Enemy:
    def __init__(self, name, hp, attack_power, defense=0, exp_reward=0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.exp_reward = exp_reward
        self.status_effects = []

    # ... 其他方法保持不变 ...

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0
        return actual_damage

    def attack_target(self, target):
        damage = self.attack_power
        actual_damage = target.take_damage(damage)
        print(f"{self.name} 对 {target.name} 造成了 {actual_damage} 点伤害！")

    # 添加状态效果相关方法
    def apply_status_effect(self, effect):
        """添加状态效果"""
        self.status_effects.append(effect)
        print(f"{self.name} 被施加了 {effect.name} 效果！")

    def update_status_effects(self):
        """更新所有状态效果"""
        for effect in self.status_effects[:]:  # 创建副本以便在循环中安全移除
            if effect.is_active:
                effect.apply_effect(self)
                effect.update()
                if not effect.is_active:
                    self.status_effects.remove(effect)
                    print(f"{self.name} 的 {effect.name} 效果消失了。")