from queue import PriorityQueue
# Hit Points: 55
# Damage: 8

def do_turn(hp, mp, boss_hp, mana_spent, shield_turns, poison_turns, recharge_turns, is_player_turn):
    
    if recharge_turns > 0:
        mp = mp + 101
    if poison_turns > 0:
        boss_hp = boss_hp - 3

    if is_player_turn == True:
        hp = hp - 1
        turns = []
        if hp <= 0:
            return turns
        if mp < 53:
            return turns
        turns.append((hp, mp - 53, boss_hp - 4, mana_spent + 53, shield_turns - 1, poison_turns - 1, recharge_turns - 1, False))

        if mp < 73:
            return turns
        turns.append((min(hp + 2, 50), mp - 73, boss_hp - 2, mana_spent + 73, shield_turns - 1, poison_turns - 1, recharge_turns - 1, False))

        if mp < 113:
            return turns
        if shield_turns - 1 <= 0:
            turns.append((hp, mp - 113, boss_hp, mana_spent + 113, 6, poison_turns - 1, recharge_turns - 1, False))
        
        if mp < 173:
            return turns
        if poison_turns - 1 <= 0:
            turns.append((hp, mp - 173, boss_hp, mana_spent + 173, shield_turns - 1, 6, recharge_turns - 1, False))
        
        if mp < 229:
            return turns
        
        if recharge_turns - 1 <= 0:
            turns.append((hp, mp - 229, boss_hp, mana_spent + 229, shield_turns - 1, poison_turns - 1, 5, False))

        return turns
    else:
        if shield_turns > 0:
            return [(hp - 1, mp, boss_hp, mana_spent, shield_turns - 1, poison_turns - 1, recharge_turns - 1, True)]
        else:
            return [(hp - 8, mp, boss_hp, mana_spent, shield_turns - 1, poison_turns - 1, recharge_turns - 1, True)]

def main ():
    q = PriorityQueue()
    q.put((0, (50, 500, 55, 0, 0, 0, 0, True)))
    while not q.empty():
        x, curr = q.get()
    possibilities = do_turn(*curr)
        for p in possibilities:
            player_loses = p[0] <= 0
            if player_loses:
                continue
            player_wins = p[2] <= 0
            if player_wins:
                print(x)
                print(p[3])
                return
            q.put((p[3], p))

main()
