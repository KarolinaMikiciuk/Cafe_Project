import csv  #explain why you are using csv dependency instead of just using pandas again

class Courier(object):
    def __init__(self,couriers_id,couriers_name,couriers_phone):
        self.couriers_phone = couriers_phone
        self.couriers_name = couriers_name
        self.couriers_id = couriers_id

    def form_a_dict(self):
        new_courier = {                                
            "id" : self._couriers_id,        
            "name" : self._couriers_name,
            "phone" : self._couriers_phone
        }
        return new_courier
    
    @property                         #NAME GETTER
    def courier_name(self):
        return self._couriers_name

    @courier_name.setter                        # NAME SETTER  SET/ UPDATE NAME
    def courier_name(self,couriers_name):
        self._couriers_name = couriers_name

    @property                         #PHONE NUM GETTER
    def courier_phone_num(self):
        return self._couriers_phone
            
    @courier_phone_num.setter   #use for updating values         #VALIDATE AND UPDATE PHONE NUM
    def courier_phone_num(self, couriers_phone):
        test_length = str(couriers_phone)
        if type(couriers_phone) == str and len(test_length) == 10:
            self._couriers_phone = couriers_phone
        else:
            raise Exception("Phone number must be 10 digits long ")
    
    @property                    # COURIER ID GETTER
    def courier_id(self):
        return self._couriers_id

    @courier_id.setter                       #UPDATE COURIER ID 
    def courier_id(self, couriers_id):               
        with open("couriers_list.csv","r") as file:
            file_column_reader = csv.reader(file, delimiter = ",") #returns list
            if couriers_id in file_column_reader:
                self._couriers_id = couriers_id
            else:
                raise Exception ("No such courier id is found in the courier list")

    @courier_id.setter    #VALIDATE AND UPDATE COURIER ID
    def courier_id(self, couriers_id):
        if type(couriers_id) == int :
            self._couriers_id = couriers_id
        else:
            raise Exception("courier id must be an integer")
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
