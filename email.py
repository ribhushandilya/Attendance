
email = input("Enter your EMAIL: ")  # j8163@gmail.com, j8163@gmail.in
e = ["jitu@gmail.com", "jituraika@gmail.com", "j8163@gmail.com"]
# gmail, .
k, j, d = 0, 0, 0
length_e = len(e)
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (("com" in email) and (email.count("com") == 1)) or (("in" in email) and (email.count("in") == 1)):
                if (("." in email)) and (("." in email[-4:] or "." in email[-3])):
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == " " or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        print("Invalid Email ID.")
                    else:
                        print("Your email is valid")
                elif " " in email:
                    print("Don't use space in the email")/
                else:
                    print("You forgot/misplace '.' in your email")
            else:
                print("Use '.com' or '.in' with your email ")
        else:
            print("Use '@' in your email")
    else:
        print("First letter should be alphabet")
else:
    print("Type your complete email")


'''if email in e:
    print("Email already exists.")

else:
    e.append(email)
    print("Your email is saved in database successfully.")
    i = int(input(" Enter 1 to check wether your email is saved or not."))
    if i == 1:
        print(e[-1]+" is successfully saved in our Database.")
    elif i == 2:
        exit
    else:
        print("Enter valid choice")
        '''
