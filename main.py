from unicodedata import name
import reverse
import ceaser
import transposition


if __name__=="__main__":
    ques = int(input("What would you like to do?\n 1) Reverse String Encryption \n 2) Ceaser Cypher\n 3) Transposition cypher \n"))
    if ques == 1:
        reverse.run()
    if ques == 2:
        ceaser.run()
    if ques == 3:
        ransposition.run()