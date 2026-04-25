# #parent Class
# class  Person: 
#     def __init__(self,name,contact,diseases):
#         self.name=name
#         self.contact=contact
#         self.diseases=diseases
        
#     def address(self):
#         print(self.name,self.contact)
        
#     def disease(self):
#         print(self.diseases)   
           
# #child class

# class Doctor(Person):
#     pass

# class Patient(Person):
#     pass


# doc1= Doctor("john",888338,"no")        
# pat1= Patient("rijo",8823238338,"yes")   



# doc1.address()
# pat1.address()

# doc1.disease()
# pat1.disease()

# print(doc1.address,doc1.disease)
        
            
            
class Classroom:
    
    def __init__(self,name,reg, status):
        
        self.name=name
        self.reg=reg
        self.status=status
        
        
    def result(self):
        
        print("student name is:",self.name,"regno:",self.reg,"status:",self.status)
        
        
s1=Classroom("rijo",12567,"pass")        
s2=Classroom("jijo",12568,"fail")        
s3=Classroom("tijo",12569,"failed/revaluation")


s1.result()        
s2.result()        
s3.result()        



            
        
    
        
                    
            
            
            
            
            
            
            