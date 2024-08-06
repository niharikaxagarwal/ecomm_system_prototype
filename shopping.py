#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


class Product:
    def __init__(self, name, price, quantity,identifier, brand):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.identifier = identifier
        self.brand = brand

    def to_json(self):
        return {"name": self.name,"price": self.price,"quantity": self.quantity,"identifier": self.identifier,"brand": self.brand}

class Clothing(Product):  #subclass of class product
    def __init__(self, name, price, quantity, identifier, brand, size, material):
        super().__init__(name, price, quantity, identifier, brand)
        self.size = size
        self.material = material

    def to_json(self):
        data = super().to_json()
        data["size"] = self.size
        data["material"] = self.material
        return data

class Food(Product):   #subclass of class product
    def __init__(self, name, price, quantity, identifier, brand, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity,identifier, brand)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans

    def to_json(self):
        data = super().to_json()
        data["expiry_date"] = self.expiry_date
        data["gluten_free"] = self.gluten_free
        data["suitable_for_vegans"] = self.suitable_for_vegans
        return data

class Footwear(Product): #subclass of class product
    def __init__(self, name, price, quantity, identifier, brand, size_UK, colour):
        super().__init__(name, price, quantity, identifier, brand)
        self.size_UK = size_UK
        self.colour = colour

    def to_json(self):
        data = super().to_json()
        data["size_UK"] = self.size_UK
        data["colour"] = self.colour
        return data

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def addProduct(self, p):
        self.cart.append(p)

    def removeProduct(self, p, EAN):
        self.cart.pop(p)
        EAN.pop(p)

    def getContents(self):
        return sorted(self.cart, key=lambda x: x.name)

    def changeProductQuantity(self, p, q):
        p.quantity = q
        

class Actual_Shopping:
    def entries(EAN):
        name=input("Insert product name / type: ")
        price=float(input("Insert its price: "))
        quantity=int(input("Insert its quantity: "))
        brand=input("Insert its brand: ")
        identifier=int(input("Insert its EAN code: "))
                       
        stop=True
        while stop:
            if(identifier not in EAN) and (len(str(identifier))==13):
                EAN.append(identifier)
                stop= False
        
            else:
                print("Identifier must be a 13 digit sequence and unique")
                identifier=int(input("Insert its EAN code:"))
            
        return name,price,quantity,brand,identifier,EAN
                       
    def main():
        EAN=[]
        cart=ShoppingCart()
        print("The program has started.")
        print("Insert your next command (H for help):")
        terminated = False
        while not terminated:
            command = input("Insert your next command: ").strip().upper()
                       
            if command == "A":
                print("Adding a new product: ")
                product_type = input("Insert its type (Clothing, Food, Footwear): ").strip().capitalize()
                
                if product_type == "Clothing":
                    name, price, quantity, identifier, brand,EAN= Actual_Shopping.entries(EAN)
                    size = input("Insert its size: ")
                    material = input("Insert its material: ")
                    product = Clothing(name, price, quantity, identifier, brand, size, material)
                       
                elif product_type == "Food":
                    name, price, quantity, identifier, brand,EAN= Actual_Shopping.entries(EAN)
                    expiry_date = input("Insert its expiry date: ")
                    while True:
                        gluten_free = input("Is it gluten free? (True/False): ").strip().lower()
                        if gluten_free=='true' or gluten_free=='false':
                            suitable_for_vegans = input("Is it suitable for vegans? (True/False): ").strip().lower()
                            if suitable_for_vegans=='true' or suitable_for_vegans=='false':
                                product = Food(name, price, quantity, identifier, brand, expiry_date, gluten_free, suitable_for_vegans)
                                break
                            else:
                                print("enter valid input")
                                                     
                
                elif product_type=='Footwear':
                    name, price, quantity, identifier, brand,EAN= Actual_Shopping.entries(EAN)
                    colour = input("What is the colour?: ")
                    
                    size_UK = input("Insert your size_UK, choose between 4-8: ")
                    product = Footwear(name,price, quantity, identifier, brand, size_UK, colour)
                    
                else:
                    print("Invalid input")
                    continue
                
                    
                
                contents=cart.getContents()
                print(f"The product {name} has been added to the cart")
                i=1
                for product in contents:
                    i+=1
                    
                    
                print(f"The cart contains {i} product(s).")
                cart.addProduct(product)
                    
                       
                       
            elif command == "R":
                identifier=int(input("Enter EAN code of the product to remove the product: "))
                index_EAN=EAN.index(identifier)
                       
                cart.removeProduct(index_EAN,EAN)
                print(f"Product {name} has been removed from the cart")
            
            
            
                             
            elif command == "S":
                print("The total of expenses:")
                contents = cart.getContents()
                
                for product in contents:
                    i=1
                    print(f"{i}-{product.quantity} * {product.name} = {product.price}")
                    i=i+1
                total_cost = sum(product.price * product.quantity for product in contents)
                print(f"Total cost: GBP {total_cost}")
                             
                        
                        
            elif command == "Q":
                identifier = int(input("Enter the EAN of Product to change quantity: "))
                new_quantity = int(input("New quantity: "))
                product_of_old_quantity = None
                                         
                for pt in cart.getContents():
                    
                    if product.identifier == identifier:
                        product_of_old_quantity = pt
                                         
                if product_of_old_quantity is not None:
                    cart.changeProductQuantity(product_of_old_quantity, new_qantity)
                                         
                else:
                    print("Product not found in cart")
                    
                    
                                         
            elif command == "E":
                contents = cart.getContents()
                json_data = [product.to_json() for product in contents]
                json_str = json.dumps(json_data, indent=4)
                print(json_str)
                                         
                    
                    
            elif command=='T':
                print("Goodbye.")
                break
            
                                         
            elif command == "H":
                print("Available commands:")
                print("A: Add a product to the cart")
                print("R: Remove a product from the cart")
                print("S: Print a summary of the cart")
                print("Q: Change the quantity of a product in the cart")
                print("E: Export a JSON version of the cart")
                print("T: Terminate the program ")
                print("H: List the supported commands")
                                        
            else:
                
                print("Command not recognized. Please try again.")
        

                       
        
    


# In[ ]:


if __name__ == "__main__":
    Actual_Shopping.main()


# In[ ]:




