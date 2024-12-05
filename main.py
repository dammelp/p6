# Praktikum 6
# Autor: Patrick Dammel
# Gruppe 8
# Datum: 01.12.2024, edited: 05.12.2024


# P.6.1 Collection Games
print("\n6.1 COLLECTION GAMES\n")
# Anmerkung: Abgabe in separaten Dateien dann ab nächster Woche.
# Dann werden auch die Ausgaben zu den Unteraufgaben schöner sein.

#1
maenner = ["Albert", "Bert", "Christian", "Dieter"]
print(f"6.1: {maenner}")
#2
maenner.insert(0,"Ernst")
maenner.append("Frank") # hier stand vorher Dieter, warum auch immer
print(f"6.2:{maenner}")
#3
maenner.remove("Bert")
print(f"6.3: {maenner}")
#4
print(f"6.4: {maenner[2]}")
#5
frauen = ("Adele", "Britney")
print(f"6.5: {frauen}")
#6
maenner[1:3] = frauen
print(f"6.6: {maenner}")
#7
print(f"6.7:{"Adele" in maenner}")
#8
s_maenner = set(maenner)
f_frauen = frozenset(frauen)
print(f"6.8:{s_maenner, f_frauen}")
#9
print(f"6.9: {s_maenner.union(f_frauen)}")
#10
maenner_2 = s_maenner.difference(f_frauen)
frauen_2 = list(f_frauen)
personen = list(s_maenner.union(f_frauen))
print(f"Aufgabe 6.10:\nmaenner_2:{maenner_2}\nfrauen_2:{frauen_2},personen:{personen}")
#11
print(f"6.11: Die Liste personen hat {len(personen)} Einträge") # Antwort: Die Liste personen hat 4 Einträge.
#12
personen.reverse()
print(f"6.12: {personen}")
#13
personen.sort()
print(f"6.13: {personen}")
#14
first = personen[0]
second = personen[1]
print(f"6.14: {first} {second}")
# empfohlene Alternative:
first, second, *stuff = personen
print(f"Alternative 6.14: {first,second}")

#15
print("6.15:")
for index, person in enumerate(personen):
    print(f"Index {index}: {person}")

#16
# zu Aufgabe 16: hier sowohl für frauen als auch für f_frauen, da ich mir nicht sicher bin, was gemeint ist (da frauen ja ein Tupel und keine Liste ist)

# Alternative:
# frauen.clear()
# funktioniert nicht, da frauen keine Liste ist. Ich weiß nicht, was hier gemeint ist.
frauen = ()   # bzw.: frauen = []
f_frauen = []

print(f"6.16: {f_frauen}")
del maenner
try:
    print(maenner)
except NameError as e:
    print(f"6.17: {e}")


A = {1: 'A', 2: 'B', 3: 'C'}
B = {'A': 1, 'B': 4, 'C': 9}
D = {x: x**2 for x in range(1,101)}
print(f"6.18:\n{A}\n{B}\n{D}")



# P.6.2 Gameboard
print("\n\n6.2 GAMEBOARD\n")
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