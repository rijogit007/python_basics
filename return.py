# #return


# # def findsum(a=0,b=0):
# #     s=a+b
# #     print(s)
    
# # findsum(10,20)    


# #scope of variable- Local variable/local scope and global variable/global scope


# # def findsum(a=0,b=0):
# #     s=a+b
# #     print(s)
    
# # findsum(10,20)    
# # print(s)  #s is only acces inside the function


# s=0
# def findsum2(a,b):
#     s=a+b
#     print(s)
    
# findsum2(2,3)
# print(s)      #access the variable inside and outside the fumction, inside the function call function s, and outside initialize s


s=0
def findsum2(a,b):
    s=a+b
    print(s)
    return "function ended"
   
print(findsum2(1,2))     