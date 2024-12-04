print("Welcome to the greatest pizza place on Earth!")
#welcome statuement^
HST = 0.13
LABOUR = 0.75
RENT = 1
MATERIAL = 0.5
#constant variables^
diameter = float(input("What is the diameter of the pizza you want? (in) "))
#gets diameter from user^
subtotal = RENT + LABOUR + (diameter * MATERIAL)
#calculates subtotal^
tax = subtotal * HST
total = subtotal + tax
#final cost^
total = round(total, 2)
print("Your total is: $ ", total)
#final statement^