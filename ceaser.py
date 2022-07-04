#What is a Ceaser Cypher?
    #A Ceaser cypher takes whatever string you enter, and uses a key(X) and list of symbols to change the letter by X # of places  
import pyperclip

def run():
        confirmation = int(input("You have selected Reverse string encryption\n Would you like to: \n 1) Encrypt \n 2) Decrypt\n"))
        if confirmation == 1:
            encrypt(input("Enter string to encrypt:\n"))
        elif confirmation == 2:
            decrypt(input("Enter string to decrypt:\n"))
        else:
            print("Invalid input, try again")       
        
def encrypt(message):
    key = int(input("What is the key? (Shift integer)\n"))
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_+{}|:"<>?~`-=[]\\;\',./'
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex= translatedIndex + len(SYMBOLS)
                
            translated= translated + SYMBOLS[translatedIndex]

        else:
                translated = translated + symbol
    print(translated)
        
def decrypt(message):
    key = int(input("What is the key? (Shift integer)\n"))
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()_+{}|:"<>?~`-=[]\\;\',./'
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex=SYMBOLS.find(symbol)
            
            translatedIndex = symbolIndex - key
            
            if translatedIndex>= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex<0:
                translatedIndex= translatedIndex + len(SYMBOLS)
            translated= translated + SYMBOLS[translatedIndex]

        else:
                translated = translated + symbol
    print(translated)