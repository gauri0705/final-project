import json
class admin:
    def __init__(self):
      self.food={}
      self.food_id=len(self.food)+1

    def add_food_items(self):
      self.name=input("enter the name of food item=")
      self.quantity=int(input("enter the quantity of food item="))
      self.prize=int(input("enter the prize of food item="))
      self.stock=int(input("enter the no of stock available of food item="))
      self.discount=int(input("enter the discount of food item="))
      self.item={"name":self.name,"quantity":self.quantity,"prize":self.prize,"stock":self.stock,"discount":self.discount}
      self.food_id=len(self.food)+1
      self.food[self.food_id]=self.item
      with open("food_items.json","w")as f:
         json.dump(self.food,f)
         print("item added sucessfully.........")
    def remove_food(self):
      for k,v in self.food.items():
         print("food id",k,"and food items",v)
         del self.food[int(input("enter the food item id which you want to delete="))]
         with open("food_items.json","w")as f:
            json.dump(self.food,f)
    print("item removed sucessfully")

    def edit_food_item(self):
       for k,v in self.food.items():
         print("food id",k,"and food items",v)
         food_code=int(input("enter the food item id which you want to edit="))
         food_edit=input("enter the field which you want to edit=")
         food_updated_value=input("enter the updated value......")
         self.food[food_code][food_edit]=food_updated_value
         with open("add_food.json","w")as f:
            json.dump(self.food,f,indent=4)
            return self.add_food_items  
         
    def view_food_item(self):
       for k,v in self.food.items():
          print(f"id :{k} food : {v}") 


