expensesRepository = []

def MakeExpense(day, ammount, expenseType):
    """
    creates a new expense with a unique id
    :return: an expense
    """
    return [0, day, ammount, expenseType]

def IndexOf(expenseList, expense):
    """
    searches for the index of expense without id
    :param expenseList: a list of expense where to search in
    :param expense: an expense to be found
    :returns: index of the expense
    :raises: exception if no expense present in the list
    """
    for searchedExpense in expenseList:
        if expense[1] == searchedExpense[1] and expense[2] == searchedExpense[2] and expense[3] == searchedExpense[3]:
            return expenseList.index(searchedExpense)
    raise Exception("Cheltuiala inexistenta!")

def ExpenseGreaterThanAmmount(expense, givenAmmount):
    """
    tests the expense to have the ammount greater than a givenAmmount
    :param expense: an expense
    :param givenAmmount: an ammount
    :return: true/false
    """
    if expense[2] > givenAmmount:
        return True
    return False

#--------------------

def AddExpenseToList(expensesList, expense):
    """
    adds an expense to the repository
    :param expensesList: an expenses list
    :param expense: an expense
    :return: nothing
    """
    expense[0] = len(expensesList)
    expensesList.append(expense)

def ReplaceExpense(expensesList, expense, updatedExpense):
    """
    replaces expense with the updatedExpense
    :param expenseList: an expense list
    :param expense: an expense to be replaced
    :param updatedExpense: an expense to replace the other
    :return: nothing
    """
    try:
        index = IndexOf(expensesList, expense)
        updatedExpense[0] = expensesList[index][0]
        expensesList[index] = updatedExpense
    except Exception as ex:
        print(ex)

def GetAllExpensesGreaterThanAmmount(expensesList, givenAmmount):
    """
    gets all expenses greater than a givenAmmount
    :param expensesList: an expenses list
    :param givenAmmount: an ammount
    :return: a list of expenses
    :raises: exception if there are no expenses to be returned
    """
    expenses = []
    for expense in expensesList:
        if ExpenseGreaterThanAmmount(expense, givenAmmount):
            expenses.append(expense)
    if expenses == []:
        raise Exception("Nici o cheltuiala corespunzatoare!")
    return expenses

def GetTotalAmmountForExpenseType(expensesList, expenseType):
    """
    gets the total ammount for a given expense type
    :param expensesList: an expenses list
    :param expenseType: an expense type
    :return: the total ammount as float
    :raises: exception if there are no expenses of the given type
    """
    totalAmmount = 0
    for expense in expensesList:
        if expense[3] == expenseType:
            totalAmmount += expense[2]
    if totalAmmount == 0:
        raise Exception("Nici o cheltuiala corespunzatoare!")
    return totalAmmount

def EraseAllWithGivenExpenseType(expensesList, expenseType):
    """
    erases all expenses with the given expense type
    :param expensesList: an expenses list
    :param expenseType: an expense type
    :return: nothing
    :raises: exception if there is no expense of the given type
    """
    ok = False
    for expense in expensesList:
        if expense[3] == expenseType:
            ok = True
            expensesList.remove(expense)
    if ok == False:
        raise Exception("Nici o cheltuiala corespunzatoare!")
