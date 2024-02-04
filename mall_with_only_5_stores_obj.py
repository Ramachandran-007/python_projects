class Mall:
    Location = 'Chennai'
    Name = 'Ha - Ha'
    Timing = '9.00 am to 10.00 pm'
    obj_count = 0

    def __init__(self,Shop_name,Shop_no,Shop_type):
        Mall.obj_count+=1
        if Mall.obj_count > 5:
            print('More than 5 obj is not allowed')
            return
        self.Shop_name = Shop_name
        self.Shop_no = Shop_no
        self.Shop_type = Shop_type

    @classmethod
    def mall_details(cls):
        print(cls.Location)
        print(cls.Name)
        print(cls.Timing)

    def display(self):
        Mall.mall_details()
        print(self.Shop_name)
        print(self.Shop_no)
        print(self.Shop_type)


shop1 = Mall('Jockey',1,'Clothings')
shop2 = Mall('Dominos',2,'Pizza')
shop3 = Mall('KFC',3,'Chicken')
shop4 = Mall('Jockey',1,'Clothings')
shop5 = Mall('Dominos',2,'Pizza')
#shop6 = Mall('KFC',3,'Chicken')       
        
        
        
