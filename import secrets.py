import secrets
import string
print("===============================================")
print("              pasword generator                ")
print("===============================================")
print()
print("step 1:pasword length")
print("a good pasword is atleast 12 characters")
print("longer = harder to guess!")
print()
length = int(input("how many characters?(press enter for 16)")or 16)
print()
answer = input("incluide UPPERCASE letters?[Y/N]").strip().lower
use_uppercase = answer !="n"
answer = input("incluide lowercase letters?[Y/N]").strip().lower
use_lowercase = answer !="n"
answer = input("incluide digits?[Y/N]").strip().lower
use_digits = answer !="n"
answer = input("incluide symbols?[Y/N]").strip().lower
use_symbols= answer !="n"
print()
print("step 3: how many paswords?")
count=int(input("number of paswords(press enter for one):")or 1)
print()
character_pool=""
if use_uppercase:
    character_pool += string.ascii_uppercase
if use_lowercase:
    character_pool += string.ascii_lowercase
if use_digits:
    character_pool += string.digits
if use_symbols:
    character_pool += string.punctuation
if character_pool == "":
    print("Oops!something went wrong")
    print("please try again")
else:
    print("=====================================================")
    print("                   your paswords          ")
    print("=========================================================")
    print()
    for i in range (count):
        pasword=""
    for i in range(length):
        pasword += secrets.choice(character_pool)
        if count == 1:
            print(f"pasword")
        else:
            print(f"{i + 1}. {pasword}")
    print()
    print("Tip:store these in a pasword manager")
    print()

    