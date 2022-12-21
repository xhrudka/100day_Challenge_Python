morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":".-..","h":"....","i":"..","j":".---","k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..","y":"-.--","z":"--.."}

outputList = []
textoutput = ()

def abc_to_morse():
    text = input()  

    # Convert string to the list
    textInList = list(text)

    # Search in the dictionary for a proper key and show the value
    for letter in textInList:
        new_symbol = morse.get(letter)
        outputList.append(new_symbol)
        outputList.append("/")

    # Join the output list to the string by map function
    textoutput='' .join(map(str,outputList))
    print(textoutput)
    
print("Hello in Morse code translater! Enter the text")
abc_to_morse()