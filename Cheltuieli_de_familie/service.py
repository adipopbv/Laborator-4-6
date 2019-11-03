import Commands
from UI import IO
import Repo
import Expenses

def DoFunctionalityWithId(funcId):
    """
    starts the functionality with the given id
    
    Args:
        commandId (int): a functionality id
    """
    if Expenses.repo == [] or Expenses.historyRepo == []:
        Expenses.repo = Repo.MakeRepo()
        Expenses.historyRepo = Repo.MakeRepo()
    functionalities[funcId]()

#---------------------------

def AddNewExpense():
    """
    adds a new expense to the expenses repository
    """
    try:
        Commands.AddNewExpense(Expenses.repo, IO.GetExpense())
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def UpdateExpense():
    """
    updates an expense to a new state
    """
    try:
        originalExpense = IO.GetExpense()
        IO.OutputText("De inlocuit cu...")
        updatedExpense = IO.GetExpense()
        Expenses.repo = Commands.UpdateExpense(Expenses.repo, originalExpense, updatedExpense)
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def EraseAllExpensesForGivenDay():
    """
    erases expenses for the given day
    """
    try:
        day = IO.GetDay()
        Expenses.repo = Commands.EraseAllExpensesForGivenDay(Expenses.repo, day)
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))
    
def EraseExpensesForTimePeriod():
    """
    erases all expenses from teh given time period
    """
    try:
        IO.OutputText("Ziua de inceput: ")
        startDay = IO.GetDay()
        IO.OutputText("Ziua de sfarsit: ")
        stopDay = IO.GetDay()
        Expenses.repo = Commands.EraseExpensesForTimePeriod(Expenses.repo, startDay, stopDay)
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def EraseAllExpensesOfGivenCategory():
    """
    erases all expenses of the given category
    """
    try:
        Expenses.repo = Commands.EraseAllExpensesOfGivenCategory(Expenses.repo, IO.GetCategory())
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def SearchExpensesGreaterThanAmmount():
    """
    searches for expenses greater than a given ammount
    """
    try:
        expenses = Commands.SearchExpensesGreaterThanAmmount(Expenses.repo, IO.GetAmmount())
        if expenses == Repo.MakeRepo():
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
        expenses = Commands.SearchExpensesBeforeGivenDayAndLessThanAmmount(Expenses.repo, IO.GetDay(), IO.GetAmmount())
        if expenses == Repo.MakeRepo():
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
        expenses = Commands.SearchAllExpensesOfGivenCategory(Expenses.repo, IO.GetCategory())
        if expenses == Repo.MakeRepo():
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def TotalAmmountForGivenCategory():
    """
    gets the total ammount for the given category
    """
    try:
        totalAmmount = Commands.TotalAmmountForGivenCategory(Expenses.repo, IO.GetCategory())
        if totalAmmount == 0:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            IO.OutputText("Suma totala ceruta este: " + str(totalAmmount))
    except Exception as ex:
        IO.OutputException(ex)

def DayWithGreatestAmmount():
    """
    gets the day with the greatest ammount
    """
    try:
        day = Commands.DayWithGreatestAmmount(Expenses.repo)
        if day == None:
            IO.OutputText("Lista de cheltuieli este goala!")
        else:
            IO.OutputText("Ziua ceruta este: " + str(day))
    except Exception as ex:
        IO.OutputException(ex)

def ExpensesWithGivenAmmount():
    """
    gets all expenses with the given ammount
    """
    try:
        expenses = Commands.ExpensesWithGivenAmmount(Expenses.repo, IO.GetAmmount())
        if expenses == Repo.MakeRepo():
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def ExpensesSortedByCategory():
    """
    gets all expenses sorted by category
    """
    try:
        expenses = Commands.ExpensesSortedByCategory(Expenses.repo)
        if expenses == {}:
            IO.OutputText("Nici o cheltuiala in lista!")
            return
        IO.OutputText("Cheltuielile cerute sunt: ")
        for expense in expenses:
            IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def WithoutExpensesOfGivenCategory():
    """
    gets all expenses without the given category
    """
    try:
        expenses = Commands.WithoutExpensesOfGivenCategory(Expenses.repo, IO.GetCategory())
        if expenses == Repo.MakeRepo():
            IO.OutputText("Nici o cheltuiala corespunzatoare")
        else:
            IO.OutputText("Cheltuielile cerute sunt: ")
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def WithoutExpensesLessThanGivenAmmount():
    """
    gets all expenses greater or equal with the given ammount
    """
    try:
        expenses = Commands.WithoutExpensesLessThanGivenAmmount(Expenses.repo, IO.GetAmmount())
        if expenses == Repo.MakeRepo():
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
            return
        for expense in expenses:
            IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def UndoLastOperation():
    """
    undo the last operation
    """
    try:
        Commands.UndoLastOperation()
        IO.OperationSuccesful()
    except Exception as ex:
        IO.OutputException(ex)

def ExitApplication():
    """
    exits the application
    """
    IO.OutputText("Iesire din aplicatie...")
    Commands.ExitApplication()

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