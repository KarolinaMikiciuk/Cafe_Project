from products_class import Product
from couriers_class import Courier
from orders_class import Order
from crud import add_to_file, update_file_value, show_file_contents, delete_entry
from commit_to_db import commit_to_db
import ast

def main():
    
    action_string = "What is the action you want to perform? \nshow entries: s \nupdate entry: u \ndelete entry: d \nadd entry: a \nexit: e "


    is_running_app = True
    while is_running_app == True:
        cat = input("What is the category? \nproducts : p \ncouriers : c \norders : o \nexit : e  ")
        if cat == 'p':  
            is_viewing_p = True
            while is_viewing_p ==True:
                act = input(action_string)
                
                if act == "a":
                    print("Please type the price, name and id of the product")
                    price = float(input("Price: "))
                    name = input("Name: ")
                    id = int(input("Id: "))
                    new_product = Product(price,name,id)
                    product_dict = new_product.form_a_dict()
                    add_to_file("products",product_dict)
                    commit_to_db("products")
                    
                if act == "s":
                    show_file_contents("products")

                if act == "u":
                    column_name = input("Enter column name ")
                    entry_id = int(input("Enter entry id "))
                    change_entry_to = input("What do you want to change the entry to? ")
                    update_file_value("products",column_name,entry_id,change_entry_to)
                    commit_to_db("products")

                if act == "d":
                    product_id = int(input("Please type the product id the entry you want to delete "))
                    delete_entry("products",product_id)
                    commit_to_db("products")
                    
                if act == 'e':
                    is_viewing_p = False

        if cat == 'c':  
            is_viewing_c = True
            while is_viewing_c ==True:
                act = input(action_string)
                
                if act == "a":
                    print("Please type the id, name and phone number of the courier")
                    id = int(input("Id: "))
                    name = input("Name: ")
                    phone = input("Phone: ")
                    new_courier = Courier(id,name,phone)
                    courier_dict = new_courier.form_a_dict()
                    add_to_file("couriers",courier_dict)
                    commit_to_db("couriers")
                    
                if act == "s":
                    show_file_contents("couriers")

                if act == "u":
                    column_name = input("Enter column name ")
                    entry_id = int(input("Enter entry id "))
                    change_entry_to = input("What do you want to change the entry to? ")
                    update_file_value("couriers",column_name,entry_id,change_entry_to)
                    commit_to_db("couriers")

                if act == "d":
                    courier_id = int(input("Please type the courier id of the courier you want to delete "))
                    delete_entry("couriers",courier_id)
                    commit_to_db("couriers")
                    
                if act == 'e':
                    is_viewing_c = False

        if cat == 'o':  
            is_viewing_o = True
            while is_viewing_o ==True:
                act = input(action_string)
                #orders_id,customer_name,customer_address,customer_phone,couriers_id,orders_stage

                if act == "a":
                    print("Please type the order id, name, address and phone number of the customer, courier id, order stage as well as a list of items")
                    order_id = int(input("Order id: "))
                    customer_name = input("Customer name: ")
                    customer_address = ast.literal_eval(input("Customer address: "))
                    customer_phone = input("Customer phone: ")
                    couriers_id = int(input("Courier id: "))
                    stage = input("Order stage: ")
                    items = ast.literal_eval(input("Items: "))
                    new_order = Order(order_id,customer_name,customer_address,customer_phone,couriers_id,stage,items)
                    order_dict = new_order.form_a_dict()
                    add_to_file("orders",order_dict)
                    commit_to_db("orders")
                    add_to_file("orders", items)
                    commit_to_db("items")
                    
                if act == "s":
                    show_file_contents("orders")

                if act == "u":
                    items_or_order = input("Do you want to update items or order? i/o ")
                    column_name = input("Enter column name ")
                    entry_id = int(input("Enter entry id "))
                    change_entry_to = input("What do you want to change the entry to? ")
                    
                    if items_or_order == "o":
                        update_file_value("orders",column_name,entry_id,change_entry_to)
                        commit_to_db("orders")
                        
                    if items_or_order == "i":
                        update_file_value("items",column_name,entry_id,change_entry_to)
                        commit_to_db("items")
                    else:
                        print("Invalid input, type i or o ")
                        
                if act == "d":
                    items_or_order = input("Do you want to delete items or order? i/o ")
                    
                    if items_or_order == "o":
                        orders_id = int(input("Please type the order id of the order you want to delete "))
                        delete_entry("orders",orders_id)
                        commit_to_db("orders")
                        
                    if items_or_order == "i":
                        product_name = input("Please type the product name of the order you want to delete ")
                        delete_entry("items",product_name)
                        commit_to_db("items")
                        
                    else:
                        print("Invalid input, type i or o ")
                    

                if act == 'e':
                    is_viewing_o = False
                    
                else:
                    print("Invalid input, type u, s, d, a or e ")


        if cat == 'e':
            is_running_app = False
            
        else: 
            print("Invalid input, type u, s, d, a or e ")
        
if __name__=="__main__":
    main()
