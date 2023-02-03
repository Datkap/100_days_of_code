greetings = print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?"))
num_of_people = int(input("How many people to split the bill?"))
percentage_of_tip = float(input("What percentage tip would you like to give?"))
tip = total_bill*(percentage_of_tip/100)
total_cost = total_bill + tip

print("Total bill was: " + str(total_bill) + ".")
print("You decided to give " + str(percentage_of_tip) + "% of a tip, which gives " + str(tip))
if num_of_people == 0:
    print("Oh shit! Everybody run and there is a bill of " + str(total_bill) + " with nobody to pay! And no tips!")
elif num_of_people == 1:
    print("You need to pay " + str(total_cost) + " with tips included.")
else:
    print("There were " + str(num_of_people) + " people and each person has to pay "
          + str(round(total_cost/num_of_people)))
