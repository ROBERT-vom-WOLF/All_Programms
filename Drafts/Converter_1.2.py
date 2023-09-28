abc = input("[V]erschlüsseln oder [E]ntschlüsseln?\t")
loop = 1


def fragestellung():
    global abc
    if not abc.lower == "v" or not abc.lower == "e":
        abc = input("[V]erschlüsseln oder [E]ntschlüsseln?\t")
    return abc


def converter(converter_text):
    global letters
    loop_count = 0
    converted = ""
    while not letters == loop_count:
        text = converter_text[loop_count:(loop_count + 1)]
        print(f"\n Mission:\t{text}")
        if (' ') in text.lower():
            if " " in text:
                converted = converted + "s12nhms34_"
            print("~~(space)~~ converted")

        if "a" in text.lower():
            if "a" in text:
                converted = converted + "l72dhlo98_"
            if "A" in text:
                converted = converted + "L72dhlo98_"
            print("~~a~~ converted")

        if "b" in text.lower():
            if "b" in text:
                converted = converted + "l78aiko56_"
            if "B" in text:
                converted = converted + "L78aiko56_"
            print("~~b~~ converted")

        if "c" in text.lower():
            if "c" in text:
                converted = converted + "l67gsht08_"
            if "C" in text:
                converted = converted + "L67gsht08_"
            print("~~c~~ converted")

        if "d" in text.lower():
            if "d" in text:
                converted = converted + "lks8onkbh_"
            if "D" in text:
                converted = converted + "Lks8onkbh_"
            print("~~d~~ converted")

        if "e" in text.lower():
            if "e" in text:
                converted = converted + "lop26712h_"
            if "E" in text:
                converted = converted + "Lop26712h_"
            print("~~e~~ converted")

        if "f" in text.lower():
            if "f" in text:
                converted = converted + "l5ghbs5ns_"
            if "F" in text:
                converted = converted + "L5ghbs5ns_"
            print("~~f~~ converted")

        if "g" in text.lower():
            if "g" in text:
                converted = converted + "lmaoksp04_"
            if "G" in text:
                converted = converted + "Lmaoksp04_"
            print("~~g~~ converted")

        if "h" in text.lower():
            if "h" in text:
                converted = converted + "lpans6g87_"
            if "H" in text:
                converted = converted + "Lpans6g87_"
            print("~~h~~ converted")

        if "i" in text.lower():
            if "i" in text:
                converted = converted + "l2nd6skn4_"
            if "I" in text:
                converted = converted + "L2nd6skn4_"
            print("~~i~~ converted")

        if "j" in text.lower():
            if "j" in text:
                converted = converted + "l25ms45ht_"
            if "J" in text:
                converted = converted + "L25ms45ht_"
            print("~~j~~ converted")

        if "k" in text.lower():
            if "k" in text:
                converted = converted + "l25dbstze_"
            if "K" in text:
                converted = converted + "L25dbstze_"
            print("~~k~~ converted")

        if "l" in text.lower():
            if "l" in text:
                converted = converted + "l5hs6ncun_"
            if "l" in text:
                converted = converted + "L5hs6ncun_"
            print("~~l~~ converted")

        if "m" in text.lower():
            if "m" in text:
                converted = converted + "l7rsdbxzg_"
            if "M" in text:
                converted = converted + "L7rsdbxzg_"
            print("~~m~~ converted")

        if "n" in text.lower():
            if "n" in text:
                converted = converted + "l53b6tb8n_"
            if "N" in text:
                converted = converted + "L53b6tb8n_"
            print("~~n~~ converted")

        if "o" in text.lower():
            if "o" in text:
                converted = converted + "l54vb6nts_"
            if "O" in text:
                converted = converted + "L54vb6nts_"
            print("~~o~~ converted")

        if "p" in text.lower():
            if "p" in text:
                converted = converted + "l26bt6nab_"
            if "P" in text:
                converted = converted + "L26bt6nab_"
            print("~~f~~ converted")

        if "q" in text.lower():
            if "q" in text:
                converted = converted + "l6rbnasam_"
            if "Q" in text:
                converted = converted + "L6rbnasam_"
            print("~~q~~ converted")

        if "r" in text.lower():
            if "r" in text:
                converted = converted + "lzb86nams_"
            if "R" in text:
                converted = converted + "Lzb86nams_"
            print("~~r~~ converted")

        if "s" in text.lower():
            if "s" in text:
                converted = converted + "l9imabsn0_"
            if "S" in text:
                converted = converted + "L9imabsn0_"
            print("~~s~~ converted")

        if "t" in text.lower():
            if "t" in text:
                converted = converted + "l5vbna7ms_"
            if "T" in text:
                converted = converted + "L5vbna7ms_"
            print("~~t~~ converted")

        if "u" in text.lower():
            if "u" in text:
                converted = converted + "l5brnas5g_"
            if "u" in text:
                converted = converted + "L5brnas5g_"
            print("~~u~~ converted")

        if "v" in text.lower():
            if "v" in text:
                converted = converted + "loiansm67_"
            if "V" in text:
                converted = converted + "Loiansm67_"
            print("~~v~~ converted")

        if "w" in text.lower():
            if "w" in text:
                converted = converted + "l65bnams_"
            if "w" in text:
                converted = converted + "L65bnams_"
            print("~~w~~ converted")

        if "x" in text.lower():
            if "x" in text:
                converted = converted + "l989887m_"
            if "x" in text:
                converted = converted + "L989887m_"
            print("~~x~~ converted")

        if "y" in text.lower():
            if "y" in text:
                converted = converted + "l5vbanms_"
            if "y" in text:
                converted = converted + "L5vbanms_"
            print("~~y~~ converted")

        if "z" in text.lower():
            if "z" in text:
                converted = converted + "l45bsams_"
            if "z" in text:
                converted = converted + "L45bsams_"
            print("~~z~~ converted")

    #    else:
    #        print(f"Error:\t{text} got not converted")
        loop_count += 1
    print(converted)
    input("\nEnter, um das programm zu beenden\n")
    exit()


def normalizer(normalizer_text):
    global letters
    new_text = ""
    normalizer_count = 0
    while letters > normalizer_count:
        code = normalizer_text[normalizer_count:(normalizer_count + 10)]
        print(f"Mission:\t{code}")
        if code == "s12nhms34_":
            new_text = new_text + " "
        normalizer_count += 10

    print(f"Neuer Text:\n{new_text}")

    print("normalize")


while loop == 1:
    if abc.lower() == "v":
        answer = "verschlüsseln"
        loop = 0
        text_raw = input("Dein Text:\n\n")
        letters = text_raw.count("")
        converter(converter_text=text_raw)
    elif abc.lower() == "e":
        answer = "entschlüsseln"
        loop = 0
        text_raw = input("Dein Text:\n\n")
        letters = text_raw.count("")
        normalizer(text_raw)
    else:
        fragestellung()

# alles in eine while loop, dann [] für den text srg verwenden
# eine variable auf 0 setzen, dann die variable in die klammer: text[variable, (variable + 1)]
# am ende der loop variable + 1
#
# geht buchstabe für buchstabe duch den str
#
#
