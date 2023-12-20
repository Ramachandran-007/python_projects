class shopping_cart:
    shop_name = 'Online_Officials'
    location = 'Chennai'
    prod_items = {'mobiles':[10,40000],'smart_watch':[20,10000],'tabs':[15,25000]}

    def __init__(self,name,ph_no,address):
        self.name = name
        self.ph_no = ph_no
        self.address = address
        self.cart = {}

    #to display the products in the shop
    @classmethod
    def items_disp(cls):
        
        print('product', end='          ')
        print('quantity', end='          ')
        print('price')

        for i, j in cls.prod_items.items():
            print(i, end='          ')
            print(j[0], end='          ')
            print(j[-1])

    #to display the customer details
    def customer_details(self):
        print(f'Name : {self.name}')
        print(f'Phone no : {self.ph_no}')
        print(f'Address : {self.address}')
        print(f'Cart : {self.cart}\n')

        if cus.cart != {}:
            print('product', end='     ')
            print('quantity', end='     ')
            print('sub total')

            total=0
            for i in cus.cart:
                print(i, end='          ')
                print(cus.cart[i], end='          ')
                sub_total = cus.cart[i]*shopping_cart.prod_items[i][-1]
                total+=sub_total
                print(sub_total)
            print(f'          Total     {total}')
        else:
            print('Your cart is empty ! ')
        
cus=shopping_cart('Ram',1234567890,'Chengalpattu')

while True:
    print('1. Press 1 to dispaly available products')
    print('2. Press 2 to display customer details')
    print('3. Press 3 to add a product to your cart')
    print('4. Press 4 to remove the product from your cart')
    print('5. Press 5 to exit \n')
    
    key=int(input('Press the key : '))
    print()
    
    if key == 5:
        True
        print('Thanks for shopping')
        break
    elif key == 1:
        shopping_cart.items_disp()
        print()
        print('*****************************************************************\n')
        
    elif key==2:
        cus.customer_details()
        print()
        print('******************************************************************\n')
        
    elif key==3:
        prod = input('Enter the product name : ')
        print()
        if prod in shopping_cart.prod_items.keys():
            prod_quan=int(input(f'How many {prod} ? : '))
            print()
            if prod_quan  <= shopping_cart.prod_items[prod][0]:
                cus.cart[prod] = prod_quan
                shopping_cart.prod_items[prod][0] -= prod_quan
                print('Product added to the cart successfully!\n')
                print('******************************************************************\n')
            else:
                print(f'Only {shopping_cart.prod_items[prod][0]} is left! \n')
                print('******************************************************************\n')
        else:
            print('This product is not available \n')
            print('******************************************************************\n')

    elif key==4:
        if cus.cart != {}:
            prod = input('What product you want to remove? : ')
            print()
            if prod in cus.cart.keys():
                quant = int(input('How many quantity you want to remove? : '))
                print()
                if quant <= cus.cart[prod]:
                    item = cus.cart[prod]
                    cus.cart[prod] = item - quant
                    shopping_cart.prod_items[prod][0] += quant
                    print('Product removed successfully! \n')
                    print('******************************************************************\n')
                else:
                    print(f'only {cus.cart[prod]} is available in your cart \n')
                    print('******************************************************************\n')
            else:
                print('This item is not available in your cart \n')
                print('******************************************************************\n')
        else:
            print('Your cart is empty')
            print('******************************************************************\n')

