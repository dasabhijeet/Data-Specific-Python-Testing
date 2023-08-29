#PRogram to calculate basic geometry shape calculations
import sys
class Geometry:
        def triangle_area(self):
            print("Enter values: ")
            b=int(input("Base: "))
            h=int(input("Height: "))
            newdata=(1/2)*b*h
            print("Area is: ",newdata)
            while True:
                    print("Enter 'quit' to exit the program !")
                    inp=input("Input: ")
                    if inp=='quit':
                        exit()
                    elif inp=='QUIT':
                        exit()
                        
        def triangle_perimeter(self):
            print("Enter values: ")
            sideA=int(input("SideA: "))
            sideB=int(input("SideB: "))
            sideC=int(input("SideC: "))
            newdata2=sideA+sideB+sideC
            print("Perimeter: ",newdata2,"units")
            
        def triangle(self):
            print(" (A)Area\n (B)Perimeter\n")
            while True:
                new1=input("Enter type: ")
                if new1 == 'A':
                   geo.triangle_area()
                elif new1 == 'B':
                   geo.triangle_perimeter()
                   
        def square(self):
            print(" (A)Area\n (B)Perimeter\n (C)Diagonal\n")
            while True:
                new1=input("Enter type: ")
                if new1=='A':
                   geo.square_area()
                elif new1=='B':
                   geo.square_perimeter()
                elif new1=='C':
                   geo.square_diagonal()

        def square_area(self):
            new3=int(input("Enter side: "))
            print("Area of square: ",new3**2,"units")
            while True:
                    print("Enter 'quit' to exit the program !")
                    inp=input("Input: ")
                    if inp=='quit':
                        exit()
                    elif inp=='QUIT':
                        exit()
        def square_perimeter(self):
            new3=int(input("Enter side: "))
            print("Perimeter of square:",new3*4,"units")
            geo.exit_menu()       #Exit menu is called for code portability

        def square_diagonal(self):
            new4=int(input("Enter side: "))
            print("Diagonal value:",new4*1.414,"units")
            geo.exit_menu()

        def rectangle(self):
            print("Enter options:\n (A)Area\n (B)Perimeter\n (C)Diagonal\n")
            while True:
                new8=input(" Choice:")
                if new8=='A':
                   geo.rectangle_area()
                elif new8=='B':
                    geo.rectangle_perimeter()
                elif new8=='C':
                    geo.rectangle_diagonal()

        def rectangle_area(self):
            new10=int(input("Side One: "))
            new11=int(input("Side Two: "))
            print("Area is:",new10*new11,"units")
            geo.exit_menu()

        def rectangle_perimeter(self):
            new10=int(input("Side One: "))
            new11=int(input("Side Two: "))
            print("Perimeter is: ",2*(new10+new11),"units.")
            geo.exit_menu()

        def rectangle_diagonal(self):
            new10=int(input("Side One: "))
            new11=int(input("Side Two: "))
            print("Rectangle diagonal:",((new10**2)+(new11**2))**(1/2),"units.")
            geo.exit_menu()

        def circle(self):
            new10=int(input("Enter radius correctly: "))
            new12=input("Enter 'A' for circumference & 'B' for area: ")
            while True:
                    if new12=='A':
                        print("Circumference:",2*3.14*new10,"units.")
                        geo.exit_menu()
                    elif new12=='B':
                        print("Area:",3.14*(new10**2),"units.")
                        geo.exit_menu()
            

        def exit_menu(self):
            while True:
                    print("Enter 'quit' to exit the program !")
                    inp=input("Input: ")
                    if inp=='quit':
                        exit()
                    elif inp=='QUIT':
                        exit()

        def menu(self):
            trin=1
            sq=2
            rect=3
            cir=4
            print("This is a program to calculate basic geometry systems !\n")
            print("WARNING: Do not type an other key other than given ones.")
            print("Options: ")
            print("_(1)Triangle")
            print("_(2)Square")
            print("_(3)Rectangle")
            print("_(4)Circle")
            inp=input("Enter your choice: ")
            if inp == '1':
                geo.triangle
            elif inp=='2':
                geo.square()
            elif inp=='3':
                geo.rectangle()
            elif inp=='4':
                geo.circle()
            else:
                print("Wrong option chosen. Program exiting !")
                exit()
        
#Functions called by creating a object of class Geometry.                
geo=Geometry()
geo.menu()
geo.triangle()

# This program is entirely based upon function calling and using creatively.
# OUTPUT:-

#   This is a program to calculate basic geometry systems !

#WARNING: Do not type an other key other than given ones.
#Options: 
#_(1)Triangle
#_(2)Square
#_(3)Rectangle
#_(4)Circle
#Enter your choice: 1
 #(A)Area
 #(B)Perimeter

#Enter type: A
#Enter values: 
#Base: 12
#Height: 5
#Area is:  30.0
#Enter 'quit' to exit the program !
#Input: quit

        
        










