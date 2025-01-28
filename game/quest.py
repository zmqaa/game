# game/quest.py

class Quest:
    def __init__(self, name, description, goal, reward):
        self.name = name
        self.description = description
        self.goal = goal  # 任务目标，例如击败特定数量的敌人
        self.reward = reward  # 任务奖励，例如经验值或物品
        self.progress = 0  # 任务进度

    def is_completed(self):
        return self.progress >= self.goal

    def update_progress(self, amount=1):
        self.progress += amount
        print(f"任务 '{self.name}' 进度更新: {self.progress}/{self.goal}")
        if self.is_completed():
            print(f"任务 '{self.name}' 已完成！")

    def claim_reward(self, player):
        if self.is_completed():
            print(f"你获得了任务 '{self.name}' 的奖励: {self.reward} 经验值！")
            player.gain_experience(self.reward)
        else:
            print(f"任务 '{self.name}' 尚未完成。")