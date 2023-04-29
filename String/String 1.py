text= input("Enter a text")
letters=0
vowels=0
consonant=0
words=0
for x in text:
 x=x.lower()
 if x >= 'a' and x <= 'z':
  letters = letters + 1
 if x== 'a' or x== 'e' or x== 'i' or x== 'o'or x=='u'  :
  vowels = vowels + 1

 if x== ' ' :
  words = words + 1

print("The Number of letters in the text",letters)
print("The Number of vowels in the text",vowels)
print("The Number of words in the text",words)