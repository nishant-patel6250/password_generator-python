import random
import string
print("Welcome to the password Generator")
no_l=int(input("How many letters would you like in your password?\n"))
no_s=int(input("How many symbols would you like?\n"))
no_n=int(input("How many numbers would you like?\n"))
# Create a list with all lowercase and uppercase letters
alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
# Get all punctuation symbols
symbols = list(string.punctuation)
num=['0','1','2','3','4','5','6','7','8','9']
password=[]
for i in range(0,no_l):
    rand_alph = random.choice(alphabet)
    password.insert(i,rand_alph)
for i in range(no_l,no_l+no_s):
    rand_sym=random.choice(symbols)
    password.insert(i, rand_sym)
for i in range(no_l+no_s,no_l+no_s+no_n):
    rand_int = random.choice(num)
    password.insert(i, rand_int)
# print(password)
random.shuffle(password)
# print(password)
list=""
for i in range(no_l+no_s+no_n):
    list=list+password[i]
print(list)