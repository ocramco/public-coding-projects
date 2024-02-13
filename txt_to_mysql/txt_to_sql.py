databaseName = input("Adja meg az elkészíteni kívánt adatbázis nevét (pl: 2022_maj_em): ")

location = input(r"Adja meg a txt fileok helyét (pl: C:\Users\user\Documents): ")
if location[-1] != "\\": location += "\\" # útvonal végére "\"

out = f"CREATE DATABASE `{databaseName}`;\n" #adatbázis létrehozása
out += f"USE `{databaseName}`;\n" #adatbázis használata

first = True
while first or input("Van még file? (igen/nem)") == "igen":
    first = False
    fileName = input("Adja meg a beolvasni kívánt file nevét (pl: file.txt): ")
    lines = [x.strip().split("\t") for x in open(location+fileName, "r", encoding="utf-8").readlines()]
    rows = lines[1:]
    colNames = lines[0]

    tableName = fileName[:-len(".txt")]
    colTypes = input("Adja meg az oszlopok fajtáit (pl: INT VARCHAR(255) VARCHAR(255)): ").split()
    primaryKey = int(input("Adja meg hanyadik oszlopban (1-től kezdve) van az elsődleges kulcs (pl: 1): "))-1

    # tábla létrehozása
    # minta: CREATE TABLE tableName (id INT, name VARCHAR(255), ev VARCHAR(255))
    out += f"\nCREATE TABLE {tableName} ("
    for i in range(len(colNames)):
        out += f"{colNames[i]} {colTypes[i].upper()}"
        if i == primaryKey: out += " PRIMARY KEY"
        if i != len(colNames)-1:
            out += ", "
        else: # ha utolsó oszlop, zárójel bezárása és újsor
            out += ");\n"

    out += f"INSERT INTO {tableName} VALUES\n" # adatok beszúrása a táblába


    for row in rows:
        out += "(" + ", ".join([f"'{x}'" for x in row]) + "),\n"

    out = out.strip()[:-1]+";\n" # ";" az utolsó sorral együtt majd új sor

out.strip() # ne legyen üres sor a végén

outFile = open(fr"{location}\create{databaseName}.sql", "w", encoding="utf-8")
outFile.write(out)
outFile.close()

print(f"A futtatható sql file elkészült: {location}create{databaseName}.sql")
input("A bezáráshoz nyomjon entert...")