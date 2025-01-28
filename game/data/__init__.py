# game/data/__init__.py
from .enemies import ENEMY_DATA
from .areas import AREAS
from .quests import QUESTS
from .items import WEAPONS, POTIONS
from .skills import SKILLS

# 可以在这里添加一些辅助函数
def get_monster_data(monster_name):
    return ENEMY_DATA.get(monster_name)

def get_area_data(area_name):
    return AREAS.get(area_name)

def get_quest_data(quest_name):
    for category in QUESTS.values():
        if quest_name in category:
            return category[quest_name]
    return None