import sys
class VowelSystem():
    def replace(self):
        out=""
        out_final=" "
        print("\n\n\nThis is a program which replaces a vowel with star(*) !\n")
        inp=input("Enter a line-string: ")
        inps=inp.split()         # Split function to split up words
        for nr in inps:          # First For-Loop(-Word_For-Loop-)
            for n in nr:         # Second For Loop(-Alphabet_For-Loop-)
                if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":  # If else
                    x="*"
                else:
                    x=n
                out=out+x
            out_final=out_final+out+" "   # Final output variable
            out=""
        print("\nCOMPARE OUTPUTS:")       # ( \n ) works as enter button
        print("\nYour String:  ",inp)     #        in computer keyboards.
        print("Finalised:   ",out_final)
            

axis=VowelSystem()
axis.replace()

# This program replaces a vowel with a star(*) and prints it in terminal screen.
# Speciality of this code is it has two addition stages, first one for each word
# -tokens and second is for adding the modified "out" values(each word).
# Another speciality is it has two for loops one for splitting up words and 2nd
# -for loop is for splitting up every alphabet of that word and checking it in
# alphabet_wise.
