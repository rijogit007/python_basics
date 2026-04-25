#without instace variable we can call  class.function name

class Student:
    school="st philo"
    @classmethod
    def schoolinfo(cls):
        
        print("school is ",cls.school)
        
        
        
# s1=Student(12)

Student.schoolinfo()        