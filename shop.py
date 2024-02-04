"""items = {'mobiles':[10,40000],'smart_watch':[10,10000],'tabs':[10,25000]}
#heading
print('product',end='     ')
print('quantity',end='     ')
print('sub total')

#mobiles
print('mobiles',end='     ')
print(items['mobiles'][0],end='     ')
print(items['mobiles'][-1])

#smart_watch
print('smart_watch',end='     ')
print(items['smart_watch'][0],end='     ')
print(items['smart_watch'][-1])

#tabs
print('tabs',end='     ')
print(items['tabs'][0],end='     ')
print(items['tabs'][-1])

items = {'mobiles': [10, 40000], 'smart_watch': [10, 10000], 'tabs': [10, 25000]}

print('product', end='     ')
print('quantity', end='     ')
print('sub total')

for i, j in items.items():
    print(i, end='     ')
    print(j[0], end='     ')
    print(j[-1])
"""
prod_items = {'mobiles':[10,40000],'smart_watch':[20,10000],'tabs':[15,25000]}

#customer's cart
        print('product', end='          ')
        print('quantity', end='          ')
        print('sub total')

        total=0
        cust_cart={}
        for i, j in self.cart.items(): #i - product, j - quantity
            print(i, end='               ')
            print(j, end='               ')
            sub_total = j*shopping_cart.prod_items[i][-1]
            print(sub_total)
            total+=sub_total
            cust_cart[i]=[j]
        print(f'                    Total            {total}')
