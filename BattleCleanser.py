with open('BD.txt', 'r') as battle:
    battle = battle.readlines()
    nb = []

    for a,ba in enumerate(battle):
        lba = ba.split()[:]
        if lba is not [] and lba[0][0] == '(': lba = lba[3:]
        print(lba)
        if 'became' in lba: continue
        if 'conquer' in lba: continue
        if 'upgrade' in lba: continue
        if 'people' in lba: continue
        if 'sell' in lba: continue
        if 'stole' in lba: continue
        if 'Canik' in lba: continue
        if 'Canik2' in lba: continue
        if 'treaty' in lba: continue
        if 'Treaty' in lba: continue
        if 'unitwaittime' in lba: continue
        if 'unitwaittime.'in lba: continue
        if 'inspired' in lba: continue
        if 'Click' in lba: continue
        if 'bought' in lba: continue
        if 'action' in lba: continue
        if 'transported' in lba: continue
        if 'building' in lba: continue
        if 'Can\'t' in lba: continue
        if 'can\'t' in lba: continue
        if len(lba) > 0 and lba[0] == '.': continue

        nb.append(' '.join(lba) + '\n')


    fnb = open('cleanBD.txt', 'w')
    fnb.writelines(nb)
