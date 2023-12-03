import re

with open ("input.txt", "r") as f:
    lines = f.readlines()
    x = 0
    for idx, line in enumerate(lines):
        res = re.finditer(r"[0-9]+", line)
        for r in res:
            surr = ""
            # Top row
            if idx > 0:
                if r.start() == 0:
                    surr += lines[idx-1][r.start():r.end()+1]
                elif r.end() == len(line)-1:
                    surr += lines[idx-1][r.end():r.end()]
                else:
                    surr += lines[idx-1][r.start()-1:r.end()+1]
            # Right and left
            if r.start() == 0:
                surr += line[r.end()]
            elif r.end() == len(line)-1:
                surr += line[r.start()-1]
            else:
                surr += line[r.start()-1] + line[r.end()]
            # Bottom row
            if idx < len(lines)-1:
                if r.start() == 0:
                    surr += lines[idx+1][r.start():r.end()+1]
                elif r.end() == len(line)-1:
                    surr += lines[idx+1][r.start()-1:r.end()]
                else: 
                    surr += lines[idx+1][r.start()-1:r.end()+1]

            if surr != len(surr) * ".":
                x += int(r.group())
    print(x)