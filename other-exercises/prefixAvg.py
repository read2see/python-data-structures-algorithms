from random import randint, uniform

# Request user's input to populate a list of expenses
def requestUserInput():
    totalDays = int(input("Enter the number of days: "))
    expenses = []
    for i in range(totalDays):
        expenses.append(float(input(f"Day #{i+1} Expenses = ")))
        
    return expenses

# Generate a random n list of random expenses
def generateRandomExpenses(maxDays, maxExpense):
    totalDays = randint(1,maxDays)
    expenses = []
    for i in range(totalDays):
        expenses.append(round(uniform(1,maxExpense),2))
    return expenses

# Print Scenario/User info
def displayScenarioInfo(expenses):
    print("Scenario Info:")
    print("-"*60)
    print("Total Days = ", len(expenses))
    print("Scenario Expenses list = ", expenses)
    for i in range(len(expenses)):
        print(f"Day #{i+1} Expense: {expenses[i]}")
    print("-"*60)
    
# Find prefix average based on a list of n items ,O(n) algorithm
def computePrefixAvg(expenses):
    
    expensesSum = expenses[0]
    
    prefixAvg = [expenses[0]]
    
    for i,item in enumerate(expenses[1:]):
        expensesSum += item
        prefixAvg.append(round(expensesSum/(i+2),2))
    
    return prefixAvg

# Find prefix average based on a list of n items, O(n^2) algorithm
def altComputePrefixAvg(expenses):
    
    prefixAvg = []
    for i in range(len(expenses)):

        expensesSum = 0

        for j in range(i+1):

            expensesSum += expenses[j]

        prefixAvg.append(expensesSum/(i+1))

    return prefixAvg

expenses = generateRandomExpenses(10,500)

displayScenarioInfo(expenses)

print("Prefix Average List = ",computePrefixAvg(expenses))