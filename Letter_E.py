word = input("Enter the word: ")
vowel = "aeiouAEIOU"

count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)    
