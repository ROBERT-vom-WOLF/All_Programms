def string_to_table(string):
    rows = string.split("\n")
    table = []
    for row in rows:
        table.append(row.split(","))
    return table


def print_table(table):
    for row in table:
        print("| ", end="")
        for cell in row:
            print(cell.ljust(10), end=" | ")
        print()


string = "Name,Alter,Geschlecht\nMax,30,Männlich\nAnna,25,Weiblich\n"
table = string_to_table(string)
print_table(table)
