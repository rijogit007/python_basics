# age=20
# if(age>=18):
#     print("you are an adult")
    
# else:
    
#     print("you are not")    


# marks=int(input("enter the number:"))

# if (marks>=90):
    
#     print("Grade A")
    
# elif(marks>=80):
    
#     print("Grade B")
    
# elif(marks>=70):
    
#     print("Grade D")
    
# else:
    
#     print("Grade E, you are failed ")            

#nested if













age=int(input("enter the age\n"))

if age>=18:
    
    print("you are elibible for reegister\n")
    
    username=input("enter the user name for reg\n")
    password=input("enter the password for reg\n")
    while True:
        
        user=input("enter the username to login\n ")
        passw=input("enter the password to login\n ")\

        if user==username and passw==password:
            print("login succesfully\n")
            break
        else:    
            print("invalid credentials , please login\n")       
else:
    print("you are not 18 , you are not elibible\n")            
            
                
                
                
     