import random

while True:
    length = int(input("Enter the length of the password: ")) 
    if length < 8 or length > 20:
        print("Atleast 8 characters and not more than 20 characters")
    else:
        break

while True:
    use_letters = bool(input("Want to use letters? (y/n):")=='y')
    use_numbers = bool(input("Want to use numbers? (y/n):")=='y')
    use_symbols = bool(input("Want to use symbols? (y/n):")=='y')
    if not use_letters and not use_numbers and not use_symbols:
        print("Say yes to atleast one of the options")
    else:
        break
    
def generate_pwd(length, use_letters, use_numbers, use_symbols):
    chars = ""
    pwd=""
    
    if use_letters:
        chars = chars + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        chars = chars + "0123456789"
    if use_symbols:
        chars = chars + "!@#$%^&*()_+"
    if chars == "":
        print("Say yes to atleast one of the options")
    for i in range(length):
        pwd = pwd + random.choice(chars)
    return pwd

print("Your password is: ", generate_pwd(length, use_letters, use_numbers, use_symbols))




