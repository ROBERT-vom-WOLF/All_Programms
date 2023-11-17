# Aufgabe 1
names = ["Elise", "Tony", "Matt"]
result1 = [x[0] for x in names]
print(result1)

# Aufgabe 2
numbers = range(1, 7)
result2 = [x for x in numbers if x % 2 == 0]
print(result2)

# Aufgabe 3
nums1 = range(1, 5)
nums2 = range(3, 7)
result3 = [x for x in nums1 if x in nums2]
print(result3)

# Aufgabe 4 slices needed
result4 = [x.lower() for x in names[::-1]]
print(result4)


# Aufgabe 5
nums3 = range(1, 101)
result5 = [x for x in nums3 if x % 12 == 0]
print(result5)


string = "amazing"
result6 = [x for x in string if x not in "aeiou"]
print(result6)
