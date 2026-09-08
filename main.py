import datetime

name = input("Wie heißt du? ")
print(f"Hallo {name}! Willkommen in VS Code. Dein Mac-Setup steht!")

heute = datetime.date.today()
semesterstart = datetime.date(2026, 10, 1)
tage_uebrig = (semesterstart - heute).days

print(f"Es sind noch genau {tage_uebrig} Tage bis zum Semesterstart in Bielefeld!")


geburtsjahr_text = input("In welchem Jahr sind Sie geboren? ")
geburtsjahr = int(geburtsjahr_text)
alter = 2026 - geburtsjahr 
print(f"Du bist oder wirst dieses Jahr {alter} Jahre alt!")