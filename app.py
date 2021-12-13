

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
    print("Here are the list of options to navigate your way through the restaurant")
    print("1. coffee and bread")
    print("2. jollof rice")
    print("3. amala and Egusi soup")
    print("4. Beans and yam")

    choice = input("")
    if choice == "1":
        print("Coffee and bread")
        print("Price: $150")
    elif choice == "2":
        print("Jollof rice and beans")
        print("Price:  $100")
    elif choice == "3":
        print("Amala and Egusi Soap")
        print("Price: $230")
    elif choice == "4":
        print("Beans and yam")
        print("Price: $400")
    else:
        print("Option not in choice")
    return choice


def list_of_items():
    greet()
    options()
list_of_items()    