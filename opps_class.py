

# class Operations:
#     def set_values(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         self.addition = self.a + self.b
#         print(self.addition)
#     def sub(self):
#         self.subtraction  = self.a - self.b
#         print(self.subtraction)
#     def multi(self):
#         self.multiplication = self.a * self.b
#         print(self.multiplication)
#     def div(self):
#         self.division = self.a / self.b
#         print(self.division)
# obj = Operations()
# obj.set_values(20,30)
# obj.add()
# obj.sub()
# obj.multi()
# obj.div()


#  if we want to execute only one function with different value than others
#
# class Operations:
#     def set_values(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         self.addition = self.a + self.b
#         print(self.addition)
#     def sub(self,c,d):
#         # self.a = a
#         # self.b = b
#         self.c = c
#         self.d = d
#         self.subtraction  = self.c - self.d
#         print('subtracting c and d is : ',self.subtraction)
#     def multi(self):
#         self.multiplication = self.a * self.b
#         print(self.multiplication)
#     def div(self):
#         self.division = self.a / self.b
#         print(self.division)
# obj = Operations()
# obj.set_values(20,30)
# obj.add()
# obj.sub(40,30)
# obj.multi()
# obj.div()





# creating user input

# class Operations:
#     def set_values(self, a, b):
#         self.a = a(input('enter 1 st number : '))
#         self.b = b(input('enter 2 nd number '))
#     def add(self):
#         self.addition = self.a + self.b
#         print(self.addition)
#     def sub(self):
#         self.subtraction  = self.a - self.b
#         print(self.subtraction)
#     def multi(self):
#         self.multiplication = self.a * self.b
#         print(self.multiplication)
#     def div(self):
#         self.division = self.a / self.b
#         print(self.division)
# obj = Operations()
# obj.set_values(a,b)
# obj.add()
# obj.sub()
# obj.multi()
# obj.div()





# import  random
# class student():
#     def register(self,name,age):
#         self.name = name
#         self.age = age
#         self.rollno = random.randint(1000,2000)
#         self.college = "SRM UNIVERSITY"
#     def get_student_details(self):
#         print("sudent details are : \n name : {}\n  age : {} \n Rollno : {}\n College: {} \n"
#               .format(self.name,self.age,self.rollno,self.college))
#
# stu1 = student()
# stu1.register('saikumar',24)
# stu1.get_student_details()
#
# stu2 = student()
# stu2.register('sumanth',23)
# stu2.get_student_details()
#
# l = [stu1,stu2]
# print('Students advailable are : ')
# for data in l:
#     data.get_student_details()
#     break


#  using __init__

# class Operations:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def add(self):
#         self.addition = self.a + self.b
#         print('after addition : ',self.addition)
#     def sub(self,c,d):
#         self.c = c
#         self.d = d
#         self.subtraction = self.c - self.d
#         print('after subtracting : ', self.subtraction)
#     def multi(self):
#         self.multiplication = self.a * self.b
#         print('after multiplying : ', self.multiplication)
#     def div(self):
#         self.division = self.a / self.b
#         print('after division : ', self.division )
# obj = Operations(10,20)
# obj.add()
# obj.sub(100,200)
# obj.multi()
# obj.div()





# class Operations():
#     def add(self,a,b):
#         self.a = a
#         self.b = b
#         self.addition = self.a + self.b
#         print(self.addition)
#     def sub(self):
#         self.subtraction = self.a - self.b
#         print(self.subtraction)
#
#
# obj = Operations()
# obj.add(10,20)
# obj.sub()







#  creating employee details

# class Employee_details():
#     def set_emp(self,empname,empid,emp_role,Inproject):
#         self.employee_name = empname
#         self.employee_id = empid
#         self.employee_role = emp_role
#         self.project_details = Inproject
#     def get_employee_details(self):
#         print("Employee details are : \n Employee_name : {}\n "
#               " Employee_IdNo : {} \n Employee_Role : {}\n "
#               "Project_Details : {} \n "
#               .format(self.employee_name,self.employee_id,self.employee_role,self.project_details))
# obj = Employee_details()
# obj.set_emp('sai',1234,'Application Developer','Yes')
# obj.get_employee_details()
#
# obj2 = Employee_details()
# obj2.set_emp('sumanth',4321,'APPLICATION DEVELOPER','YES')
# obj2.get_employee_details()



# class Employee_details():
#     def set_emp(self,empname,empid,emp_role,Inproject):
#         self.employee_name = empname
#         self.employee_id = empid
#         self.employee_role = emp_role
#         self.project_details = Inproject
#     def get_employee_details(self):
#         print("Employee details are : \n Employee_name : {}\n "
#               " Employee_IdNo : {} \n Employee_Role : {}\n "
#               "Project_Details : {} \n "
#               .format(self.employee_name,self.employee_id,self.employee_role,self.project_details))
# print("obj1")
# obj = Employee_details()
# obj.set_emp(input("enter name :"), input("enter id : "), input("enter emp_role : "),input("Inproject(yes/no) : "))
#obj.get_employee_details()

# print("obj2")
# obj2 = Employee_details()
# obj2.set_emp(input("enter name :"), input("enter id : "), input("enter emp_role : "),input("Inproject(yes/no) : "))
#obj2.get_employee_details()



# obj2 = Employee_details()
# obj2.set_emp('sumanth',4321,'APPLICATION DEVELOPER','YES')
# obj2.get_employee_details()

# l = [obj,obj2]
# for data in l :
#     data.get_employee_details()




# Getting student eligibility details

# import random
# class student():
#     def register(self,name,age):
#         self.name = name
#         self.age = age
#         self.rollno = random.randint(1000,2000)
#         self.college = "SRM UNIVERSITY"
#         self.attendence = random.randint(50,90)
#         self.eligibility = 55
#     def get_student_details(self):
#         print("sudent details are : \n name : {}\n  age : {} \n Rollno : {}\n College: {} \n Attendence : {}\n"
#               .format(self.name, self.age, self.rollno, self.college, self.attendence))
#     def exam_eligibility(self):
#         # print(eligibility)
#         if self.eligibility  <= self.attendence:
#             print(" eligible")
#         else:
#             print(" Not eligible")
#
#     def attendence_class(self):
#         self.attendence = 0
#
#
# stu1 = student()
# stu1.register('saikumar',24)
# stu1.get_student_details()
# stu1.exam_eligibility()
# stu1.exam_eligibility()


   # or

import  random
class Student():
    stu_id = 1000
    def register(self):
        self.name = input("Enter student Name : ")
        self.age = int(input("Enter student Age : "))
        Student.stu_id +=1
        self.reg_no = Student.stu_id
        self.college = 'Srm university'
        self.attendence = 0

    def get_student_details(self):
        self.status = self.exam_eligibility()
        print("sudent details are : \n name : {}\n  age : {} \n Rollno : {}\n College: {} \n Attendence : {}\n"
              .format(self.name, self.age, self.reg_no, self.college,self.attendence))

    def attend_class(self):
         self.attendence = random.randint(30,80)


    def exam_eligibility(self):
        if self.attendence == 0:
            print("New student")
        elif self.attendence >= 40:
            print("Eligible for exam")
        else:
            print('Not Eligible for exam')

     def update_attendence(self,newattend):
         
         if newattend < 50:
             self.attendence = 50
         else:
             self.attendence = newattend

obj = Student()
obj.register()
obj.get_student_details()
obj.exam_eligibility()
obj.attend_class()
obj.update_attendence(50)









