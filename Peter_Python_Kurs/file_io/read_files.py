df = open("text.txt", mode="a+")

print(df.read())

df.seek(0)
df.write("Morgen hab ich Urlaub!!")

print(df.read())

df.close()
