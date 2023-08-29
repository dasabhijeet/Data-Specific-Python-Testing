num_in=int(input("Enter a number to check AmstrongNess :"))
num_out=0
temp=num_in
while temp > 0:
    num_mod=temp%10
    num_out+=num_mod ** 3.0
    temp=temp//10 
 
if num_out == num_in:
 print("Yes, Test Passed !, Value:",num_out)
else:
 print("Sorry, Test couldn't pass out !, Value:",num_out)


#Mistakes may Happen Points:-
# 1) Double slashes(//) means floor division.
# 2) Brackets in 'if' & 'while' statements.
# 3) Variable type should be declared properly in inputs.
