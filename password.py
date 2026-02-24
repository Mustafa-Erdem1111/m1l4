import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_len = int(input("Lütfen parolanın uzunluğunu giriniz:"))

my_pass = ""

for i in range (pass_len):
    my_pass += random.choice(chars)

print(my_pass)


