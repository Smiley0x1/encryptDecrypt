from unicodedata import name
import reverse
import ceaser


if __name__=="__main__":
    ques = int(input("What would you like to do?\n 1) Reverse String Encryption \n 2) Ceaser Cypher\n"))
    if ques == 1:
        reverse.run()
    if ques ==2:
        ceaser.run()