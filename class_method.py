class mobile:
    brand = 'ASUS'
    os_type = 'Android'
    location = 'Chennai'

    def __init__ (self,model,specification,color,amount):
        self.model = model
        self.specification = specification
        self.color = color
        self.amount = amount

    @classmethod
    def mod_location (cls,new_location):
        cls.location = new_location

    @classmethod
    def main_details(cls):
        print(cls.brand)
        print(cls.os_type)
        print(cls.location)

    def sub_details(self):
        print(self.model)
        print(self.specification)
        print(self.color)
        print(self.amount)


        
        
m1=mobile('a1','8/120','red',12000)
m2=mobile('a2','16/256','blue',20000)
m3=mobile('a3','18/234','pink',30000)
m4=mobile('a4','24/1tb','golden brown',50000)
