"""
​"Write a Python program that asks for a username and password. 
Use nested if-else statements so that if the login fails, the program 
specifically checks and prints if 'Both are wrong', or if it is just a 
'Wrong username' or a 'Wrong password'."""
Username=input("Enter Username: ")
Password=input("Enter Password: ")

if Username == "Admin" and Password == "pass":
    print("Login Successfull")
else:
    if Username!="Admin" and Password!="pass":
        print("Both Username and password are wrong")
    else:
        if(Username != "Admin"):
                print("Wrong username")
        else:
                print("Wrong password")
