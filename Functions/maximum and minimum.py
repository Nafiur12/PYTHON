def min(x, y, z, w):
    min_val = x
    if y < min_val:
        min_val = y
    if z < min_val:
        min_val = z
    if w < min_val:
        min_val = w
    return min_val

def max(x, y, z, w):
    max_val = x
    if y > max_val:
        max_val_val = y
    if z > max_val:
        max_val = z
    if w > max_val:
        max_val = w
    return max_val

# Example usage:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
print("The minimum value is:", min(a, b, c, d))
print("The maximum value is:", max(a, b, c, d))