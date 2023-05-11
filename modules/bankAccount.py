import requests
import pandas as pd

class BankAccount:
    accountCount = 0

    def __init__(self, owner:str, balance:float=0, rate:float = 0.01 ,currency:str="PLN"):
        self.__owner = owner
        self.__balance = balance
        self.__currency = currency
        self.__rate = rate
        BankAccount.accountCount+=1

    def add_int_rate(self):
        self.__balance = round(self.__balance + (self.__balance*self.__rate),2)

    def cash_in(self, *amounts:float):
        for amount in amounts:
            if amount > 0:
                self.__balance += amount

    def cash_out(self, *amounts):
        current_balance = self.__balance 
        for amount in amounts:
            if amount < 0 and current_balance + amount > 0:
                self.__balance += amount
                current_balance = self.__balance

    def convert_currency(self, newCurrency):
        response_API = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/')
        data = response_API.json()[0]
        data = pd.DataFrame(data["rates"])[["code","mid"]]

        availableCurrencies = list(data["code"].unique())
        currentCurrency = self.__currency
        newCurrency = newCurrency.upper()

        if currentCurrency != newCurrency and (newCurrency in availableCurrencies or newCurrency=="PLN"):
            get_rate = 1/data[data["code"]==currentCurrency]["mid"].item() if newCurrency=="PLN" else data[data["code"]==newCurrency]["mid"].item()
            self.__balance = self.__balance*(1/get_rate)
            self.__currency = newCurrency
            return True

        elif currentCurrency == newCurrency:
            return None

        elif newCurrency not in availableCurrencies:
            return False

    @staticmethod 
    def currency_rates(currency:str): #jak zwykla funkcja poza klasa, łatwy dostęp
        response_API = requests.get('http://api.nbp.pl/api/exchangerates/tables/a/')
        data = response_API.json()[0]
        data = pd.DataFrame(data["rates"])[["code","mid"]]

        currency = currency.upper()
        output = data[data["code"]==currency]["mid"]

        if len(output)>0:
            output = output.item()
            print(output)
            return True
        else:
            return False

class BankAccountJr(BankAccount):
    def __init__(self, owner:str, balance:float=0, rate:float = 0.01 ,currency:str="PLN"):
        super().__init__(owner, balance,rate, currency)
        if self._BankAccount__balance > 50000:
            print("Initial balance exceeded limit")
            return False
         
    def add_int_rate(self):
        self._BankAccount__balance = self._BankAccount__balance + (self._BankAccount__balance * (self._BankAccount__rate+0.02))

    def add_supervisor(self, supervisorName:str):
        self.__supervisor = supervisorName

