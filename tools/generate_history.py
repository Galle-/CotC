# -*- coding: utf-8 -*-
from os import listdir
from copy import deepcopy
import random
import buildings


PATH = "..\Crisis of the Confederation\history\provinces\\"

files = [file for file in listdir(PATH) if ".txt" in file]

def main():
    for file in files:
        f = open(PATH + file, 'r')
        original_lines = f.readlines()
        f.close()

        lines = [line.strip() for line in original_lines if line.strip()]
        new_lines = deepcopy(original_lines)

        b_types = dict()
        write = dict()

        for num, line in enumerate(lines):
            if line[0] == '#':
                continue

            if "title = " in line:
                c_name = line.split('=')[1].strip()

            for b_type in ["castle", "city", "temple"]:
                if "= " + b_type in line:
                    b_name = line.split('=')[0].strip()
                    b_types[b_name] = b_type

            if line[-1] == '{' and lines[num+1][0] == '}':
                date = line.split('=')[0].strip()
                write[date] = list()
                for b_name in b_types:
                    b_type = b_types[b_name]
                    
                    more = ""
                    if b_name in buildings.ss_list:
                        more += " space_station"
                    if b_name in buildings.asteroid_list:
                        more += " asteroids"
                        
                    temps = ["burning", "hot", "warm", "optimal_hot", "optimal_cold", "cool", "cold", "frozen"]
                    temp = random.choice(temps)
                    if "_i_" in b_name: # close to star
                        temp = temps[random.randint(0,1)] # burning or hot
                    elif "_ii_" in b_name: # second closest to star
                        temp = temps[random.randint(0,2)] # burning to warm
                    elif "_iii_" in b_name: # third closest to star
                        temp = temps[random.randint(1, 4)] # hot to optimal (either)
                    elif "_iv_" in b_name: # fourth from star
                        temp = temps[random.randint(3, 6)] # optimal (either) to cold
                    elif "_v_" in b_name: # fifth from star
                        temp = temps[random.randint(4, 6)] # cold optimal to cold
                    elif "_vi_" in b_name: # sixth from star
                        temp = temps[random.randint(5, 7)] # cool to frozen
                    
                    more += ' ' + temp
                    
                    if date == "1.1.1":
                        write[date].extend(['\t' + b_name + " = " + b + '\n' for b in buildings.create(b_type + more)] + ['\n'])

        if len(write) == 0: # nothing to change in this file
            continue

        offset = 1
        for num, line in enumerate(original_lines):
            for date in write.keys():
                if date in line:
                    for new_line in write[date]:
                        new_lines.insert(num + offset, new_line)
                        offset += 1

        f = open(PATH + file, 'w')
        original_lines = f.writelines(new_lines)
        f.close()
        
if __name__ == "__main__":
    main()
