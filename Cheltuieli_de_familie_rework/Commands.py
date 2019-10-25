from Cheltuieli_de_familie_rework.UI import IO
from Cheltuieli_de_familie_rework import Repo

commands = {
    1: AddNewExpense,
    2: UpdateExpense,
    #6: SearchExpensesGreaterThanAmmount,
    #9: TotalAmmountForGivenCategory,
    #13: EraseExpensesOfGivenCategory,
    #16: ExitApplication
}

def DoCommandWithId(commandId):
    commands[commandId]()

def AddNewExpense():
    """
    adds a new expense to the expenses repository
    """
    try:
        expense = IO.GetExpense()
        Repo.AddToRepo(Repo.expenseRepo, expense)
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
        Repo.SwapInRepo(Repo.expenseRepo, originalExpense, updatedExpense)
    except Exception as ex:
        IO.OutputException(ex)