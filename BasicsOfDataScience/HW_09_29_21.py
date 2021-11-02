class Credited():
    def __init__(self,Name,Acc_no,branch,balance):
        self.H_name=Name
        self.Account=Acc_no
        self.Branch=branch
        self.balance=balance

    def Credit(self, amt):
        self.balance += amt
        print(f"\n{self.H_name} {amt} Credited in Your account.")
    def Loan(self):
        if self.balance>50000:
            print('loan Approved')
        else:
            print('Insefficient balance\n')
    def Acc_details(self):
        print(f"Account Holder Name: {self.H_name}\nAccount No:{self.Account}\nBranch:{self.Branch}\nAccount Balance: {acc.balance}\n")

acc=Credited('Mr. Leon Kennedy',987654321,'Dubagga',10000)

acc.Credit(5000)
print('Avialable Balance is: ',acc.balance,'\n')
print('Loan Status:- ',end='')
acc.Loan()
print('Account Details:-\n')
acc.Acc_details()
