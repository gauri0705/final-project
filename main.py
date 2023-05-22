from admin import*
from user import*
import sys
print("WELCOME TO FOOD ORDERING APP....")
while True:
    print("Welcome to the Food Delivery App!")
    print("1for..... Admin Login")
    print("2 for.... User Register")
    print("3 for.... User Login")
    choice = input("Enter your choice: ")
    if choice == "1":
        res=admin()
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")
        print("Admin logged in successfully!")
        while True:
            print("-------------------------------- Admin ----------------------------------")
            print("1 for... Add new food items")
            print("2 for.... Edit food items")
            print("3 for.... View list of all food items")
            print("4 for.... Remove a food item")
            print("5 for.... exit")

            admin_choice = input("Enter your choice: ")
            if admin==1:
                res.add_food_item()
            elif admin==2:
                res.edit_food_item()   
            elif admin==3:
                res.view_food_item() 
            elif admin==4:
                res.remove_food_item()          
            elif admin==5:
                sys.exit()
            else:
                print("enter valid input....")     
    if choice=="2":
        res=user()
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = user.get(email)
        if user and user.password == password:
            print("User logged in successfully!")
        while True:
            print("------------------user------------------------")
            print("1 for............PLACE NEW ORDER")
            print("2 for.............ORDER HISTORY")
            print("3 for..............UPDATE PROFILE")
            print("4 for.........EXIT")
            user_choice = input("Enter your choice: ")
            if user==1:
                res.place_new_order()
            elif user==2:
                res.order_history()   
            elif user==3:
                res.update_profile() 
            elif user==4:
                sys.exit() 
            else:
                print("enter valid input...")   
    if choice=="3":
        print("thank you for visiting the food delivery app...")
        sys.exit()  
