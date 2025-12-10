import re #expressions module to allow pattern matching
import random #to generate random numbers and choices for password suggestion
import string #to access letters, digits, and punctuation for password suggestion

def analyze_password(password, name):
    errors = 0 #error counter, if 0 it will proceed. If 1 or more it will ask to enter new password
    #-------------RULES-----------------------
    # 0. Name can't be use in password
    if name.lower() in password.lower():
        print('Password cannot contain your name')
        errors += 1

    # 1. Repeating numbers
    if re.search(r'(\d)\1', password):
        print('Your password contains repeating numbers')
        errors += 1 #This code will add to the counter if this if condition will be executed.
                    #Same will happened to the rest of the error +=1 code.
    # 2. Uppercase letter
    if not re.search(r'[A-Z]', password):
        print('Your password must contain one upper case letter')
        errors += 1

    # 3. Lowercase letter
    if not re.search(r'[a-z]', password):
        print('Your password must contain one lower case letter')
        errors += 1

    # 4. Special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>~`/\\\[\];+=_-]', password):
        print('Your password must contain one special character')
        errors += 1

    # 5. Minimum length
    if len(password) < 8:
        print('Your password must be minimum of 8 characters in length')
        errors += 1

    # 6. No spaces allowed
    if " " in password:
        print('Your password cannot contain spaces')
        errors += 1

    return errors

#------------Password suggestion---------------------

def suggest_password(name):
    # This script will generate a password that meets all rules
    special_chars = '!@#$%^&*(),.?":{}|<>~`/\\[];+=_-'
    while True:
        password_chars = [
            random.choice(string.ascii_uppercase), # 1 uppercase
            random.choice(string.ascii_lowercase), # 1 lowercase
            random.choice(special_chars),          # 1 special character
            random.choice(string.digits)           # 1 digit
        ]
        # Fill remaining characters to reach at least 10 chars
        while len(password_chars) < 10:
            password_chars.append(random.choice(string.ascii_letters + string.digits + special_chars))
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        # Ensure it doesn't contain user's name in any case and no repeating numbers
        if name.lower() not in password.lower() and not re.search(r'(\d)\1', password):
            return password

# ------------------ Programm for analyzing -------------------

name = input("Enter your full name: ") #This command will ask to enter their name

while True: #Loop to repeatedly ask for a valid password if one rule is broken.
    password = input("\nEnter your password:")
    
    if password.lower() == "exit": #Check if user wants to exit
        print("Program exited by user. Goodbye!")
        break

    print("\nAnalyzing beeep... beep.. beep...\n")#Im just adding it to make it more polished and fun.

    errors = analyze_password(password, name) #This will call the analyze_password codes to check for password and get error count.

    if errors == 0:#if 0 errors then this will print
        print("\nPassword strength is strong, you are certified unhackable!")
        print("Don't forget your password")
        break#Loop will stop and it will exit
    else:#If errors <= 1 then it will loop again.
        print(f"\nPassword has {errors} errors. Please try again or type exit to quit\n")
        suggestion = suggest_password(name)
        print(f"Password suggestion: {suggestion}\n")
