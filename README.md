CYB333 Password Analyzer Project
**Project Overview**
This project is a Python-based Password Strength Analyzer that validates user-created password againts a set of security rules.
The program provides feedback explaining what went wrong and generates a secure password suggestion that can meet all requirments.
The goal of this project is to help user understand what makes a password strong while also offering automated suggestions.

**Project Objectives**
-Enforce common password security best practices
-Prevent weak or predictable password
-Educate users through clear error messages
-Automatically generates strong password

**Features**
-Checks if the password contains user's name
-Detects repeating numbers
-Requires atleast: (One uppercase letter, One lower case letter, One digit, One special character)
-Enforces a minimum password length
-Disables spaces 
-Allows users to retry and exit the program
-Generates a strong and secure password suggestions

**How The Program Works**
1. The user enters their full name.

2. The user is prompted to enter a password.

3. The password is analyzed using predefined rules.

4. If the password is weak:

   Then errors are displayed and strong password suggestion is generated

5. If the password passes all checks:

   Then a success message is shown and the program exits

6. The user can type exit at any time to quit.

**Setup and Running the Code **

Prerequisites
1. Python 3.x installed on your system

Dependencies
This project uses only Python standard library modules, so no external installations are required:

re – for regular expression pattern matching

random – for generating random password characters

string – for accessing letters, digits, and punctuation

**Steps To Run**
1. Save the code in a file

2. Open a terminal or cmd

3. Type python (filename).py

**Password Rules Summary**
1. Not contain the user’s name (case-insensitive)
2. Not contain repeating numbers
3. Include at least one uppercase letter
4. Include at least one lowercase letter
5. Include at least one special character
6. Be at least 8 characters long
7. Contain no spaces
