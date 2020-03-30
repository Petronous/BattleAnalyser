costDict = {
'Howitzer': 70,
'Mech. Inf': 50,
'Armor II': 80,
'Marines': 60,
'Mobile SAM': 75,
'Paratroopers': 60,
'Anti-Aircraft Artillery': 50,
'Stealth Bomber': 160,
'Helicopter': 100,
'Riflemen': 40,
'Jet Bomber': 140,
'Stealth Fighter': 80,
'Spy': 35,
'Cruise Missile': 60,
'AWACS': 140,
'Battleship': 160,
'AEGIS Cruiser':100,
'Carrier': 160,
'Transport': 50,
'Jet Fighter': 70,
'Fighter': 60,
'Heavy Bomber': 120,
'Artillery': 50,
'Partisan': 0,
'Alpine Troops': 50
}



def AddToDict(thing, dict):
    if not(thing in dict): dict[thing] = 1
    else: dict[thing] += 1

def AddNation(n, d):
    if not(n in d): d[n] = {}

def uProdCost(msg, dict):
    nb = []
    nb.append(msg + ': ')
    sum = 0
    for u, n in dict.items():
        if u.count('and ') > 0:
            u = u[:u.index('and ')-1]
        ul = len(u) - 1
        while u[ul] in ['!', '.', ' ', '\n']:
            u = u[:ul]
            ul -= 1
        sum += costDict[u]*n

    nb.append(str(sum) +'\n\n')
    return nb, sum

def eProdCost(msg, dict):
    nb = []
    nb.append(msg + ': \n')
    ssum = 0
    for na, us in dict.items():
        nb.append('    ' + na + ': ')
        sum = 0
        for u, n in us.items():
            if u.count('and ') > 0:
                u = u[:u.index('and ')-1]
            ul = len(u) - 1
            while u[ul] in ['!', '.', ' ', '\n']:
                u = u[:ul]
                ul -= 1
            sum += costDict[u]*n
        ssum += sum
        nb.append(str(sum) +'\n')
    nb.append('\n')
    return nb, ssum




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
            AddNation(lba[2], es)
            AddToDict(lba[3], es[lba[2]])
            if 'Cruise Missile' in lba[3]:
                AddNation(lba[2], ef)
                AddToDict(lba[3], ef[lba[2]])
        if lba[1] == '<F':
            AddNation(lba[2], ef)
            AddToDict(lba[3], ef[lba[2]])
        if lba[1] == '>S':
            AddToDict(lba[0], us)
            AddNation(lba[2], el)
            AddToDict(lba[3], el[lba[2]])
            if 'Cruise Missile' in lba[3]:
                AddNation(lba[2], uf)
                AddToDict(lba[0], uf[lba[2]])
        if lba[1] == '>F':
            AddToDict(lba[3], uf)

    sum = 0
    ex, s = uProdCost("Your fails", uf)
    sum += s
    nb.extend(ex)
    ex, s = uProdCost("Your losses", ul)
    sum += s
    nb.extend(ex)
    nb.extend(["Your total: " + str(sum) + '\n\n'])

    sum = 0
    ex, s = eProdCost("Enemy fails", ef)
    sum += s
    nb.extend(ex)
    ex, s = eProdCost("Enemy losses", el)
    sum += s
    nb.extend(ex)
    nb.extend(["Enemy total: " + str(sum)])

    fnb = open('Losses.txt', 'w')
    fnb.writelines(nb)
