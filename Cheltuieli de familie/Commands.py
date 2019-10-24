import Validation
import InputOutputUI
import Repo

def MakeCommand(value):
    """
    makes an input value to a command
    :param inputValue: value to be transformed
    :return: a command
    """
    try:
        Validation.ValidateCommand(value)
        command = int(value)
        return command
    except Exception as ex:
        raise Exception(ex)

def DoCommand(command):
    """
    executes the given command
    :param command: a command
    :return: nothing
    """
    if command == 1:
        AddNewExpense()
    elif command == 2:
        UpdateExpense()
    elif command == 6:
        AllExpensesGreaterThanAmmount()
    elif command == 9:
        TotalAmmountForExpenseType()
    elif command == 13:
        EraseAllWithGivenExpenseType()
    elif command == 16:
        ExitApplication()

#------------------------------------

def AddNewExpense():
    """
    adds a new expense in the expenses list
    :return: nothing
    """
    try:
        expense = InputOutputUI.GetExpense()
        Validation.ValidateExpense(expense)
        Repo.AddExpenseToList(Repo.expensesRepository, expense)
    except Exception as ex:
        print(ex)

def UpdateExpense():
    """
    updates an expense form the list of expenses
    :return: nothing
    """
    try:
        print("Cheltuiala de schimbat:")
        expense = InputOutputUI.GetExpense()
        Validation.ValidateExpense(expense)
        print("Cheltuiala sub forma actualizata:")
        updatedExpense = InputOutputUI.GetExpense()
        Validation.ValidateExpense(updatedExpense)
        Repo.ReplaceExpense(Repo.expensesRepository, expense, updatedExpense)
    except Exception as ex:
        print(ex)

def AllExpensesGreaterThanAmmount():
    """
    gets all expenses greater than a given ammount
    :return: nothing
    """
    try:
        givenAmmount = InputOutputUI.GetValue("Introduceti suma: ", float)
        Validation.ValidateValue(givenAmmount, float)
        expensesList = Repo.GetAllExpensesGreaterThanAmmount(Repo.expensesRepository, givenAmmount)
        InputOutputUI.ShowExpenses(expensesList)
    except Exception as ex:
        print(ex)

def TotalAmmountForExpenseType():
    """
    gets the total ammount for expenses with a given type
    :return: nothing
    """
    try:
        expenseType = InputOutputUI.GetValue("Introduceti tipul cheltuielii: ", str)
        totalAmmount = Repo.GetTotalAmmountForExpenseType(Repo.expensesRepository, expenseType)
        InputOutputUI.ShowValue(totalAmmount)
    except Exception as ex:
        print(ex)

def EraseAllWithGivenExpenseType():
    """
    erases all of the expenses that are of the given type
    :return: nothing
    """
    try:
        expenseType = InputOutputUI.GetValue("Introduceti tipul cheltuielii: ", str)
        Repo.EraseAllWithGivenExpenseType(Repo.expensesRepository, expenseType)
    except Exception as ex:
        print(ex)

def ExitApplication():
    """
    exits the application
    :return: nothing
    """
    print("Iesire din aplicatie...")
    exit()