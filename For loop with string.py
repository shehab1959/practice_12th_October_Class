text = "Shehab"

for i in text:
    print(i)
    print("Done")
print(len(text)) #6



##
word = input("Type input: ") #hello
count = 0
for i in word:
    print(i)
    count = count + 1
print(count) #5
print(len(word)) #5





##Find total number of vowels from the input string.
text = input("Enter your string here: ")
count = 0
vowels = "aeiouAEIOU"

for i in text:
    if i in vowels:
        print(i)
        count += 1
print("Total vowels are: ", count)