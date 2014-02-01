# -*- coding: utf-8 -*-
from os import listdir
counties = dict()
b_types = dict()
PATH = "..\Crisis of the Confederation\history\provinces\\"

def list_holdings():
    for file in listdir(PATH):
        if file.endswith(".txt"):
            parse(file)
    for c_name in sorted(counties.keys()):
        if "MISSING" not in counties[c_name][1] and "MISSING" not in counties[c_name][2]:
            continue
        n = c_name.ljust(20, ' ') + '\t'
        c = counties[c_name][1].ljust(25, ' ') + '\t'
        r = counties[c_name][2]
        print(n)# + c + r)
        #for b_name in counties[c_name][0]:
        #    print('\t' + b_name.ljust(25) + '\t' + b_types[b_name])
    


def parse(file):
    f = open(PATH + file, 'r')
    try:
        lines = f.readlines()
    except:
        print("skipped", file)
        return
    f.close()

    c_name = None
    baronies = set()
    culture = "CULTURE_MISSING"
    religion = "RELIGION_MISSING"
    for num, line in enumerate(lines):
        if line[0] == '#' or line[0] == '\n':
            continue
        if "title = c_" in line:
            c_name = line.split('=')[1].strip()
        if c_name == "c_al_hadd":
            print(line.strip())
        if "b_" in line:
            b_name = line.split('=')[0].strip()
            b_type = line.split('=')[1].strip()
            if "b_" not in b_name or b_type not in ["castle", "temple", "city"]:
                continue
            baronies.add(b_name)
            b_types[b_name] = b_type
        if "culture" in line or "arab_samawati" in line:
            culture = line.split('=')[1].strip()
            if '#' in culture:
                culture = culture.split('#')[0].strip()
        if "religion = " in line:
            religion = line.split('=')[1].strip()
        if "1.1.1" in line:
            break
    counties[c_name] = (baronies, culture, religion)

if __name__ == "__main__":
    list_holdings()
