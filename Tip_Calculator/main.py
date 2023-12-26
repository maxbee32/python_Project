print('Welcome to the tip calculator.')
total_bill = float(input('What is the total bill? $'))
tip_percentage = float(input('What percentge tip would you like to give? 10, 12, or 15? '))
bill_split = float(input('How many people to split the bill? '))

tip_and_bill = total_bill * (tip_percentage /100) 
bill_payment = (tip_and_bill + total_bill)/ bill_split
bill_payment = "{:.2f}".format(bill_payment)
print(f'Each person should pay: ${bill_payment}')
