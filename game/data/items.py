# game/data/items.py

WEAPONS = {
    "铁剑": {
        "attack_bonus": 5,
        "price": 100,
        "description": "普通的铁剑，略微提升攻击力"
    },
    "青铜剑": {
        "attack_bonus": 8,
        "price": 200,
        "description": "青铜打造的剑，具有不错的攻击力"
    },
    "精钢剑": {
        "attack_bonus": 12,
        "price": 500,
        "description": "精钢打造的剑，拥有优秀的攻击力"
    }
}

POTIONS = {
    "小型治疗药水": {
        "heal_amount": 20,
        "price": 50,
        "description": "回复少量生命值"
    },
    "中型治疗药水": {
        "heal_amount": 40,
        "price": 100,
        "description": "回复中等生命值"
    },
    "大型治疗药水": {
        "heal_amount": 60,
        "price": 200,
        "description": "回复大量生命值"
    }
}