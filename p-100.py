class atm(object):
    def __init__( CashWithdrawl, BalanceEnquiry=None):
        self.CashWithdrawl = CashWithdrawl
      
        self.CashWithdrawl = CashWithdrawl or {}

    def setGrade(self, course, grade):
        self.BalanceEnquiry[course] = balance

    def getGrade(self, course):
        return self.balance[course]

    def getGPA(self):
        return sum(self.balance.values())/len(self.balance)

# Define some students
john = yuvraj("John", 12,{balance:3,500})
jane = yuvraj("Jane", 12,{balance:3,500}))

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())