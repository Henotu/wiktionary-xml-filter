import io

str = ""

with io.open("./Substantive.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if len(line) > 2:
            if not ("\\" in line):
                if not (":" in line):
                    if not ("," in line):
                        str = str + line + ",\n"

with io.open("./Substantive_filtered.txt", "w", encoding="utf-8") as l:
    l.write(str)
    l.close()
