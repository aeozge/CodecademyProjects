#The following example is the answer of tip calculator project in Codecademy.
meal = 44.50 #the price of meal.
tax = 0.0675 
tip = 0.15 # at least %15
meal = meal + (meal * tax)
total = meal + (meal * tip)

print("%.2f" % total)

