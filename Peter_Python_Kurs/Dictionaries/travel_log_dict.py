travel_log = {
    "frankreich": {
        "besuchte_staedte": ["paris", "straßburg"],
        "anzahl_besuche": 12
    },
    "amerika": {
        "besuchte_staedte": ["new york", "las vegas"],
        "anzahl_besuche": 5
    },
    "spanien": {
        "besuchte_staedte": ["barcelona", "madrid"],
        "anzahl_besuche": 20
    }
}
for char_1 in travel_log:
    print(f"\n{char_1}:", end="")
    for char_2 in travel_log[char_1]["besuchte_staedte"]:
        print(f"\n\t\t\t\t\t{char_2}\t\t", end="")
