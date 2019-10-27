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

def EraseAllExpensesForGivenDay():
    """
    erases expenses from the given day
    """
    try:
        day = IO.GetDay()
        Expenses.repo = [expense for expense in Expenses.repo if not Expenses.SameDay(Expenses.Day(expense), day)]
    except Exception as ex:
        IO.OutputException(ex)

def EraseExpensesForTimePeriod():
    """
    erases all expenses from the given time period
    """
    try:
        IO.OutputText("Ziua de inceput: ")
        startDay = IO.GetDay()
        IO.OutputText("Ziua de sfarsit: ")
        stopDay = IO.GetDay()
        Expenses.repo = [expense for expense in Expenses.repo if not (Expenses.Day(expense) >= startDay and Expenses.Day(expense) <= stopDay)]
    except Exception as ex:
        IO.OutputException(ex)

def EraseAllExpensesOfGivenCategory():
    """
    erases all expenses from the given category
    """
    try:
        category = IO.GetCategory()
        Expenses.repo = [expense for expense in Expenses.repo if not Expenses.SameCategory(Expenses.Category(expense), category)]
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
        else:
            IO.OutputText("Cheltuielile cerute sunt: ")
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def TotalAmmountForGivenCategory():
    """
    gets total ammount for a given expenses category
    """
    try:
        category = IO.GetCategory()
        totalAmmount = 0
        for expense in Expenses.repo:
            if Expenses.SameCategory(Expenses.Category(expense), category):
                totalAmmount += Expenses.Ammount(expense)
        if totalAmmount == 0:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            IO.OutputText("Suma totala ceruta este: " + str(totalAmmount))
    except Exception as ex:
        IO.OutputException(ex)

def WithoutExpensesOfGivenCategory():
    """
    removes all expenses of given category
    """
    try:
        category = IO.GetCategory()
        expenses = []
        for expense in Expenses.repo:
            if not Expenses.SameCategory(Expenses.Category(expense), category):
                expenses.append(expense)
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare")
        else:
            IO.OutputText("Cheltuielile cerute sunt: ")
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def ExitApplication():

    IO.OutputText("Iesire din aplicatie...")
    exit()

#---------------------------
    
commands = {
    "1": AddNewExpense,
    "2": UpdateExpense,
    "3": EraseAllExpensesForGivenDay,
    "4": EraseExpensesForTimePeriod,
    "5": EraseAllExpensesOfGivenCategory,
    "6": SearchExpensesGreaterThanAmmount,
    "9": TotalAmmountForGivenCategory,
    "13": WithoutExpensesOfGivenCategory,
    "16": ExitApplication
}