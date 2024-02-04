class company:
    company = 'HCL'
    location = 'Chengalpattu'

    def __init__ (self,name,age,phno):
        self.name = name
        self.age = age
        self.phno = phno
        print('obj is created')

    def emp_details(self):
        print(f'Emp_name : {self.name}')
        print(f'emp_age : {self.age}')
        print(f'emp_phno : {self.phno}')

    def change_age(self,new_age):
        self.age = new_age


'''
output:

e1=company('ram',32,8870900909)
obj is created
e1.name
'ram'

e2=company('purushoth',21,34879873)
obj is created

e3=company('moni',20,39480950)
obj is created

e3.emp_details
<bound method company.emp_details of <__main__.company object at 0x000002BA056F2E10>>

e3.emp_details()
Emp_name : moni
emp_age : 20
emp_phno : 39480950

e1.emp_details()
Emp_name : ram
emp_age : 32
emp_phno : 8870900909

e1.change_age(12)

e1.age
12

e1.emp_details()
Emp_name : ram
emp_age : 12
emp_phno : 8870900909


e2.emp_details()
Emp_name : purushoth
emp_age : 21
emp_phno : 34879873

company.change_age(e2,11)

e2.emp_details()
Emp_name : purushoth
emp_age : 11
emp_phno : 34879873


company.emp_details(e1)
Emp_name : ram
emp_age : 32
emp_phno : 8870900909
'''
