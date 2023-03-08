name = input("Enter name : ")
username = input("Enter a username : ")
password = input("Enter a password : ")

creds = []
creds.append(username)
creds.append(password)

credentials = tuple(creds)

print(credentials)