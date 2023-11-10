# Problem: innerhalb einer verschachtelten funktion möchte man eine break point setzen, der aber nur
# bei einem bestimmten schleifendurchlauf ausgelöst wird, wie kann man das am effektivsten machen
# hier soll der break point nur ausgelöst werden, wenn num 9 und integer 98 ist
def print_number():
    for integer in range(1, 101):
        print(f"Waiting: {integer}")


def main():
    for num in range(1, 11):
        print(f"num: {num}")
        print_number()


main()
