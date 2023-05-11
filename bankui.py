from modules.bankAccount import BankAccount, BankAccountJr

options = """
    Press to take actions below:
    a - create new regular bank account 
    b - add money/cash out 
    c - add interest rate 
    d - convert currency 
    e - check current currecy rate 
    f - create new junior bank account 
    g - check current balance 
    h - add supervisor to junior bank account
    x - quit
"""
print(options)

decision = input("Your decision: ").lower()

while decision!="x":

    if decision == "a":
        ownerName = input("Provide your name: ")
        newAccount = BankAccount(owner = ownerName)
        print(vars(newAccount))
        print(options)
        decision = input("Your decision: ").lower()

    elif decision == "f":
        ownerName = input("Provide your name: ")
        newAccount = BankAccountJr(owner = ownerName)
        print(vars(newAccount))
        print(options)
        decision = input("Your decision: ").lower()

    elif decision == "h":
        try:
            if isinstance(newAccount, BankAccountJr):
                supervisorName = input("Provide supervisor name: ")
                newAccount.add_supervisor(supervisorName)
                print(vars(newAccount))
                print(options)
                decision = input("Your decision: ").lower()
            else:
                print("You cannot add supervisor to regular bank account. Try with junior bank account type.")
                print(options)
                decision = input("Your decision: ").lower()
        except NameError:
            print("Bank accounts doesn't exists. Please create firstly.")
            print(options)
            decision = input("Your decision: ").lower()

    elif decision=="b":
        try:
            amount = float(input("Provide amount : "))
            if amount > 0:
                newAccount.cash_in(amount)
                print(vars(newAccount))
                print(options)
                decision = input("Your decision: ").lower()
            else:
                newAccount.cash_out(amount)
                print(vars(newAccount))
                print(options)
                decision = input("Your decision: ").lower()
        except NameError:
            print("Bank accounts doesn't exists. Please create firstly.")
            print(options)
            decision = input("Your decision: ").lower()
        except ValueError:
            print("Please use only numeric input")
            print(options)
            decision = input("Your decision: ").lower()

    elif decision=="c":
        try:
            newAccount.add_int_rate()
            print(vars(newAccount))
            print(options)
            decision = input("Your decision: ").lower()
        except NameError:
            print("Bank accounts doesn't exists. Please create firstly.")
            print(options)
            decision = input("Your decision: ").lower()

    elif decision=="d":
        try:
            newCurrency = input("Type currency code: ").upper()
            result = newAccount.convert_currency(newCurrency)
            if result == False:
                print(f"Currency {newCurrency} doesn't exist. Try again.")
                print(options)
                decision = input("Your decision: ").lower()
            elif result is None:
                print("Nothing to change")
                print(options)
                decision = input("Your decision: ").lower()
            else:
                print(vars(newAccount))
                print(options)
                decision = input("Your decision: ").lower()
        except NameError:
            print("Bank accounts doesn't exists. Please create firstly.")
            print(options)
            decision = input("Your decision: ").lower()

    elif decision == "e":
        currencyToCheck = input("Type currency code: ").upper()
        try:
            result = newAccount.currency_rates(currencyToCheck)
            if not result:
                print(f"Currency {currencyToCheck} not available")
            print(options)
            decision = input("Your decision: ").lower()
        except NameError:
            print("Bank accounts doesn't exists. Please create firstly.")
            print(options)
            decision = input("Your decision: ").lower()

    elif decision=="g":
        try:
            print(f"Current balance: {newAccount._BankAccount__balance} {newAccount._BankAccount__currency}")
            decision = input("Your decision: ").lower()
        except NameError:
            print("Bank accounts doesn't exists. Please create firstly.")
            print(options)
            decision = input("Your decision: ").lower()

    else:
        print("Action not available. Try again.")
        print(options)
        decision = input("Your decision: ").lower()

print("Bye")





