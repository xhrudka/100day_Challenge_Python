abc = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f",".-..":"g","....":"h","..":"i",".---":"j","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","...-":"u","...-":"v",".--":"w","-.--":"y","--..":"z"}
outputList_abc = []
textoutput_abc = ()

def morse_to_abc():
    text = input()  
    #Text in letter and in the list
    textInLetters = text.split("/")

    for letter_abc in textInLetters:
        new_symbol_abc = abc.get(letter_abc)
        outputList_abc.append(new_symbol_abc)

    # Join the output list to the string by map function
    textoutput_abc ='' .join(map(str,outputList_abc))
    print(textoutput_abc)

print("Hello in Morse code translater! Enter the morse code with, between the letter put: /")
morse_to_abc()