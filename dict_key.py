student={
    
   "name":"john Doe",
   "age":20,
   "place":"america",
   
   "subjects":
            {"math":20,
            "english":25},  
}


print(student.keys())
print(list(student.keys()))


#update

student.update({"name":"adersh"})


print(student)

student.delete({"name"})

print(student)