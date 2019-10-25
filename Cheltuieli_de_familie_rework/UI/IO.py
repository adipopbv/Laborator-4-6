from Cheltuieli_de_familie_rework.UI import Graphics
from Cheltuieli_de_familie_rework import Repo
from Cheltuieli_de_familie_rework import Expenses

def Input(promptText):
    """
    gets a value from the user via the console
    
    Args:
        promptText (str): text to be outputted before reading input
    
    Returns:
        any type: the value inputted by the user
    """
    OutputText(promptText)
    inputValue = input()
    return inputValue

def OutputText(text):
    """
    outputs a given text
    
    Args:
        text (str): the text to be outputted
    """
    Graphics.Display(text)

def OutputException(exceptionMessage):
    """
    outputs the given exception message
    
    Args:
        exceptionMessage (str): the exception text to be outputted
    """
    Graphics.Display(exceptionMessage)

def OutputExpense(expense):
    """
    outputs an expense
    
    Args:
        expense (dictionary): an expense to be outputted
    """
    Graphics.Display("id: " + str(expense.get("id")) + '\n' +
                    "day: " + str(expense.get("day")) + '\n' +
                    "ammount" + str(expense.get("ammount")) + '\n' +
                    "category: " + expense.get("category"))

def GetCommandId():
    """
    gets a command id from the user
    
    Returns:
        int: a valid command id
    """
    commandId = Input("Introduceti numarul comenzii dorite: ")
    try:
        #ValidateCommandId(commandId)
        return commandId
    except Exception as ex:
        OutputException(ex)
        return GetCommandId()

def GetExpense():

    OutputText("Introduceti cheltuiala dorita: ")
    try:
        day = Input("Ziua: ")
        ammount = Input("Suma: ")
        category = Input("Tipul cheltuielii: ")
        expense = Expenses.MakeExpense(day, ammount, category)
        #ValidateExpense(expense)
        return expense
    except Exception as ex:
        OutputException(ex)
        return GetExpense()
