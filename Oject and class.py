class Student:
    student_count=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
        Student.student_count+=1
    def printsttudentdata(self):
        print('name:',self.name,'id: ',self.id)
std1=Student('leo',102)
std2=Student('nahom',101)
std3=Student('nati',100)
print('total student',Student.student_count)
std1.printsttudentdata()
std2.printsttudentdata()
std3.printsttudentdata()




