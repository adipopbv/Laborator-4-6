import Commands
from UI import IO

def DoFunctionalityWithId(funcId):
    """
    starts the functionality with the given id
    
    Args:
        commandId (int): a functionality id
    """
    functionalities[funcId]()

#---------------------------

def AddNewExpense():
    """
    adds a new expense to the expenses repository
    """
    try:
        Commands.AddNewExpense(IO.GetExpense())
        IO.OperationSuccesful()
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
        Commands.UpdateExpense(originalExpense, updatedExpense)
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)

def EraseAllExpensesForGivenDay():
    """
    erases expenses for the given day
    """
    try:
        day = IO.GetDay()
        Commands.EraseAllExpensesForGivenDay(day)
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)
    
def EraseExpensesForTimePeriod():
    """
    erases all expenses from teh given time period
    """
    try:
        IO.OutputText("Ziua de inceput: ")
        startDay = IO.GetDay()
        IO.OutputText("Ziua de sfarsit: ")
        stopDay = IO.GetDay()
        Commands.EraseExpensesForTimePeriod(startDay, stopDay)
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)

def EraseAllExpensesOfGivenCategory():
    """
    erases all expenses of the given category
    """
    try:
        Commands.EraseAllExpensesOfGivenCategory(IO.GetCategory())
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)

def SearchExpensesGreaterThanAmmount():
    """
    searches for expenses greater than a given ammount
    """
    try:
        expenses = Commands.SearchExpensesGreaterThanAmmount(IO.GetAmmount())
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            IO.OutputText("Cheltuielile cerute sunt: ")
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def SearchExpensesBeforeGivenDayAndLessThanAmmount():
    """
    searches all expense before a given day and less than a given ammount
    """
    try:
        expenses = Commands.SearchExpensesBeforeGivenDayAndLessThanAmmount(IO.GetDay(), IO.GetAmmount())
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            IO.OutputText("Cheltuielile cerute sunt: ")
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def SearchAllExpensesOfGivenCategory():
    """
    searches all expenses of given category
    """
    try:
        expenses = Commands.SearchAllExpensesOfGivenCategory(IO.GetCategory())
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

functionalities = {
    "1": AddNewExpense,
    "2": UpdateExpense,
    "3": EraseAllExpensesForGivenDay,
    "4": EraseExpensesForTimePeriod,
    "5": EraseAllExpensesOfGivenCategory,
    "6": SearchExpensesGreaterThanAmmount,
    "7": SearchExpensesBeforeGivenDayAndLessThanAmmount,
    "8": SearchAllExpensesOfGivenCategory,
    "9": TotalAmmountForGivenCategory,
    "10": DayWithGreatestAmmount,
    "11": ExpensesWithGivenAmmount,
    "12": ExpensesSortedByCategory,
    "13": WithoutExpensesOfGivenCategory,
    "14": WithoutExpensesLessThanGivenAmmount,
    "15": UndoLastOperation,
    "16": ExitApplication
}