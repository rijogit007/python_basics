# class Classname:
#     var=10



# class Mobile:
# #     # color="red"
    
#     def call(self):
#         print("calling....")
#         print("disconnected")
        
#     def game(self):    
#         print("gaming....")
    
# m1=Mobile()        
# m2=Mobile()        

# m1.call()



# m1.game()


#instance variable


# class Mobile:
#     color="black"
#     def call(self):
#         print("calling")
        
#     def info(self):
        
#         print("colour",self.color)    
        
        
# m1=Mobile()
# m1.info()        

# print(m1.color)
# print(Mobile.color)

class Student:
    def __init__(self,name,age,school):
      
        self.n1=name
        self.a=age
        self.school=school
    def info(self):
        
        print("name is",self.n1)   
        print("age is",self.a)   
        print("school",self.school)   
        
s1=Student("rijo",12,"stphilo")

s1.info()