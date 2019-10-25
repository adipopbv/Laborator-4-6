from UI import IO
import Repo
import Expenses

def DoCommandWithId(commandId):
    commands[commandId]()

def AddNewExpense():
    """
    adds a new expense to the expenses repository
    """
    try:
        expense = IO.GetExpense()
        Repo.AddToRepo(Expenses.repo, expense)
    except Exception as ex:
        IO.OutputException(ex)

def UpdateExpense():
    """
    updates an expense to a new state
    """ 
    try:
        originalExpense = IO.GetExpense()
        IO.OutputText("De inlocuit cu...")
        updatedExpense = IO.GetExpense()
        Repo.SwapInRepo(Expenses.repo, originalExpense, updatedExpense)
    except Exception as ex:
        IO.OutputException(ex)

def SearchExpensesGreaterThanAmmount():
    """
    searches for expenses greater than a given ammount
    """
    try:
        ammount = IO.GetAmmount()
        expenses = []
        for expense in Expenses.repo:
            if Expenses.GreaterAmmount(Expenses.Ammount(expense), ammount):
                expenses.append(expense)
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        IO.OutputText("Cheltuielile cerute sunt: ")
        for expense in expenses:
            IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

#---------------------------
    
commands = {
    "1": AddNewExpense,
    "2": UpdateExpense,
    "6": SearchExpensesGreaterThanAmmount,
    #"9": TotalAmmountForGivenCategory,
    #"13": EraseExpensesOfGivenCategory,
    #"16": ExitApplication
}