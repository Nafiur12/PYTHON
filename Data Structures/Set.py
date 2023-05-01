set1 = set(input("Enter elements of the first set, separated by spaces: ").split())
set2 = set(input("Enter elements of the second set, separated by spaces: ").split())

print("First set: ", set1)
print("Second set: ", set2)
print("Union of 2 sets", set1 | set2 )
print("Intersection of two sets", set1 & set2)
print("Subtraction of two sets", set1 - set2)