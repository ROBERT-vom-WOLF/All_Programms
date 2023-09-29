import random
game = 1
zweigungen = 0
print("Wilkommen zu Robins unendlichkeits-Labyrinth")
name = input("Aber zuerst, verrate mir noch deinen Namen:\t")
print('''
Eine bunte Gruppe von Abenteurern wagt sich in ein mysteriöses und gefährliches Labyrinth im tiefen Dschungel. 
Ihre Mission ist es, die Geheimnisse und Herausforderungen des Labyrinths zu enthüllen. Doch der Weg führt sie 
durch endlose Gänge, irreführende Wendungen und unvorhersehbare Fallen. Nur die Mutigsten werden den Ausweg 
und die verborgenen Schätze finden. Es ist eine Reise voller Gefahren, aber auch von Gemeinschaft und 
menschlicher Stärke. Die Frage bleibt: Werden sie die Geheimnisse des Labyrinths lüften?
''')

print("Du stehts vor einer Zweigung, die nach [L]inks oder [R]echts geht.")
input("Wo gehst du lang?\n\t")

while game == 1:
    schaetze = ["Diamanten", "Goldbarren", "antike Münzen", "seltene Briefmarken", "Gemälde berühmter Künstler", "Luxusuhren", "Silberbesteck", "Edelsteinschmuck", "Vintage-Weine", "historische Artefakte", "Sammlerstücke aus Porzellan", "Designerhandtaschen", "Echtschmuck"]
    zweigungen = zweigungen + 1
    ereignisse = ["nichts als leere...", "einen gegner...", "einen Schatz...", "eine Tür..."]
    enemy_defeat = random.randint(1, 10)
    geschehen = random.choices(ereignisse, weights=[0, 0, 0, 3], k=1)
    random_leere = random.randint(1, 3)
    schatz = random.choices(schaetze, k=1)

    if geschehen == ['nichts als leere...']:

        print("Du siehts nichts als Leere...")
        if random_leere == 1:
            print('"So oft laufe ich ins Leere!"')
            input("~~~enter zum vortfahren~~~\n")
            print('"Ich werde noch verrueckt!"')
        elif random_leere == 2:
            print('"Schon wieder?"')
            input("~~~enter zum vortfahren~~~\n")
            print('"Das gibts nicht!"')
        else:
            print('"Das geht schon ewig so!"')
            input("~~~enter zum vortfahren~~~\n")
            print('"Langsam werde ich wütend!"')
        print("Wo gehts jetzt weiter?")
        input("[L]inks oder [R]echts?\n\t")

    elif geschehen == ['einen gegner...']:

        print(''"Warte! Da ist was!"'')
        print("Hinter dieser Ecke befindet sich ein Monster! ")
        input("~~~enter zum vortfahren~~~\n")
        print("Du zückst dein Schwert und richtest dich auf")
        print('"Warte ich oder Stürme ich auf ihn auf es zu?"')
        input("~~~enter zum vortfahren~~~\n")
        print("Schnell, du musst dich eintscheiden!")
        attack = input("[W]arten oder [S]türmen?\n\t")
        if attack.lower() == "w":
            if enemy_defeat > 3:
                print("Dieses etwas stürmt auf dich zu, doch du weichst aus!")
                input("~~~enter zum vortfahren~~~\n")
                print("Du holst aus und streckst das Monster nieder!")
                print("Keuchend gehst du weiter...")
                input("~~~enter zum vortfahren~~~\n")
            else:
                print("Das monster fackelt nicht lange und rennt auf dich zu!")
                input("~~~enter zum vortfahren~~~\n")
                print("Du versuchts dein bestest, doch binnen weniger Augenblicke befindest du dich im Himmel")
                print("Nach", zweigungen, "Zweigungen ist es endlich vorbei...")
                print("Game Over")
                input("~~~enter zum beenden~~~\n")
                exit()
        else:
            if enemy_defeat > 3:
                print("Du rennt so schnell wie du kannst auf das Monter zu!")
                input("~~~enter zum vortfahren~~~\n")
                print("Im vorbeirennen schneidest du das Monster zu Hack!")
                print('"Wow" sagst du. "Das training hat sich gelohnt..."')
                print("Keuchend gehst du weiter...")
                input("~~~enter zum vortfahren~~~\n")
            else:
                print("Das monster fackelt nicht lange und rennt auf dich zu!")
                input("~~~enter zum vortfahren~~~\n")
                print("Du versuchts dein bestest, doch binnen weniger Augenblicke befindest du dich im Himmel")
                print("Nach", zweigungen, "Zweigungen ist es endlich vorbei...")
                print("Game Over")
                input("~~~enter zum beenden~~~\n")
                exit()
        print("Doch wo gehts jetzt weiter?")
        input("[L]inks oder [R]echts?\n\t")

    elif geschehen == ['einen Schatz...']:
        #           Schatz
        print("Du kannst deinen Augn nicht trauen!")
        print("Da liegt eine Truhe!")
        input("~~~enter zum vortfahren~~~\n")
        print("Du öffnest die knarrzige Kiste...")
        print("Drinnen liegt:\t", schatz)
        input("~~~enter zum vortfahren~~~\n")
        print("Aber wo gehts jetzt weiter?")
        input("[L]inks oder [R]echts?\n\t")

    elif geschehen == ['eine Tür...']:
        #           Tür
        print("Du siehst leere...")
        print("Warte mal! Da ist was!")
        print("Da ist eine Tür!")
        input("~~~enter zum vortfahren~~~\n")
        print("Du gehst hin...")
        print("Du willst an den Türgriff fassen\ndoch dieser öffnet sich schon von alleine.")
        input("~~~enter zum vortfahren~~~\n")
        print("Es scheint grelles Licht aus der Tür.")
        print("Du gehst hinein")
        input("~~~enter zum vortfahren~~~\n")
        print("Du öffnest deine Augen und merkst, das du in einem Krankenhaus liegst.")
        print('Neben dir leigt ein junger mann und sagt: "Endlich mal wach?" ')
        print('Du fragst: "Wo bin ich?"')
        input("~~~enter zum vortfahren~~~\n")
        print('"Du warst im koma! Die schwester hat mir erzählt, dass dir eine Heckenschere auf den Kopf gefallen sei."')
        print('"Und ich bin hier nur, weil mein Ohr Blutet."')
        input("~~~enter zum vortfahren~~~\n")
        print('"Mein Name ist Josua, schön dich auch mal wach zu sehen."')
        print('Der mann streckt dir die Hand hin.')
        input("~~~enter zum vortfahren~~~\n")
        print('"Mein Name ist ' + name + '"')
        print("Doch dir wird schon wieder Müde und du schläfts ein")
        input("~~~enter zum vortfahren~~~\n")
        print("Als du wieder aufwachst, schaust du dich wieder um.")
        print("Vor dir steht ein alter Mann vor dir und lächelt dich an")
        input("~~~enter zum vortfahren~~~\n")
        print("Du stehst mit ihm zusammen auf einer Wolke, die richtig schön weich ist.")
        print("Nein, das ist nicht Gott!")
        input("~~~enter zum vortfahren~~~\n")
        print("Du reibst dir die Augen und alles wird wieder etwas klarer. ")
        print('"Hey, zieh doch nicht alles alleine weg!", hörst du jemanden sagen')
        input("~~~enter zum vortfahren~~~\n")
        print("Du schaust dich wieder um und merkst, dass du bei deinem besten Kumpel auf dem Sofa liegts")
        print("Du warst in dem Labyrinth garnicht, du hast einfach nur fantasiert.")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tErfolg freigeschaltet:")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t~~Auf Wolke 7~~")
        input("~~~enter zum beenden~~~\n")
        exit()

    else:
        print("Error!!\ngeschehen:", geschehen)
        exit()
