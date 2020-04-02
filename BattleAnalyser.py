def AddToDict(thing, dict):
    if not(thing in dict): dict[thing] = 1
    else: dict[thing] += 1

def AddNation(n, d):
    if not(n in d): d[n] = {}

def uDictToText(msg, dict):
    nb = []
    nb.append(msg + ': \n')
    for u, n in dict.items():
        nb.append('    ' + str(n) + 'x ' + u + '\n')
    nb.append('\n')
    return nb

def eDictToText(msg, dict):
    nb = []
    nb.append(msg + ': \n')
    for na, us in dict.items():
        nb.append('    ' + na + ': \n')
        for u, n in us.items():
            nb.append('        ' + str(n) + 'x ' + u + '')
    nb.append('\n')
    return nb

with open('interBD.txt', 'r') as battle:
    battle = battle.readlines()
    nb = []
    us = {}
    ul = {}
    uf = {}
    es = {}
    el = {}
    ef = {}

    for a,ba in enumerate(battle):
        lba = ba.split('_')

        if lba[1] == '<S':
            AddToDict(lba[0], ul)
            if len(lba[2]) > 0:
                AddNation(lba[2], es)
                AddToDict(lba[3], es[lba[2]])
        if lba[1] == '<F':
            AddNation(lba[2], ef)
            AddToDict(lba[3], ef[lba[2]])
        if lba[1] == '>S':
            AddToDict(lba[0], us)
            AddNation(lba[2], el)
            AddToDict(lba[3], el[lba[2]])
        if lba[1] == '>F':
            AddToDict(lba[0], uf)

    nb.extend(uDictToText("You were killing with", us))
    nb.extend(uDictToText("You failed with", uf))
    nb.extend(uDictToText("You lost from attacks", ul))
    nb.extend(eDictToText("Enemies were killing with", es))
    nb.extend(eDictToText("Enemies failed with", ef))
    nb.extend(eDictToText("Enemies lost from attacks", el))

    fnb = open('Table.txt', 'w')
    fnb.writelines(nb)
