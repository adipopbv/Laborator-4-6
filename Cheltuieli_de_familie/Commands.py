import Repo
import Expenses

def AddNewExpense(repo, expense):
    """
    adds a new expense to the repository
    
    Args:
        expense (dict): an expense
    
    Raises:
        Exception: expense not added to the repo
    """
    try:
        Repo.AddToRepo(repo, expense)
        return repo
    except Exception as ex:
        raise Exception(ex)

def UpdateExpense(repo, originalExpense, updatedExpense):
    """
        updates an expense to a new state
    
    Args:
        originalExpense (dict): original expense
        updatedExpense (dict): updated expense
    
    Raises:
        Exception: expense not updated
    """
    try:
        Repo.SwapInRepo(repo, originalExpense, updatedExpense)
        return repo
    except Exception as ex:
       raise Exception(ex)

def EraseAllExpensesForGivenDay(repo, day):
    """
    erases expenses from the given day
    
    Args:
        day (int): a day
    
    Raises:
        Exception: expenses not erased
    """
    try:
        expenses = [expense for expense in repo if not Expenses.SameDay(Expenses.Day(expense), day)]
        return Repo.MakeRepo(expenses)
    except Exception as ex:
        raise Exception(ex)

def EraseExpensesForTimePeriod(repo, startDay, stopDay):
    """
    erases all expenses from the given time period
    
    Args:
        startDay (int): start day
        stopDay (int): stop day
    
    Raises:
        Exception: expenses not erased
    """
    try:
        repo = Repo.MakeRepo(expense for expense in repo if not (Expenses.Day(expense) >= startDay and Expenses.Day(expense) <= stopDay))
        return repo
    except Exception as ex:
        raise Exception(ex)

def EraseAllExpensesOfGivenCategory(repo, category):
    """
    erases all expenses from the given time period
    
    Args:
        category (str): a category
    
    Raises:
        Exception: expanses not erased
    """
    try:
        repo = Repo.MakeRepo(expense for expense in repo if not Expenses.SameCategory(Expenses.Category(expense), category))
        return repo
    except Exception as ex:
        raise Exception(ex)

def SearchExpensesGreaterThanAmmount(repo, ammount):
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
        expenses = Repo.MakeRepo(expense for expense in repo if Expenses.GreaterAmmount(Expenses.Ammount(expense), ammount))
        return expenses
    except Exception as ex:
        raise Exception(ex)

def SearchExpensesBeforeGivenDayAndLessThanAmmount(repo, day, ammount):
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
        expenses = Repo.MakeRepo(expense for expense in repo if Expenses.Day(expense) < day and Expenses.Ammount(expense) < ammount)
        return expenses
    except Exception as ex:
        raise Exception(ex)

def SearchAllExpensesOfGivenCategory(repo, category):
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
        expenses = Repo.MakeRepo(expense for expense in repo if Expenses.SameCategory(Expenses.Category(expense), category))
        return expenses
    except Exception as ex:
        raise Exception(ex)

def TotalAmmountForGivenCategory(repo, category):
    """
    gets total ammount for a given expenses category
    
    Args:
        repo (list): a repository
        category (str): a category
    
    Raises:
        Exception: no expense with the given category
    
    Returns:
        int: total ammount
    """
    try:
        totalAmmount = 0
        for expense in repo:
            if Expenses.SameCategory(Expenses.Category(expense), category):
                totalAmmount += Expenses.Ammount(expense)
        return totalAmmount
    except Exception as ex:
        raise Exception(ex)

def DayWithGreatestAmmount(repo):
    """
    gets the day with the greatest ammount
    
    Args:
        repo (list): a repository
    
    Raises:
        Exception: no expense in repo
    
    Returns:
        int: day with greatest ammount
    """ 
    try:
        day = None
        maxAmmount = -0.1
        for expense in repo:
            if Expenses.Ammount(expense) > maxAmmount:
                maxAmmount = Expenses.Ammount(expense)
                day = Expenses.Day(expense)
        return day
    except Exception as ex:
        raise Exception(ex)

def ExpensesWithGivenAmmount(repo, ammount):
    """
    gets expenses with the given ammount
    
    Args:
        repo (list): a repository
        ammount (float): an ammount
    
    Raises:
        Exception: no expense in repo
    
    Returns:
        list: expenses with given ammount
    """
    try:
        expenses = Repo.MakeRepo(expense for expense in repo if Expenses.SameAmmount(Expenses.Ammount(expense), ammount))
        return expenses
    except Exception as ex:
        raise Exception(ex)

def ExpensesSortedByCategory(repo):
    """
    gets expenses sorted by category
    
    Args:
        repo (list): a repository
    
    Raises:
        Exception: no expense in repo
    
    Returns:
        list: sorted expenses by category
    """
    try:
        category = lambda expense : Expenses.Category(expense)
        expenses = sorted(repo, key = category)
        return expenses
    except Exception as ex:
        raise Exception(ex)

def WithoutExpensesOfGivenCategory(repo, category):
    """
    removes all expenses of given category
    
    Args:
        repo (list): a repo
        category (str): a category
    
    Raises:
        Exception: no expense in repo
    
    Returns:
        list: repo without expenses of the given category
    """
    try:
        expenses = Repo.MakeRepo()
        for expense in repo:
            if not Expenses.SameCategory(Expenses.Category(expense), category):
                expenses.append(expense)
        return expenses
    except Exception as ex:
        raise Exception(ex)

def WithoutExpensesLessThanGivenAmmount(repo, ammount):
    """
    removes all expenses less than the given ammount
    
    Args:
        repo (list): a repo
        ammount (float): an ammount
    
    Raises:
        Exception: no expense in repo
    
    Returns:
        list: repo without expenses less than given ammount
    """
    try:
        expenses = Repo.MakeRepo(expense for expense in repo if Expenses.Ammount(expense) >= ammount)
        return expenses
    except Exception as ex:
        raise Exception(ex)

def UndoLastOperation():
    """
    rewinds the repo to its state before the last operation
    
    Raises:
        Exception: no expense in repo
    """
    try:
        repo = Repo.CloneRepo(Expenses.historyRepo[-2])
        Repo.RemoveFromRepo(Expenses.historyRepo, Expenses.historyRepo[-1])
    except Exception as ex:
        raise Exception(ex)

def ExitApplication():
    """
    exits app
    """
    exit()