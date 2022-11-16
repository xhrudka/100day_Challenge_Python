# Morse code translator

Alp_to_Morse = { "a": ".-", "b": "-...", "c": "-.--" }

def selection_function():
    print("For translation to Morse code select 1, for translation from morse code select 2.")
    selection = input()
    print(type(selection))

    if selection == "1":
        print("Please write your alphabetic text:")
        global alp_text
        alp_text = input()
        ToMorseCode_Function()
    else:
        print("Please write your Morse code, between the letter put /:")
        global morse_text
        morse_text = input ()
        FromMorseCode_Function()
    
def ToMorseCode_Function():
    for letter in alp_text:
        for key, value in Alp_to_Morse.items():
            if letter == value:
                print(value)
                
def FromMorseCode_Function():
    print("YZ")
  
print("Hello in Morse code translater!")  
selection_function()
exit