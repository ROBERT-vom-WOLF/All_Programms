print("Ihr Text:")
text = str(input())

letters = text.count("")
print("Zeichenanzahl:", letters)
words = text.count(" ")
int(words)
words = words + 1
print("Wörter:", words)

text_to_list = text.split()


# new_text = text.replace(" ", "\n")

list = [text_to_list]
x = sorted(list)

#print("\n")
#print(new_text)
print(x)






