import random
inc=int(input('Enter password length:'))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:,?/"
p =  ''.join(random.sample(s,inc ))
print ("Your secure password:",p)
