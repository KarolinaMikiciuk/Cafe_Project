#pickle the object then unpickle to use pandas to write into csv

class Product(object):
    def __init__(self,product_price,product_name,product_id) -> None:       #-> Product lol
        self.product_price = product_price
        self.product_name = product_name        #not supposed to return
        self.product_id = product_id
                                    
    def form_a_dict(self):
        new_product = {                                
            "id" : self._product_id,        
            "name" : self._product_name,
            "phone" : self._product_price
        }
        return new_product 
    
    @property                         #NAME GETTER
    def product_name(self):
        return self._product_name

    @product_name.setter                        #UPDATE NAME 
    def product_name(self,product_name):
        self._product_name = product_name

    @property                         #PRODUCT PRICE GETTER
    def product_price(self):
        return self._product_price
            
    @product_price.setter   #use for updating values         #VALIDATE AND UPDATE PRODUCT PRICE
    def product_price(self, product_price):
        if type(product_price) == float :
            self._product_price = product_price
        else:
            raise Exception("Product price must be a float")
    
    @property                    # PRODUCT ID GETTER
    def product_id(self):
        return self._product_id

    @product_id.setter                     #VALIDATE AND UPDATE PRODUCT ID
    def product_id(self, product_id):
        if type(product_id) == int :
            self._product_id = product_id
        else:
            raise Exception("Product id must be an integer")
    

