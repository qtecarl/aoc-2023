import re

with open ("input.txt", "r") as f:
    lines = f.readlines()
    x = 0
    dic = {}
    for idx, line in enumerate(lines):
        res = re.finditer(r"[0-9]+", line)
        for r in res:
            surr = ""
            # Top row
            tr = ""
            if idx > 0:
                if r.start() == 0:
                    tr = lines[idx-1][r.start():r.end()+1]
                elif r.end() == len(line)-1:
                    tr =  lines[idx-1][r.end():r.end()]
                else:
                    tr =  lines[idx-1][r.start()-1:r.end()+1]
                surr += tr
                gears = re.finditer(r"\*", tr)
                for gear in gears:
                    row = idx
                    col = gear.start() + r.start()
                    if r.start() == 0:
                        col += 1
                    if (row, col) in dic:
                        dic[(row, col)].append(r.group())
                    else:
                        dic[(row, col)] = [r.group()]
            # Middle row
            mr = ""
            if r.start() == 0:
                mr = line[r.end()]
            elif r.end() == len(line)-1:
                mr = line[r.start()-1]
            else:
                mr = line[r.start()-1] + line[r.end()]
            surr += mr
            gears = re.finditer(r"\*", mr)
            for gear in gears:
                row = idx+1
                if len(mr) == 1:
                    if r.start() == 0:
                        col = r.end()
                    elif r.end() == len(line)-1:
                        col = r.start()+1
                elif mr[0] == '*': 
                    col = r.start()
                else:
                    col = r.end()+1
                if (row, col) in dic:
                    dic[(row, col)].append(r.group())
                else:
                    dic[(row, col)] = [r.group()]
            # Bottom row
            br = ""
            if idx < len(lines)-1:
                if r.start() == 0:
                    br = lines[idx+1][r.start():r.end()+1]
                elif r.end() == len(line)-1:
                    br = lines[idx+1][r.start()-1:r.end()]
                else: 
                    br = lines[idx+1][r.start()-1:r.end()+1]
                surr += br
                gears = re.finditer(r"\*", br)
                for gear in gears:
                    row = idx+2
                    col = gear.start() + r.start()
                    if r.start() == 0:
                        col -= 1
                    if (row, col) in dic:
                        dic[(row, col)].append(r.group())
                    else:
                        dic[(row, col)] = [r.group()]
    
    for v in dic.values():
        if len(v) == 2:
            x += int(v[0]) * int(v[1])
    
    print(x)
                
