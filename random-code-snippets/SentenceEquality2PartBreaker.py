import sys                            #sys package imported
class Sentence_Breaker():             #class init
    def sense(self):                  #Function init
        c=0                           #Counter c=0 init
        i=0                           # 'i' init for list variable
        out=" "                       # 'out' and 'out2'-String initialisation
        out2=" "
        inp=input("Enter a line: ")
        inplen=len(inp)               #Input string length counter
        inps=inp.split(" ")           #String splitter
        in2=inplen//2                 # '//' for quotient value & '/' for rem.
        list=inps                     #Assigning tokens in py-List
        for e in inps:                #Token counter using fo loop
            c=c+1
        c2=c//2
        print("Tokens= ",c)
        print("Half Tokens= ",c2)
        for i in range(1,c2):         #Specifying half range upto c2
            out=out+list[i]+" "       #Using list index, tokens are printed
        print("Part 1- ",list[0],out)
        for q in range(c2,c):
            out2=out2+list[q]+ " "    #List indexing for easy token handling
        print("Part 2- ",out2)
        print("\nMain token-",list[0])  #Printing the first token

obbArr=Sentence_Breaker()             # obbArr is object of class
obbArr.sense()                        #Function sense(self) is called.


#This program breaks a given sentence into 2 equal parts
#Python Program
#Written by- Abhijeet_AKD
#Date- 24th October 2018
