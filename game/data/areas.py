# game/data/areas.py

AREAS = {
    "森林": {
        "description": "一片茂密的森林，充满了未知的危险。",
        "enemies": ["哥布林", "狼"],
        "events": ["enemy", "treasure", "nothing"],
        "connections": ["村庄", "山脉"],
        "level_requirement": 1
    },
    "村庄": {
        "description": "一个宁静的小村庄，村民们友好而热情。",
        "enemies": [],
        "events": ["nothing", "shop"],
        "connections": ["森林"],
        "level_requirement": 1
    },
    "山脉": {
        "description": "高耸的山脉，寒风凛冽，隐藏着强大的敌人。",
        "enemies": ["巨魔"],
        "events": ["enemy", "treasure"],
        "connections": ["森林"],
        "level_requirement": 5
    }
}