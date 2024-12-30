#rent calculator

total_rent = int(input("Enter the Total Rent = "))
Food_charges = int(input("Enter the Food Charges = "))
Water_charges = int(input("Enter the Water Charges = "))
ElectricityBill = int(input("Enter the Electricity Bill = "))
Person = int(input("Enter the Number of person living in room = "))

Amount = (total_rent + Food_charges + Water_charges + ElectricityBill)//Person
print("Each Person have to pay =",Amount)