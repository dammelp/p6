# P.6.1 Collection Games

maenner = ["Albert", "Bert", "Christian", "Dieter"]

maenner.insert(0,"Ernst")
maenner.append("Dieter")
maenner.remove("Bert")
print(maenner[2])
frauen = ("Adele", "Britney")
maenner[1:3] = frauen
print("Adele" in maenner)
s_maenner = set(maenner)
f_frauen = frozenset(frauen)
print(s_maenner.union(f_frauen))
maenner_2 = s_maenner.difference(f_frauen)
frauen_2 = list(f_frauen)
personen = list(s_maenner.union(f_frauen))
print(len(personen)) # Antwort: Die Liste personen hat 4 Einträge.
personen.reverse()
personen.sort()
first = personen[0]
second = personen[1]
for index, person in enumerate(personen):
    print(f"Index {index}: {person}")

# zu Aufgabe 16: hier sowohl für frauen als auch für f_frauen, da ich mir nicht sicher bin, was gemeint ist (da frauen ja ein Tupel und keine Liste ist)
frauen = ()   # bzw.: frauen = []
f_frauen = []
del maenner

A = {1: 'A', 2: 'B', 3: 'C'}
B = {'A': 1, 'B': 4, 'C': 9}
D = {x: x**2 for x in range(1,101)}



# P.6.2 Gameboard

def gameboard(cols, rows, content):
    rows_list = list(rows)

    print("  | " + " | ".join(cols) + " |")
    print("---" + "----" * len(cols) + "-")

    for r in rows_list:
        row_content = [content.get(f"{c}{r}", " ") for c in cols]
        print(f"{r} | " + " | ".join(row_content) + " |")



# Test_1
gameboard("ABC", "123", {"B2":"X"})
# Test_2
d = {"A1": "X", "A2":"O", "C3":"X", "C1":"O"}
gameboard("ABCD", "1234", d)