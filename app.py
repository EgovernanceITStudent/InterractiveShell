"""
list of items :
1. coffee and bread
2. jollof rice
3. amala and Egusi soup
4. Beans and yam

price:
1. Coffe and bread = 150
2. Jollof rice = 200
3. Amala and Egusi soup = 300
4. Beans and yam = 250

"""

def greet():
    print("Hi ")
    print("Welcome to Egovernance IT Restaurant")
    print("")
# greet()

def options():
    print("Menu: Select any of the options below ")
    print("1. coffee and bread")
    print("2. jollof rice")
    print("3. amala and Egusi soup")
    print("4. Beans and yam")

    choice = input("") # input
    while choice != "quit": # This place as a bug
        if choice == "1":
            print("Coffee and bread")
            print("Price: $150")
        elif choice == "2":
            print("Jollof rice and beans")
            print("Price:  $100")
        elif choice == "3":
            print("Amala and Egusi Soup")
            print("Price: $230")
        elif choice == "4":
            print("Beans and yam")
            print("Price: $400")
        else:
            print("Option not in choice")
        choice = input("Choice Another Option or Quit to Exit: ") # input

    


    

def list_of_items():
    greet()
    options()
list_of_items()    

# welcome = ">>>>>Welcome To E-Shop<<<<<"
# print(welcome)
# # This loop will go on until the budget is integer or float
# while True:
#     try:
#         bg = float(input("Enter your budget: "))
#     # if budget is integer or float it will be stored
#     # temporarily in variable 's'
#         s = bg
#     except ValueError:
#         print("PRINT NUMBER AS A AMOUNT")
#     continue
# else:
#     break

# # dictionary to store product("name"), quantity("quant"),
# # price("price") with empty list as their values
# a ={"name":[], "quant":[], "price":[]}

# count = 0
# for number in range(1,100):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f'we have {count} even numbers')