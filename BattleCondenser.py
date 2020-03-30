with open('cleanBD.txt', 'r') as battle:
    battle = battle.readlines()
    nb = []

    for a,ba in enumerate(battle):
        lba = ba.split()[:]
        #if 'became' in lba: continue
        uType = ''
        res = ''
        eType = ''
        eNation = ''
        lw = ''
        ru = 0
        si = 0
        if lba[0] == 'Your':
            si = 1
            if lba[1] == 'attacking': si = 2
        for a,wo in enumerate(lba[si:]):
            if ru == 0:
                if wo == 'survived':  res = '<F'; ru = 1; continue
                if wo == 'lost':      res = '<S'; ru = 1; continue
                if wo == 'failed':    res = '>F'; ru = 1; continue
                if wo == 'succeeded': res = '>S'; ru = 1; continue
                uType += wo + ' '
            elif ru == 1:
                if wo == 'the': ru = 2
            elif ru == 2:
                if wo == 'pathetic': ru = 1; continue
                eNation += wo + ' '
                ru = 3
            elif ru == 3:
                eType += wo + ' '
        nb.append(uType + '_' + res + '_' + eNation + '_' + eType + '\n')


    fnb = open('interBD.txt', 'w')
    fnb.writelines(nb)
