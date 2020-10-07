#A Login System v2
Users = {'Alireza':'mayor'}
def SignUp ():
    User = input("Please Enter Your Username: ")
    Pass = input("Please Enter Your Password: ")
    CPass = input("Please Confirm Your Password: ")
    while Pass != CPass:
        print("WRONG!! Please Try Again: ")
        Pass = input("Please Enter Your Password: ")
        CPass = input("Please Confirm Your Password: ")
    Users[User] = Pass
    print("Congrats You are signed up. ")
def Login():
    User = input("Please Enter Your Username: ")
    while not (User in Users):
        User = input("wrong username please try again: ")
    print("Welcome " + User)
    Pass = input("Please Enter Your Password: ")
    while Pass != Users[User]:
        print("Wrong password \n Please Try Again: ")
        Pass = input("Please Enter Your Password: ")
    print("Hello " + User)

a=input('Would you like to sign up  or log in?: ')
if a == 'sign up' or a == 'Sign up' or a == 'singup':
    SignUp()
if a == 'Log in' or a == 'log in' or a == 'login':
    Login()
        
            

