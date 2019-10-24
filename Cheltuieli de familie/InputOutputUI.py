import GraphicalUI
import Validation
import Commands
import Repo

def GetCommand():
    """
    gets the command inputed by the user
    :return: a command as integer value
    """
    value = input("Introduceti o comanda: ")
    GraphicalUI.EmptyLine()
    try:
        command = Commands.MakeCommand(value)
    except Exception as ex:
        print(ex)
        command = GetCommand()
    return command

def GetValue(outputText, valueType):
    """
    gets input from the user as type
    :param outputText: the text to be outputed
    :param type: the type of the input value
    :return: the value as type
    :raises: exception if value is not of the according type
    """
    try:
        value = valueType(input(outputText))
        Validation.ValidateValue(value, valueType)
        return value
    except Exception as ex:
        print(ex)
        return GetValue(outputText, valueType)

def GetExpense():
    """
    gets an expense inputed by the user
    :return: an expense as a list of values
    """
    day = GetValue("Introduceti ziua: ", int)
    ammount = GetValue("Introduceti suma: ", float)
    expenseType = GetValue("Introduceti tipul cheltuielii: ", str)
    GraphicalUI.EmptyLine()
    return Repo.MakeExpense(day, ammount, expenseType)
        
def ShowExpenses(expensesList):
    """
    prints a list of expenses
    :param expensesList: a list of expenses
    :return: nothing
    """
    print("Cheltuielile cerute sunt: ")
    for expense in expensesList:
        print(expense)

def ShowValue(value):
    """
    prints a value
    :param value: a value of any type
    :return: nothing
    """
    print("Valoarea ceruta este: \n" + str(value))