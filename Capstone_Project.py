

mini_shopee_data = {
    'id' : ['102','21','173','544','755','77','99'],
    'product' : ['Sprite','Fanta','Toblerone','Chitato','Handphone','Sofa','TV'],
    'stock' : [22,25,27,30,2,3,1],
    'price' : [7500,8000,20000,3200,7850000,2500000,5000000],
    'rating' : [0,0,0,0,0,0,0],
    'sold' : [0,0,0,0,0,0,0],
    'weight' : [0.25,0.25,0.1,0.05,0.8,10.0,5.0],
    'sales' : [0,0,0,0,0,0,0]
}

cart = {}

average = {}

purchased = []


main_menu = '''
==============================================
>>>>>>>>>>  Data Centre  <<<<<<<<<<

        1.  Informations Center
        2.  Add New Product
        3.  Update Product Informations
        4.  Delete Product
        5.  Back To Admin or Customer Menu
==============================================
'''

menu_info = '''
==============================================
>>>>>>>>>>  Informations Center  <<<<<<<<<<

        1.  All Products Informations
        2.  Specific Product Informations
        3.  Products Performance Graph
        4.  Sales Summary
        5.  Back To Main Menu
==============================================
'''

menu_new = '''
==============================================
>>>>>>>>>>  Add New Product  <<<<<<<<<<

        1.  Add New Data
        2.  Back To Main Menu
==============================================
'''

menu_update = '''
==============================================
>>>>>>>>>>  Update Product Informations  <<<<<<<<<<

        1.  Update Existing Data
        2.  Back To Main Menu
==============================================
'''

menu_delete = '''
==============================================
>>>>>>>>>>  Delete Data  <<<<<<<<<<

        1.  Delete Existing Data
        2.  Back To Main Menu
==============================================
'''

menu_cust = '''
==============================================
>>>>>>>>>>  Welcome to Mini Shopee  <<<<<<<<<<

        1.  Purchase Now!
        2.  Rate Product
        3.  Back To Admin or Customer Menu
==============================================
'''

no_data = '\n!!! Data does not exist !!!'
no_option = '(The Option You Entered Is Not Valid.Please Try Again.)'
select = 'Select Option:'

def yes_no(word):
    print(f'\n>>>>>>>>>> {word} <<<<<<<<<<\n1.Yes\n2.No')
    user_input = input(select)
    while user_input not in ['1','2']:
        print(no_option)
        print(f'\n>>>>>>>>>> {word} <<<<<<<<<<\n1.Yes\n2.No')
        user_input = input(select)
    return user_input

def casting_function(col,user_input):
    if col in ['stock','price','sold','sales']:
        while not user_input.isdigit():
            print('!!! Invalid Input !!!')
            user_input = input('Enter Valid Input :')
        user_input = int(user_input)
    elif col in ['rating','weight']:
        user_input = user_input.replace(',','.')
        while not user_input.replace('.','').isdigit():
            print('!!! Invalid Input !!!')
            user_input = input('Enter Valid Input :')
        user_input = float(user_input)
    return user_input

def show_id_list(data):
    for i in range(len(data['id'])):
        list_id = ''
        if (i%2==0) and (i!=0):
            list_id = '\n{} : {}'.format(data['id'][i],data['product'][i])
            while len(list_id)<40:
                list_id += ' '
        else:
            list_id = '{} : {}'.format(data['id'][i],data['product'][i])
            while len(list_id)<40:
                list_id += ' '
        print(list_id,end='')

def back_to_access():
    print('\n0 . Back')
    user_input = input(select)
    while user_input != '0':
        print(no_option)
        print('\n0 . Back')
        user_input = input(select)
    else:
        return access_data()

def table_maker(data,col_size,all_or_spec):
    table_1 = ''
    table_2 = ''
    table_size = []
    for n,d in enumerate(data):
        table_1 += '+--'+'-'*col_size[n]
        table_size.append(len(table_1))
        table_2 += f'|{d}'
        while len(table_2)<len(table_1):
            table_2 += ' '
        if n == len(data)-1 :
            table_1 += '+'
            table_2 += '|'
    print(table_1,table_2,table_1,sep='\n')
    data_index = [mini_shopee_data['id'].index(x) for x in mini_shopee_data['id'] if x in all_or_spec]
    for i in data_index:
        table_3 = ''
        for n,d in enumerate(data):
            table_3 += '|{}'.format(mini_shopee_data[d][i])
            while len(table_3)<table_size[n]:
                table_3 += ' '
            if n == len(data)-1 :
                table_3 += '|'
        print(table_3)
    print(table_1)
    return
            



def all_data(data):
    if len(data['id']) > 0:
        data_to_show = list(data)
        col_size = []
        for d in data_to_show:
            max_len = max([len(str(x)) for x in data[d]])
            col_size.append(max([len(d),max_len]))
        table_maker(data_to_show,col_size,data['id'])
        back_to_access() 
    else:
        print(no_data)
        return access_data() 
    
def specific_data(data):
    if len(data['id']) > 0:
        data_to_show = list(data)
        col_size = []
        for d in data_to_show:
            max_len = max([len(str(x)) for x in data[d]])
            col_size.append(max([len(d),max_len]))
        show_id_list(data)
        user_input = input('\nEnter Product id :')
        if user_input in data['id']:
            table_maker(data_to_show,col_size,[user_input])
            back_to_access()
        else:
            print(no_data)
            return access_data() 
    else:
        print(no_data)
        return access_data()
        
def performance_graph(data):
    if len(data['id'])>0:
        print('>>>>>>>>>>Products Sold<<<<<<<<<<')
        for i in range(len(data['id'])):
            print('|{}'.format('___'*data['sold'][i]),sep='')
            print('|{}|{}'.format('___'*data['sold'][i],data['product'][i]))
            if i == (len(data['id'])-1):
                print('|{}'.format('===='*max(data['sold'])))
                for n in range(0,max(data['sold']),2):
                    if n==0:
                        print(' ',end='')
                        print('{}'.format(n),end='')
                    else:
                        print('{}{}'.format(' '*5,n),end='')
        back_to_access()
    else:
        print(no_data)
        return access_data()
    
def sales_summary(data):
    if len(data['id']) > 0:
        print('>>>>>>>>>> Sales Summary <<<<<<<<<<')
        data_to_show = [key for key in data if key not in ['stock','rating','weight']]
        col_size = []
        for d in data_to_show:
            max_len = max([len(str(x)) for x in data[d]])
            col_size.append(max([len(d),max_len]))
        table_maker(data_to_show,col_size,data['id'])
        print('Total Sales : {}'.format(sum(data['sales'])))
        back_to_access()
    else:
        print(no_data)
        return access_data()
       
def access_data():
    print(menu_info)
    user_input=input(select)
    while user_input != '5':
        if user_input not in functions['access_func'].keys(): 
            print(menu_info)
            print(no_option)
            user_input = input(select)
        else:
            return functions['access_func'][user_input](mini_shopee_data)
    else:
        return
    
def add_new_data():
    print(menu_new)
    user_input = input(select)
    while user_input not in ['1','2']:
        print(menu_new)
        print(no_option)
        user_input = input(select)
    if user_input == '1':
        show_id_list(mini_shopee_data)
        user_input_id = input('\nEnter Product Id :')
        if user_input_id in mini_shopee_data['id']:
            print('\n!!!Data Already Exists!!!')
            return add_new_data()
        else:
            user_input_product = input('Enter Product Name :')
            user_input_stock = input('Enter Product Stock :')
            user_input_stock = casting_function('stock',user_input_stock)
            user_input_price = input('Enter Product Price :')
            user_input_price = casting_function('price',user_input_price)
            user_input_weight = input('Enter Product Weight in "Kg":')
            user_input_weight = casting_function('weight',user_input_weight)
            user_input_save = yes_no('Save Data?')
            if user_input_save == '1':
                list_input = [user_input_id,user_input_product,user_input_stock,user_input_price,user_input_weight]
                for n,key in enumerate(['id','product','stock','price','weight']):
                    mini_shopee_data[key].append(list_input[n])
                for key in ['rating','sold','sales']:
                    mini_shopee_data[key].append(0)
                print('\nData Successfully Saved')
                return add_new_data()
            else:
                return add_new_data()
    else:
        return

def update_data(data=mini_shopee_data):
    if len(data['id']) > 0:
        data_to_show = list(data)
        col_size = []
        for d in data_to_show:
            max_len = max([len(str(x)) for x in data[d]])
            col_size.append(max([len(d),max_len]))
    else:
        print('You Do Not Have Any Data To Update')
        return
    print(menu_update)
    user_input = input(select)
    while user_input not in ['1','2']:
        print(no_option)
        print(menu_update)
        user_input = input(select)
    if user_input == '1':
        show_id_list(data)
        user_input_id = input('\nEnter Product Id :')
        if user_input_id in data['id']:
            table_maker(data_to_show,col_size,[user_input_id])
            user_input_cont = yes_no('Continue Update?')
            if user_input_cont == '1':
                user_input_col = input('Enter Column Name To Change :').casefold()
                while user_input_col not in data.keys():
                    print('Column Not Found')
                    user_input_col = input('Enter Column Name To Change :').casefold()
                change_value = input('Enter Value For "{}" Column :'.format(user_input_col))
                change_value = casting_function(user_input_col,change_value)
                user_input_update = yes_no('Update Data?')
                if user_input_update == '1':
                    id_index = data['id'].index(user_input_id)
                    data[user_input_col][id_index] = change_value
                    print('Data Successfully Updated')
            return update_data()
        else:
            print('The Data You Are Looking For Does Not Exist')
            return update_data()

def delete_data(data = mini_shopee_data):
    if len(data['id']) > 0:
        data_to_show = list(data)
        col_size = []
        for d in data_to_show:
            max_len = max([len(str(x)) for x in data[d]])
            col_size.append(max([len(d),max_len]))
    else:
        print('You Do Not Have Any Data To Delete')
        return
    print(menu_delete)
    user_input = input(select)
    while user_input not in ['1','2']:
        print(no_option)
        print(menu_delete)
        user_input = input(select)
    if user_input == '1':
        table_maker(data_to_show,col_size,data['id'])
        user_input_id = input('\nPlease Enter Product Id :')
        if user_input_id in data['id']:
            item_index = data['id'].index(user_input_id)
            y_n = yes_no('Delete Data?')
            if y_n == '1':
                for key in data.keys():
                    del data[key][item_index]
                print('\nData Successfully Deleted')
                return delete_data()
            else:
                return delete_data()
        else:
            print(no_data)
            return delete_data()
    else:
        return

def add_cart(data,data_to_show,col_size):
    table_maker(data_to_show,col_size,data['id'])
    user_input_id = input('Please Enter Product Id :')
    if user_input_id not in data['id']:
        print('Item Not Found.')
        return
    item_index = data['id'].index(user_input_id)
    if user_input_id in cart.keys():
        available = data['stock'][item_index]-cart[user_input_id]
        user_input_stock = input('Quantity (Available:{}) :'.format(available))
        user_input_stock = casting_function('stock',user_input_stock)
        total_item = cart[user_input_id] + user_input_stock
        while total_item > data['stock'][item_index]:
            available = data['stock'][item_index]-cart[user_input_id]
            user_input_stock = input('Not Enough Stocks (Available:{})\nQuantity :'.format(available))
            user_input_stock = casting_function('stock',user_input_stock)
            total_item = cart[user_input_id] + user_input_stock
        cart[user_input_id] += user_input_stock
        print('Items Added To Your Cart.')
        return
    else:
        user_input_stock = input('Quantity (Available:{}) :'.format(data['stock'][item_index]))
        user_input_stock = casting_function('stock',user_input_stock)
        while user_input_stock > data['stock'][item_index]:
            user_input_stock = input('Not Enough Stocks (Available:{})\nQuantity :'.format(data['stock'][item_index]))
            user_input_stock = casting_function('stock',user_input_stock)
        cart[user_input_id] = user_input_stock
        print('Items Added To Your Cart.')
        return
    
def view_cart(data,data_to_show=[],col_size=[]):
    print('\n>>>>>>>>>> Your Cart <<<<<<<<<<')
    total_all = 0
    if len(cart)>0:
        for i, key in enumerate(cart.keys(),1):
            item_index = data['id'].index(key)
            name = data['product'][item_index]
            price = data['price'][item_index]
            total = cart[key] * price
            total_all += total
            print('{}.\t{} : {} x Rp. {} = Rp. {}'.format(i,name,cart[key],price,total))
        print(f'Total = Rp. {total_all}\n')
    else:
        print('No Item In Your Cart.\n')
        return
    print('0. Back\n1. Remove Item')
    user_input = input(select)
    while user_input not in ['0','1']:
        print(no_option)
        print('0. Back\n1. Remove Item')
        user_input = input(select)
    if user_input == '0':
        return
    else:
        for key in cart.keys():
            item_index = data['id'].index(key)
            print('{} : {} <Quantity:{}>'.format(key,data['product'][item_index],cart[key] ))
        input_remove = input('Enter Product Id You Want To Remove :')
        while input_remove not in cart.keys():
            print('{} : {} <Quantity:{}>'.format(key,data['product'][item_index],cart[key] ))
            print('No Such Item In Your Cart')
            input_remove = input('Enter Product Id You Want To Remove :')
        input_remove_quant = input('Enter Quantity :')
        input_remove_quant = casting_function('stock',input_remove_quant)
        if input_remove_quant >= cart[input_remove]:
            del cart[input_remove]
            return view_cart(mini_shopee_data)
        else:
            cart[input_remove] -= input_remove_quant
            return view_cart(mini_shopee_data)

def check_out(data,data_to_show,col_size):
    print('>>>>>>>>>> Payment Details <<<<<<<<<<')
    total_all = 0
    total_weight = 0
    shipping_fee = 5000
    if len(cart)>0:
        for i, key in enumerate(cart.keys(),1):
            item_index = data['id'].index(key)
            name = data['product'][item_index]
            price = data['price'][item_index]
            total = cart[key] * price
            weight = data['weight'][item_index]
            total_all += total
            total_weight += weight
            print('{}.\t{} : {} x Rp. {} = Rp. {}'.format(i,name,cart[key],price,total))
        total_shipping = total_weight*shipping_fee
        print(f'\nTotal = Rp. {total_all}\nShipment Fee = Rp. {total_shipping}\nTotal Payment = Rp. {total_all+total_shipping}')
        user_input = yes_no('Pay?')
        if user_input == '1':
            print('Payment Done!')
            for i, key in enumerate(cart.keys()):
                item_index = data['id'].index(key)
                data['sold'][item_index] += cart[key]
                data['stock'][item_index] -= cart[key]
                data['sales'][item_index] = data['sold'][item_index] * data['price'][item_index]
                purchased.append(key)
            cart.clear()
        else:
            return
    else:
        print('No Item Yet.\n')
        return

def purchase_now(data=mini_shopee_data):
    data_to_show = [key for key in data.keys() if key not in ['stock','sales','weight']]
    col_size = []
    for d in data_to_show:
        max_len = max([len(str(x)) for x in data[d]])
        col_size.append(max([len(d),max_len]))
    user_input = 0
    while user_input != '4':
        table_maker(data_to_show,col_size,data['id'])
        print('1.Add to Cart\n2.View Cart\n3.Check Out\n4.Back')
        user_input = input(select)
        if user_input in functions['purchase_func'].keys():
            functions['purchase_func'][user_input](data,data_to_show,col_size)
    else:
        return
    
def rate_product(data=mini_shopee_data):
    if len(purchased) > 0:
        data_to_show = list(data)[:2]
        col_size = []
        for d in data_to_show:
            max_len = max([len(str(x)) for x in data[d]])
            col_size.append(max([len(d),max_len]))
    else:
        print('You Have Not Purchase Any Item')
        return
    user_input = yes_no('Rate Now?')
    if user_input == '1':
        table_maker(data_to_show,col_size,purchased)
        user_input_id = input('Please Enter Product Id :')
        while user_input_id not in purchased:
            table_maker(data_to_show,col_size,purchased)
            print('You Can Only Rate Purchased Items.')
            user_input_id = input('Please Enter Product Id :')
        item_index = data['id'].index(user_input_id)
        user_rate = input('How Do You Like Our Product?(0-5)')
        user_rate = casting_function('rating',user_rate)
        while user_rate > 5 :
            print('You Can Only Rate Between 0 to 5')
            user_rate = input('How Do You Like Our Product?(0-5)')
            user_rate = casting_function('rating',user_rate)
        data['rating'][item_index] += user_rate
        if user_input_id not in average.keys():
            average[user_input_id] = 1
        else:
            average[user_input_id] = 2
        data['rating'][item_index] /= average[user_input_id]
        purchased.remove(user_input_id)
        print('You Have Successfully Rated This Product!')
        return rate_product()
    elif user_input == '2':
        return
    else:
        print(no_option)
        return rate_product()




functions = {
    'main_func' : {'1':access_data,'2':add_new_data,'3':update_data,'4':delete_data},
    'access_func' : {'1':all_data,'2':specific_data,'3':performance_graph,'4':sales_summary},
    'cust_func' : {'1':purchase_now,'2':rate_product},
    'purchase_func' : {'1':add_cart,'2':view_cart,'3':check_out}
}

def main_menu_admin(functions=functions):
    user_input = 0
    while  user_input != '5':
        print(main_menu)  
        user_input = input(select)
        if user_input in functions['main_func'].keys():
            functions['main_func'][user_input]()
        elif user_input != '5':
            print(no_option)
    return admin_or_cust()


def main_menu_cust(functions=functions):
    user_input = 0
    while  user_input != '3':
        print(menu_cust)  
        user_input = input(select)
        if user_input in functions['cust_func'].keys():
            functions['cust_func'][user_input]()
        elif user_input != '3':
            print(no_option)
    return admin_or_cust()

def admin_or_cust():
    print('\nLog In As?\n1.Admin\n2.Customer\n3.Exit Program')
    user_input = input(select)
    while user_input not in ['1','2','3']:
        print(no_option)
        print('\nLog In As?\n1.Admin\n2.Customer\n3.Exit Program')
        user_input = input(select)
    if user_input == '1':
        return main_menu_admin()
    elif user_input == '2':
        if len(mini_shopee_data['id']) > 0:
            return main_menu_cust()
        else:
            print('No Item Available to Purchase Yet.')
            return admin_or_cust()
    else:
        print('Closing Program.')
        return

    
admin_or_cust()
