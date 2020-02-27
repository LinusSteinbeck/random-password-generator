import random

def main():
    choice = input("""
Press 1 for only characters.
Press 2 for characters with numbers.
Press 3 for characters, numbers and special characters
""")
    chars_only_character = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars_character_numbers = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    chars_character_number_special = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
    password = ""

    if choice == "1":
        length = int(input("Input Password length: "))
        while len(password) != length:
            password = password + random.choice(chars_only_character)
            if len(password) == length:
                print("Password: %s" % password)
                again()

    elif choice == "2":
        length = int(input("Input Password lenght: "))
        while len(password) != length:
            password = password + random.choice(chars_character_numbers)
            if len(password) == length:
                print("Password: %s" % password)
                again()

    elif choice == "3":
        length = int(input("Input Password lenght: "))
        while len(password) != length:
            password = password + random.choice(chars_character_number_special)
            if len(password) == length:
                print("Password: %s" % password)
                again()



#-----------------------------------------------------------------------------------------------------------------------------------------------
def again():
    play_again = input("""
Do you want to run the program again?
Y for YES
N for NO
""")

    if play_again.upper() == "N":
        print("bye.")

    elif play_again.upper() == "Y":
        main()

    else:
        again()

main()
