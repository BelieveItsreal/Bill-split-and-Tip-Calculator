print("*************Welcome to the tip calculator******************")
bill = float(input("What was the total bill? $"))
tip = int(input("Whatpercentage tip you want to give? 10 , 12 or 15? "))
people = int(input("How many people to split the bill? "))

#adding tip into the bill
tip_bill = bill * (tip/100)

#printing the bill upto 2 decimal places
fin_bill = round(tip_bill,2)

#total bill calculation
total_bill = bill + fin_bill

#printing the bill upto 2 decimal places
fin_total = round(total_bill, 2)

#diving thge total bill for each person
each_person = fin_total / people
fin_person = round(each_person, 2)
print(f"Each person should pay: ${fin_person}")
