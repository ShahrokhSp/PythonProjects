#A Login System
def SignUp ():
    User = input("Please Enter Your Username: ")
    textU = open('C:\\Users\\Alireza\\Desktop\\Project Learning\\Python\\Projects\\Login System\\Login data users.txt',"a")
    User = User + "\n"
    textU.writelines(User)
    Pass = input("Please Enter Your Password: ")
    CPass = input("Please Confirm Your Password: ")
    while Pass != CPass:
        print("WRONG!! Please Try Again: ")
        Pass = input("Please Enter Your Password: ")
        CPass = input("Please Confirm Your Password: ")
    textP = open('C:\\Users\\Alireza\\Desktop\\Project Learning\\Python\\Projects\\Login System\\Login data passes.txt','a')
    Pass += "\n"
    textP.writelines(Pass)
    print("Congrats You are signed up. ")
def Login():
    textU = open('C:\\Users\\Alireza\\Desktop\\Project Learning\\Python\\Projects\\Login System\\Login data users.txt','r')
    U = textU.read()
    User = input("Please Enter Your Username: ")
    while not (User in U):
        User = input("wrong username please try again: ")
    print("Welcome" + User)
    Pass = input("Please Enter Your Password: ")
    textP = open('C:\\Users\\Alireza\\Desktop\\Project Learning\\Python\\Projects\\Login System\\Login data passes.txt','r')
    P = textP.read()
    while not (Pass in P):
        print("Wrong password \n Please Try Again: ")
        Pass = input("Please Enter Your Password: ")
    print("Hello " + User)
        
            
        
        
            

