"""
Write a Python program that takes a username and password as input and checks login credentials using an if–elif–else ladder.
Conditions:
If username is "admin" and password is "pass", print “LOGIN successful”
If both username and password are wrong, print “Wrong Username and Password”
If only the username is wrong, print “Wrong Username”
Otherwise, print “Wrong Password”
"""

#username="admin"
#password="pass"
username=input("Enter username: ")
password=input("Enter password: ")

if (username=="admin" and password=="pass"):
    print("LOGIN successful")
elif (username!="admin" and password!="pass"):
    print("Wrong Username and Password")
elif (username!="admin"):
    print("Wrong Username")
else:
    print("Wrong password")