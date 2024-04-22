# Basic_Calculator
n1=int(input("Enter the First Number: "))
n2=int(input("Enter the Second Number: "))
print("Make your choice")
operation=input("Enter the Operation(+,-,*,/) :")

if operation=='+':
    print("Sum", n1+n2)
elif operation=='-':
    print("Difference", n1-n2)
elif operation=='*':
    print("Multiplication", n1*n2)
elif operation=='/':
    if n2!=0:
        print("Division", n1/n2)
    else:
        print("Can`t Divided by 0")
else:
    print("Invalid Choice/Operation")

# Number_System
a=int(input("Enter the Starting Point: "))
b=int(input("Enter the Ending Point: "))
c=int(input("Enter the Updation Point: "))
print("## Make Your Choice ##")
print("Choose" "1.For Row Wise Printing", "2.For Column Wise Printing")
choice=int(input("Enter the Choice: "))
if choice==1:
    for i in range(a,b+1,c):
        print(i, end=' ')
elif choice==2:
    for i in range(a,b+1,c):
        print(i)
else:
    ("Invalid Choice")

# Voting_System
Name=input("PLease Enter your Name: ").capitalize()
Age=int(input("Please Enter Your Age: "))
Voter_ID_No=int(input("Please Enter your Voter ID Number: "))
if Age<18:
    print("You are not Eligible for Voting")
else:
    print("Please Make your Party Choice: ")
    print("Press" "1.BJP", "2.CONG", "3.S.P", "4.AAP")
    choice=int(input("Enter the Choice: "))
    if choice==1:
        print(" BJP ")
    elif choice==2:
        print(" CONG ")
    elif choice==3:
        print(" S.P ")
    elif choice==4:
        print(" AAP ")
    else:
        ("You choose an Invalid Choice: ")
    print("Thank You For voting")

# Student_Record_Grading_System
STD_Name=input("Enter the name of Student: ")
Class=input("Enter the class of the student:")
Sec=input("Enter the section of the student: ")
Roll_No=int(input("Enter the Roll No: "))
print("Enter the marks of the Subjects")
Maths=int(input("Enter the marks of the Maths Subject: "))
Chemistry=int(input("Enter the marks of the Chemistry Subject: "))
Electronics=int(input("Enter the marks of the Electronics Subject: "))
Python_Programming=int(input("Enter the marks of the Python_Programming Subject: "))
English=int(input("Enter the marks of the English Subject: "))
Total_Marks=Maths+Chemistry+Electronics+Python_Programming+English
Percentage=Total_Marks/5
print(Total_Marks)
print(Percentage,"%")
if Percentage>90:
    print("A grade")
    print("You Have Done an Excellent Work")
elif Percentage>75:
    print("B Grade")
    print("Good job")
elif Percentage>55:
    print("C Grade")
    print("You need to improve")
elif Percentage>35:
    print("D Grade")
    print("You need to work hard")
else:
    print("You Failed")

# Inventory_System
inventory = {
    'fruits': {
        'apple': {'quantity': 100, 'price': 140},
        'banana': {'quantity': 50, 'price': 50},
        'orange': {'quantity': 75, 'price': 80}
    },
    'vegetables': {
        'carrot': {'quantity': 80, 'price': 40},
        'tomato': {'quantity': 60, 'price': 45},
        'spinach': {'quantity': 40, 'price': 20}
    },
    'dairy': {
        'milk': {'quantity': 120, 'price': 33},
        'cheese': {'quantity': 90, 'price': 70},
        'yogurt': {'quantity': 70, 'price': 45}
    }
}
choice = 0
while choice != 6:
    print("\n1. Display Inventory")
    print("2. Make Purchase")
    print("3. Restock Inventory")
    print("4. Print Out of Stock Items")
    print("5. Add more items")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Current Inventory:")
        for category, items in inventory.items():
            print(f"{category.capitalize()}:")
            for item, details in items.items():
                print(f"  {item.capitalize()}: {details['quantity']} (Price: Rs {details['price']})")
    elif choice == 2:
        item = input("Enter the item to purchase: ").lower()
        quantity = int(input("Enter the quantity to purchase: "))
        for category, items in inventory.items():
            if item in items:
                if items[item]['quantity'] >= quantity:
                    items[item]['quantity'] -= quantity
                    print(
                        f"Successfully purchased {quantity} {item.capitalize()}. Remaining quantity: {items[item]['quantity']}.")
                else:
                    print("Error: Not enough quantity in stock.")
    elif choice == 3:
        item = input("Enter the item to restock: ").lower()
        quantity = int(input("Enter the quantity to restock: "))
        for category, items in inventory.items():
            if item in items:
                items[item]['quantity'] += quantity
                print(
                    f"Successfully restocked {quantity} {item.capitalize()}. Total quantity: {items[item]['quantity']}.")
    elif choice == 4:
        print("Out of Stock Items:")
        for category, items in inventory.items():
            for item, details in items.items():
                if details['quantity'] == 0:
                    print(f"  {item.capitalize()}")
    elif choice == 5:
        category = input("Enter the category of the new item: ").lower()
        item = input("Enter the name of the new item: ").lower()
        quantity = int(input("Enter the quantity of the new item: "))
        price = float(input("Enter the price of the new item: "))

        if category in inventory:
            if item not in inventory[category]:
                inventory[category][item] = {'quantity': quantity, 'price': price}
                print(f"Successfully added {item.capitalize()} to {category.capitalize()} category.")
            else:
                print("Error: Item already exists in the inventory.")
        else:
            inventory[category] = {item: {'quantity': quantity, 'price': price}}
            print(f"Successfully added {item.capitalize()} to a new category: {category.capitalize()}.")
    elif choice != 6:
        print("Invalid choice. Please try again.")


# Roll_Dice
import random
print(random.randint(1,6))


# Rock_Paper_Scissors
import random
no_of_rounds=int(input("Enter the number of rounds: "))
user_points = 0
computer_points = 0
for round_number in range(no_of_rounds):
    user_action = input(f"Round {(round_number+1)}: Rock, Paper or Scissors: ")
    while user_action not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please try again.")
        user_action = input("Round {}: Rock, Paper or Scissors: ".format(round_number+1)).lower()
    computer_action = random.choice(["rock", "paper", "scissors"])
    print("Computer chose: {}".format(computer_action))
    if user_action == computer_action:
        print("It's a tie!")
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "scissors" and computer_action == "paper") or \
         (user_action == "paper" and computer_action == "rock"):
        user_points += 1
        print("You win this round!")
    else:
        computer_points += 1
        print("Computer wins this round!")
if user_points > computer_points:
    print("\nYou Win :)")
else:
    print("\nYou Lose :(")