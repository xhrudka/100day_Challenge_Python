morse = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":".-..","h":"....","i":"..","j":".---","k":"-.-","l":".---","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..","y":"-.--","z":"--.."}
abc = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f",".-..":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","...-":"u","...-":"v",".--":"w","-.--":"y","--..":"z"}
outputList_abc = []
textoutput_abc = ()
outputList = []
textoutput = ()

def abc_to_morse():
    print("Enter your text, which has to be encrypted into Morse code:")
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
    print("Encrypt code is: ")
    print(textoutput)
    

def morse_to_abc():
    print("Enter your morse code, which has to be dencrypted:")
    text = input()  
    #Text in letter and in the list
    textInLetters = text.split("/")

    for letter_abc in textInLetters:
        new_symbol_abc = abc.get(letter_abc)
        outputList_abc.append(new_symbol_abc)

    # Join the output list to the string by map function
    textoutput_abc ='' .join(map(str,outputList_abc))
    print("Decrypted message is: ")
    print(textoutput_abc)

print("Back in time, 15 years ago and Welcome in the morse code translator!")
print("Please press 1 if you like to entrypt your text and press 2 if you like to decrypt your morse code: ")
status = input()
match status:
    case "1":
        abc_to_morse()
    case "2":
        morse_to_abc()