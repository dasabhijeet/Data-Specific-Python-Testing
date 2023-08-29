def print_factors(x):
   value=0
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           value=value+1
           print('Value',value,'is= ',i)

#Entering Section
#Here, a function is designed to pass a value through it...
#Later a input taken through another statement other than print-factors function
#Another counter is given to count and print number of factors...

num=int(input('Enter a number: '))
print_factors(num)
