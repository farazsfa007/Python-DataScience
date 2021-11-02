class Account:
    def __init__(self,name,acc_no,branch,balance):
        self.holder_name=name
        self.acc_no=acc_no
        self.branch=branch
        self.balance = balance

    def debit(self, amt):
        self.balance -= amt
        print(f"{amt} debited from {self.holder_name}'s account")


acc1 = Account("Mr. Neo Anderson", 123456789, 'hazratganj', 2000)
acc2 = Account("Mrs. Neo Anderson", 987654321, 'hazratganj', 5000)

acc1.debit(1500)
acc2.debit(2300)

print(acc1.balance)
print(acc2.balance)


# homework
# 1. Create a method debit in above class.
# 2. Create a method which displays all the account details.
# 3. Create a method getLoan , it should print 'loan approved' if balance
#     is above 50000 else print insuffient balance.