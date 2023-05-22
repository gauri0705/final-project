import json
class user:
    def registration(self):
        self.name=input("enter the name of customer=")
        self.phone_no=int(input("enter the phone no of user="))
        self.email=input("enter the email id of user=")
        self.address=input("enter the address of user=")
        self.password=int(input("enter the password="))
        self.user_login={"name":self.name,"phone_no":self.phone_no,"email":self.email,"address":self.address,"password":self.password}
    

    def place_new_order(self):        
        self.menu=input("Food Menu:")
        self.item1=input("1. Tandoori Chicken (4 pieces) [INR 240]")
        self.item3=input("2. Vegan Burger (1 Piece) [INR 320]")
        self.item3=input("3. Truffle Cake (500gm) [INR 900]")
        food_item_numbers = input("Enter the numbers of the food items you want to order (separated by commas): ")
        food_item_numbers = [int(num) for num in food_item_numbers.split(",")]
        selected_food_items = []
    while True:
                print("-------------------------------- User ----------------------------------")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                

                user_choice = input("Enter your choice: ")
    for number in food_item_numbers:
                        if number == 1:
                            selected_food_items.append(1, "Tandoori Chicken", "4 pieces", 240)
                        elif number == 2:
                            selected_food_items.appen(2, "Vegan Burger", "1 piece", 320)
                        elif number == 3:
                            selected_food_items.append(3, "Truffle Cake", "500gm", 900)
                        else:
                            print("Invalid food item number!")
                            user.place_new_order(selected_food_items)
    def order_history():
       user.view_order_history()

    def update_profile():
                    
        self.full_name = input("Enter your full name (leave blank to skip): ")
        self.phone_number = input("Enter your phone number (leave blank to skip): ")
        self.email = input("Enter your email (leave blank to skip): ")
        self.address = input("Enter your address (leave blank to skip): ")
        self.password = input("Enter your password (leave blank to skip): ")

                


         
