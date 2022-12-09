"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, contract, number_of_hours_worked, commmission, number_of_contracts_landed):
        self.name = name
        self.pay = pay
        self.contract = contract # contract type
        self.number_of_hours_worked = number_of_hours_worked
        self.comission = commmission
        self.number_of_contracts_landed = number_of_contracts_landed

    def get_contract(self):
        return self.contract

    def get_pay(self):
        if (self.number_of_hours_worked > 0):
            self.pay = self.pay * self.number_of_hours_worked
        return self.pay
    
    def get_comission(self):
        if (self.number_of_contracts_landed > 0):
            self.comission = self.comission * self.number_of_contracts_landed
        return self.comission

    def get_total_pay(self):
        total_pay = self.get_pay() + self.get_comission()
        return total_pay

    def __str__(self):
        print(f"{self.name} works on a contract of {self.number_of_hours_worked} hours at {self.pay} and receives a commission for {self.number_of_contracts_landed} contract(s) at {self.contract}/contract. Their total pay is {self.get_total_pay()} ")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
