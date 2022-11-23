abc = {".-":"a","-...":"b"}
print("Hello in Morse code translater! Enter the morse code with, between the letter put: /")
outputList_abc = []
textoutput_abc = ()
text = input()  
#Text in letter
textInLetters = text.split("/")

# Convert string to the list
#textInList = list(text)
print(text)
print(type(text))
print(textInLetters)
print(type(textInLetters))

for letter_abc in textInLetters:
    new_symbol_abc = abc.get(letter_abc)
    outputList_abc.append(new_symbol_abc)

# Join the output list to the string by map function
textoutput_abc ='' .join(map(str,outputList_abc))
print(textoutput_abc)