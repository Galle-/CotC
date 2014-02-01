# -*- coding: utf-8 -*-

# This tool reads crisis_cultures.txt,
# puts the names in a python dict,
# and lets you generate random names
# of a given gender and given or random culture

from random import choice, randint
    
def parse_names():
    names = {}
    for num, line in enumerate(lines):
        if "male_names" in line:
            gender = 'F' if "female" in line else 'M'
            culture = backtrace_to_culture(num)
            try:
                names[culture]
            except:
                names[culture] = {'F':[], 'M':[]}
            n = num
            while True:
                n += 1
                if "}" in lines[n]:
                    break
                l = [name.split('_')[0] for name in lines[n].strip().split()]
                names[culture][gender].extend(l)
    return names

def backtrace_to_culture(n):
    while True:
        n -= 1
        if lines[n].count('\t') == 1:
            return lines[n].strip()[:-4]

def random_name(gender, culture=None):
    append_culture = ""
    if culture is None:
        culture = choice(list(names.keys()))
        append_culture = " (" + culture + ")"
    pool = names[culture][gender]
    return pool[randint(0,len(pool))] + append_culture

f = open("..\Crisis of the Confederation\common\cultures\crisis_cultures.txt", 'r')
lines = f.readlines()
f.close()
names = parse_names()

if __name__ == "__main__":
    print(names["anglo_terran"])
    print(random_name("F", "anglo_terran"))
    print(random_name("M", "anglo_terran"))
    print(random_name("F"))
    print(random_name("M"))
