books = int(input("How many books do you want to buy? "))
amount = int(input("How much do you have? "))
amount_required = 100

if  books == amount_required > amount:
  print("you can purchase the books")

else:
  print("You donot have sufficient funds to buy the books")
  print(f"You will need  {amount} to buy the book.")