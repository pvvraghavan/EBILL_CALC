import mysql.connector
import os

from os import path

working_path = r'C:\Users\vaish\Desktop\CS'

os.chdir(working_path)

con=mysql.connector.connect(host='localhost',user='root',password='Cynosure9',database='EBILL')


if con.is_connected():
    print("connected")
    cur=con.cursor()
    filename = r'login.txt'

#LOGIN PROGRAM
    def read_credentials(): 
        if path.isfile(filename) is True:
            f = open(filename,'rt')
            a = f.readlines()
            for i in a:
                print(i)
                username = i.split(',')[0]
                passwrd = i.split(',')[1].replace('\n','')
                print('Username: ',username)
                print('Password: ',passwrd)
                login.key = username
                login.value = passwrd
                login.add(login.key,login.value)
            print(login)
        else:
            print('No previous credentials found. Create some user accounts first')

    def update_credentials():
         f = open(working_path+filename,'wt')
         if len(login) == 0:
             print('No previous credentials found. Create some user accounts first')
         else:
             for i in login:
                 print(i)
                 print(login[i])                
                 f.write(i+','+login[i]+'\n')
    def create_account(username,passwrd):
        login.key = username
        login.value = passwrd
      
        login.add(login.key,login.value)
      
        print(login)

    def validate_user(username,passwrd):
        try:
            for key in login:
                if (key == username):
                    if (login[username] == passwrd):
                        print('The user '+ username +' has been authenticated successfully')
                    else:
                        print('The username and password does not match. Please try again')
        except:
            print('The user '+ username +' is not present in the database. Please create an account first')
        

# Create your dictionary class  
    class user_list(dict):  
  
    # __init__ function  
        def __init__(self):
            self = dict()
          
    # Function to add key:value  
        def add(self, key, value):  
            self[key] = value  
  

    if __name__ == "__main__":
        login = user_list()

        entry_key = 0

        while (entry_key != -1):
            entry_key = input("Press 1 to create a new user or 2 to login to your account: ")

            if (int(entry_key) == 1):
                print("Create a login credential first")
                username = input("Enter User name: ") 
                passwrd = input("Enter Password: ")
                create_account(username,passwrd)

            elif (int(entry_key) == 2):

                print("Login to your account")
                username = input("Enter User name: ") 
                passwrd = input("Enter Password: ")
                validate_user(username,passwrd)

            answer = input ("Do you want to continue (y/n)?: ")

            if ((answer == "y") or (answer == "Y")):
                entry_key = 0
            else:
                entry_key = -1

        update_credentials()
                                 
#ELECTRICITY BILL PROGRAM
    
    opt='y'
    while opt == 'y':
        SNO=int(input("Enter SNo:"))
        CNAME=input("Enter your name:")
        UNITS=int(input("Enter amount of electricity consumed:"))
        sub=250
        if UNITS>0 and UNITS<=100:
            x=(unit)*2.5 - sub
            fixedprice = 20
        elif UNITS>100 and UNITS<=200:
            x=(100)*2.5 + (UNITS-100)*3 - sub
            fixedprice = 30
        elif UNITS>200 and UNITS<=500:
           x=(100)*2.5 + (200-100)*3 + (UNITS-400)*4.6 - sub
           fixedprice  = 40
        elif UNITS>500:
            x=(UNITS)*6.6 - sub
            fixedprice = 50
        TOTAL=(x+fixedprice)
        Query = "INSERT INTO Ebillcalc VALUES ({},'{}',{},{})".format(SNO,CNAME,UNITS,TOTAL)
        cur.execute(Query)
        con.commit()
        print("Total amount to be paid:",TOTAL)
        opt=input("Do you want to pay another bill(y/n)?:")
        
    
    
Query="SELECT * FROM Ebillcalc"
cur.execute(Query)
data=cur.fetchall()
for i in data:
    print(i)
con.close()


 

        
        
    
