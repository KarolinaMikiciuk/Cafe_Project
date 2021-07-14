
print("MAIN MENU OPTIONS: 1. Shop   2. Exit   3. Couriers ")
open_menu = input(print("For Shop press 1, for Exit press 0, for Couriers press 2 "))   

def show_entries(category):
    with open(f"{category}_list.txt","r") as my_list:
        lines = my_list.readlines() #list of lines
        i = 0
        for i in range(len(lines)):  
            indice = str(i)
            line = lines[i]
            line= line.strip()
            print(line, indice) # prints each line
            i += 1
        return lines
                
def add_to_list(category,new_entry):
    with open(f"{category}_list.txt","a+") as my_list:
            my_list.write(new_entry)
            lines = my_list.readlines()
            print("the new list is: ")
            for line in lines:
                line = line.strip()
                print(line)
                
def update_name(category,index,name):
    lines = show_entries(category)
    lines[index] = name #updates name
    with open(f"{category}_list.txt","w") as my_list:
        my_list.writelines(lines) #list of lines    
        contents = my_list.readlines()
        print("the new list is: ")
        print(contents)
        
def delete_entry(category,index):
    lines = show_entries(category)
    lines.remove(index) #updates name
    with open(f"{category}_list.txt","w") as my_list:
        my_list.writelines(lines) #list of lines    
        contents = my_list.readlines()
        print("the new list is: ")
        print(contents)
        
#-----------------------------------------------------------------------------------------------------------------------------------

if open_menu == "0":
    print("you are about to exit")
    result = input(print("type anything to exit"))  

elif open_menu == "1":            #NEED TO ADD OPTION 0 (return to main menu)
    option_chosen= input(print("to exit press 0, to see  products press 1, to add a new product press 2, to update product name press 3, to delete product press 4"))
    
    if option_chosen == "1":
        show_entries("food") 
        exit = input(print("type anything to exit"))
        
    elif option_chosen == "0":            
        print("you are about to exit")
        result = input(print("type anything to exit"))

    elif option_chosen == "2":                             #adds a new product
        new_product = input(print("Add a new product name:"))
        add_to_list("food",new_product)
        print("you are about to exit")
        result = input(print("type anything to exit"))
        
    elif option_chosen == "3": #print product names with index values
        show_entries("food")
        index = input(print("enter the number of the product you want to update the name of"))
        name = input(print("what name do you want to update it to"))
        update_name("food",index,name)
        print("you are about to exit")
        result = input(print("type anything to exit"))
        
    elif option_chosen == "4":
        show_entries("food")
        index = input(print("enter the index of the product you want to delete"))
        delete_entry("food",index)
        print("you are about to exit")
        result = input(print("type anything to exit"))
                    
    else:                                                 
        print("invalid input, press either 1 or 0")
        
elif open_menu == "3":
    option_chosen= input(print("to exit press 0, to see couriers press 1, to add a new courier press 2, to update courier name press 3, to delete a courier press 4"))  

    if option_chosen == "1":
        show_entries("courier") 
        print("you are about to exit")
        result = input(print("type anything to exit"))       
        
    elif option_chosen == "0":            
        print("you are about to exit")
        result = input(print("type anything to exit"))
    
    elif option_chosen == "2":                             #adds a new product
        new_courier = input(print("Add a new courier name:"))
        check_list = list(new_courier) 
        while new_courier == "" :
            print("This is not a valid name")
            new_courier = input(print("Add a new courier name:"))   
        check_against = [ '1','2','3','4','5','6','7','8','9','0']
        for item in check_against:
            while item in check_list:
                print("This is not a valid name")
                new_courier = input(print("Add a new courier name:"))
            break
        add_to_list("courier",new_courier)
            
        print("you are about to exit")
        result = input(print("type anything to exit"))
    
    elif option_chosen == "3": #print couriers names with index values
        show_entries("courier")
        index = input(print("enter the index of the courier you want to update the name of"))
        name = input(print("what name do you want to update it to"))
        update_name("courier",index,name)
        print("you are about to exit")
        result = input(print("type anything to exit"))

else:
    print("please type in valid input")
    


