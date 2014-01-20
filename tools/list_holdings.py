# -*- coding: utf-8 -*-
from os import listdir

PATH = "..\Crisis of the Confederation\history\provinces\\"
baronies = set()
counties = set()

def main():
    for file in listdir(PATH):
        if file.endswith(".txt"):
            parse(file)
    print(sorted(counties))
    print(sorted(baronies))


def parse(file):
    f = open(PATH + file, 'r')
    try:
        lines = f.readlines()
    except:
        print("skipped", file)
        return
    f.close()

    for num, line in enumerate(lines):
        if "b_" in line:
            line = line.split('=')[0].strip()
            if "b_" not in line:
                continue
            baronies.add(line)
        if "title = c_" in line:
            line = line.split('=')[1].strip()
            counties.add(line)

main()
