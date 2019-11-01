import Repo
import Expenses

def AddNewExpense(expense):
    """
    adds a new expense to the repository
    
    Args:
        expense (dict): an expense
    
    Raises:
        Exception: expense not added to the repo
    """
    try:
        Repo.AddToRepo(Expenses.repo, expense)
    except Exception as ex:
        raise Exception(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def UpdateExpense(originalExpense, updatedExpense):
    """
        updates an expense to a new state
    
    Args:
        originalExpense (dict): original expense
        updatedExpense (dict): updated expense
    
    Raises:
        Exception: expense not updated
    """
    try:
        Repo.SwapInRepo(Expenses.repo, originalExpense, updatedExpense)
    except Exception as ex:
       raise Exception(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def EraseAllExpensesForGivenDay(day):
    """
    erases expenses from the given day
    
    Args:
        day (int): a day
    
    Raises:
        Exception: expenses not erased
    """
    try:
        Expenses.repo = [expense for expense in Expenses.repo if not Expenses.SameDay(Expenses.Day(expense), day)]
    except Exception as ex:
        raise Exception(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def EraseExpensesForTimePeriod(startDay, stopDay):
    """
    erases all expenses from teh given time period
    
    Args:
        startDay (int): start day
        stopDay (int): stop day
    
    Raises:
        Exception: expenses not erased
    """
    try:
        Expenses.repo = [expense for expense in Expenses.repo if not (Expenses.Day(expense) >= startDay and Expenses.Day(expense) <= stopDay)]
    except Exception as ex:
        raise Exception(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def EraseAllExpensesOfGivenCategory(category):
    """
    erases all expenses from the given time period
    
    Args:
        category (str): a category
    
    Raises:
        Exception: expanses not erased
    """
    try:
        Expenses.repo = [expense for expense in Expenses.repo if not Expenses.SameCategory(Expenses.Category(expense), category)]
    except Exception as ex:
        raise Exception(ex)
    Repo.AddToRepo(Expenses.historyRepo, Repo.CloneRepo(Expenses.repo))

def SearchExpensesGreaterThanAmmount(ammount):
    """
    searches for expenses greater than a given ammount
    
    Args:
        ammount (float): an ammount
    
    Raises:
        Exception: no expenses greater than ammount
    
    Returns:
        list: list of expenses
    """
    try:
        expenses = [expense for expense in Expenses.repo if Expenses.GreaterAmmount(Expenses.Ammount(expense), ammount)]
        return expenses
    except Exception as ex:
        raise Exception(ex)

def SearchExpensesBeforeGivenDayAndLessThanAmmount(day, ammount):
    """
    searches all expense before a given day and less than a given ammount
    
    Args:
        day (int): a day
        ammount (float): an ammount
    
    Raises:
        Exception: no expenses with the given properties
    
    Returns:
        list: list of expenses
    """
    try:
        expenses = [expense for expense in Expenses.repo if Expenses.Day(expense) < day and Expenses.Ammount(expense) < ammount]
        return expenses
    except Exception as ex:
        raise Exception(ex)

def SearchAllExpensesOfGivenCategory(category):
    """
    searches all expenses of given category
    
    Args:
        category (str): a category
    
    Raises:
        Exception: no expenses of the given category
    
    Returns:
        list: list of expenses
    """
    try:
        expenses = [expense for expense in Expenses.repo if Expenses.SameCategory(Expenses.Category(expense), category)]
        return expenses
    except Exception as ex:
        raise Exception(ex)

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

def DayWithGreatestAmmount():
    """
    gets the day with the greatest ammount
    """
    try:
        day = None
        maxAmmount = -0.1
        for expense in Expenses.repo:
            if Expenses.Ammount(expense) > maxAmmount:
                maxAmmount = Expenses.Ammount(expense)
                day = Expenses.Day(expense)
        if day == None:
            IO.OutputText("Lista de cheltuieli este goala!")
        else:
            IO.OutputText("Ziua ceruta este: " + str(day))
    except Exception as ex:
        IO.OutputException(ex)

def ExpensesWithGivenAmmount():
    """
    gets expenses with the given ammount
    """
    try:
        ammount = IO.GetAmmount()
        expenses = [expense for expense in Expenses.repo if Expenses.SameAmmount(Expenses.Ammount(expense), ammount)]
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            for expense in expenses:
                IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def ExpensesSortedByCategory():
    """
    gets expenses sorted by category
    """
    try:
        category = lambda expense : expense["category"]
        expenses = sorted(Expenses.repo, key = category)
        if expenses == {}:
            IO.OutputText("Nici o cheltuiala in lista!")
            return
        IO.OutputText("Cheltuielile cerute sunt: ")
        for expense in expenses:
            IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def GetAllExpensesOfGivenCategory():
    """
    gets all expenses of given category
    """
    try:
        category = IO.GetCategory()
        expenses = [expense for expense in Expenses.repo if Expenses.SameCategory(Expenses.Category(expense), category)]
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
        else:
            for expense in expenses:
                IO.OutputExpense(expense)
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

def WithoutExpensesLessThanGivenAmmount():
    """
    removes all expenses less than the given ammount
    """
    try:
        ammount = IO.GetAmmount()
        expenses = [expense for expense in Expenses.repo if Expenses.Ammount(expense) >= ammount]
        if expenses == []:
            IO.OutputText("Nici o cheltuiala corespunzatoare!")
            return
        for expense in expenses:
            IO.OutputExpense(expense)
    except Exception as ex:
        IO.OutputException(ex)

def UndoLastOperation():

    try:
        Expenses.repo = Repo.CloneRepo(Expenses.historyRepo[-2])
        Repo.RemoveFromRepo(Expenses.historyRepo, Expenses.historyRepo[-1])
    except Exception as ex:
        IO.OutputException(ex)

def ExitApplication():

    IO.OutputText("Iesire din aplicatie...")
    exit()