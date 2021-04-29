"""

This program will allow the user to make transactions to a savings account.

The account initially has a balance of $2,000. The first option is to make the depostit
in the savings account of any amount.The second option allows the userto make a withdrawal
that is less or equal to their current balance. The third option is to obtain the balnce.
The fourht option is to quit. There will four functions that will allow the user to make 
transactions to their savings account. Function one will calculate the amount for the first option,
functions two will calculate the amount for option two,functiona three will print the amount
for options three, and function four will end the user's transactions. 


function1 will add deposit to current balance: $2,000

function2 will withdraw money from the savings account, will output "denied" if maximum withdrawal
limit is reached

function3 will print the current balance

function4 will allow the user to quit

if the user makes a deposit, then it will output to the user "Deposit processed"

if the user attempts to make a withdrawal larger than the current balance, it will output "Denied.
Maximum withdrawal is ___"

if the user request balance of their savings account, it will output to the user 
"Balance ___", or else if user did not input the proper number, it will output
"Error. You did not enter proper number."

"""

"""
#options
print("options:")
print("1. Make a Deposit")
print("2. Match a Withdrawal")
print("3. Obtain Balnace")
print("4. Quit")
balance=2000
while True:
    num=int(input("Make a selections from the options menu: "))
    if num==1:
        deposit= float(input("Enter amount of deposit: "))
        balance +=deposit
        print("Deposit Processe.")
    elif num==2:
        withdrawal=float(input("Enter amount of withdrawal: "))
        while (withdrawal>balance):
            print("Denied. Maximum withdrawal is ${0:,.2f}"
                    .format(balance))
            withdrawal=float(input("Enter amount of withdrawal: "))
        balance-=withdrawal
        print("Withdrawal Processed.")
    elif num==3:
        print("Balance: ${0:,.2f}".format(balance))
    elif num==4:
        break
    else:
        print("You did not enter a proper number.")
"""
print("Options:")
print("1. Make a Deposit")
print("2. Make a Withdrawal")
print("3. Obtain Balance")
print("4. Quit")
balance = 2000
while True:
    num = int(input("Make a selection from the options menu: "))
    if num == 1:
        deposit = float(input("Enter amount of deposit: "))
        balance += deposit
        print("Deposit Processed.")
    elif num == 2:
        withdrawal = float(input("Enter amount of withdrawal: "))
        while (withdrawal > balance):
            print("Denied. Maximum withdrawal is ${0:,.2f}" .format(balance))
            withdrawal = float(input("Enter amount of withdrawal: "))
        balance -= withdrawal
        print("Withdrawal Processed.")
    elif num == 3:
        print("Balance: ${0:,.2f}" .format(balance))
    elif num == 4:
        break
    else:
        print("You did not enter a proper number.")
