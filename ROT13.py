#define prerequisite
abc = "abcdefghijklmnopqrstuvwxyz"
enctext = ""
dectext = ""
#ask user for input
text= input("enter text you want to encrypt or decrypt: ")
text = str.lower(text)
#main program
for i in text:
    ind = abc.find(i)
    ind = (ind+13)%26
    enctext = enctext+(abc[ind])
for i in enctext:
    ind = abc.find(i)
    ind = (ind+13)%26
    dectext = dectext+(abc[ind])
#output
print("output: " , enctext)
print("your input: " , dectext)
