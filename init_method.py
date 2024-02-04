class company:
    company_name = 'HCL'
    location = 'Chennai'

    def __init__ (self,name,id,phno):
        self.name = name
        self.id = id
        self.phno = phno

e1 = company('Ram',1001,89087098)
e2 = company('Purushoth',1002,989788787)

print(e1.id)
print(e2.phno)
