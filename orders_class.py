import csv

class Order(object):
    def __init__(self,order_id,customer_name,customer_address,customer_phone_num,courier_id,stage,items):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_phone_num = customer_phone_num
        self.courier_num = courier_id
        self.stage = stage
        self.items = items
        self.order_id = order_id

    def form_a_dict(self):
            
        new_order = {
                    "orders_id" : self._order_id,
                    "customer_name" : self._customer_name,
                    "customer_address" : self._customer_address.replace(',','.'),
                    "customer_phone" : self._customer_phone_num,
                    "couriers_id" : self._courier_num,
                    "orders_stage" : self._stage,
            }
        return new_order
    
    @property                         #ORDER ID
    def order_id(self):
        return self._order_id
    
    @order_id.setter                       #UPDATE ORDER ID 
    def order_id(self, order_id):               
        self._order_id = order_id

    @property                         #CUSTOMER NAME
    def customer_name(self):
        return self._customer_name

    @customer_name.setter                        #UPDATE CUSTOMER NAME
    def customer_name(self,customer_name):
        self._customer_name = customer_name
    
    @property                           #CUSTOMER PHONE NUM
    def customer_phone_num(self):
        return self._customer_phone_num
            
    @customer_phone_num.setter                           #VALIDATE AND UPDATE PHONE NUM
    def customer_phone_num(self, customer_phone_num):
        test_length = str(customer_phone_num)
        if len(test_length) == 10:
            self._customer_phone_num = str(customer_phone_num)
        else:
            raise Exception("Phone number must be 10 digits long ")
    
    @property                    # COURIER ID
    def courier_num(self):
        return self._courier_num

    @courier_num.setter                       #UPDATE COURIER ID 
    def courier_num(self, courier_id):               
        with open("couriers_list.csv","r") as file:
            file_column_reader = csv.reader(file, delimiter = ",") #returns list
            if courier_id in file_column_reader:
                self._courier_num = courier_id
            else:
                raise Exception ("No such courier id is found in the courier list")
    
    @property
    def stage(self):
        return self._stage
    
    @stage.setter
    def stage(self,stage):
        if stage == "preparing" or stage == "delivering" or stage == "delivered" :
            self._stage = stage
        else:
            raise Exception ("Stage must be one of the following: preparing/delivering/delivered")
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self,items):
        if type(items) == list and len(items) != 0:
            self._items = items
        else:
            raise Exception ("Items must be a list of length > 0")
        
    @property 
    def customer_address(self):
        return self._customer_address 
        
    @customer_address.setter
    def customer_address(self,customer_address):
        test_postcode = customer_address[0]
        
        if (
            type(customer_address) == list and 
            len(test_postcode) == 6 and
            len(customer_address) == 3 and  #PEP8 guidelines to improve readability
            type(customer_address[0]) == str and
            type(customer_address[1]) == str and
            (type(customer_address[2]) == int or customer_address[2] == "N") and
            test_postcode[0].isdigit() == False  and
            test_postcode[1].isdigit() == True  and
            test_postcode[2].isdigit() == True  and
            test_postcode[3].isdigit() == True  and
            test_postcode[4].isdigit() == False  and        #["C352KD","sunflower road",2]
            test_postcode[5].isdigit() == False
            
            ):
            self._customer_address = customer_address
        else:
            raise Exception("Incorrect address format, please enter appropriate input, e.g. ['C352KD','sunflower road',2] ")
        
