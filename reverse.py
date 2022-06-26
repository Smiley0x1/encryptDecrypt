def run():
        confirmation = int(input("You have selected Reverse string encryption\n Would you like to: \n 1) Encrypt \n 2) Decrypt\n"))
        if confirmation == 1:
            encrypt(input("Enter string to encrypt:\n"))
        elif confirmation == 2:
            decrypt(input("Enter string to decrypt:\n"))
        else:
            print("Invalid input, try again")       
        
def encrypt(enc):
    new = []
    for l in enc:
        if new ==[]:
            new.append(l)
        else:
            new.insert(0,l)
    print("".join(map(str, new)))
    
def decrypt(dec):
    new = []
    for l in dec:
        if new ==[]:
            new.append(l)
        else:
            new.insert(0,l)
    print("".join(map(str, new)))
    