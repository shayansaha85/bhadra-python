username = input("Enter a username : ")
password = input("Enter a password : ")

newpass = ""

db_creds = ('robert45', "Robert123!")

if username == db_creds[0] and password == db_creds[1]:
    ans = input("Do you want to change your password? (y/N) : ")
    if ans.lower() == 'y':
        newpass = input("Enter your new password : ")
        re_enter_pass = input("Re-enter new password : ")
        if re_enter_pass == newpass:
            username = db_creds[0]
            db_creds = list(db_creds)
            db_creds.remove(db_creds[1])
            db_creds.append(newpass)
            db_creds = tuple(db_creds)
            print("Ok password change")
            print("New credentials tuple ",db_creds)
        else:
            print("Password mismatch")
    elif ans.lower() == 'n':
        print("Okay no problem")
    else:
        print("Incorred.. Either enter 'y' or 'N'")
else:
    print("Wrong username or password")