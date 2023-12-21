# Done: schreibe eine Funktion 'copy' die als 1. Parameter einen bestehenden File Namen und
#  als 2. Parameter einen neuen File Namen erhalten kann.
#  Die Funktion soll den Inhalt der 1. Datei auslesen und in der 2. Datei abspeichern
#  Teste die Funktion an einer Beispieldatei

def copy(old_file, new_file):
    old = open(old_file, mode="r")
    new = open(f"{new_file}.txt", mode="w")
    new.write(old.read())
    old.close()
    new.close()


copy("test_text.txt", "neue datei")
