from UI import Graphics
import Repo
import Expenses
import Validator

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
    Graphics.Display("ziua: " + str(expense.get("day")) + '\n' +
                    "suma: " + str(expense.get("ammount")) + '\n' +
                    "tipul cheltuielii: " + expense.get("category"))
    Graphics.EmptyLine()

def OperationSuccesful():
    """
    outputs succesful operation
    """
    Graphics.Display("Operatie reusita!")

def GetCommand():
    """
    gets a command
    
    Returns:
        str: a command
    """
    command = Input("Introduceti comanda dorita: ")
    return command

def GetCommandId():
    """
    gets a command id from the user
    
    Returns:
        int: a valid command id
    """
    commandId = Input("Introduceti numarul comenzii dorite: ")
    try:
        Validator.ValidateCommandId(commandId)
        return commandId
    except Exception as ex:
        OutputException(ex)
        return GetCommandId()

def GetExpense():
    """
    gets an expense from the user
    
    Returns:
        dictionary: an expense
    """
    OutputText("Introduceti cheltuiala dorita: ")
    try:
        day = int(Input("Ziua: "))
        ammount = float(Input("Suma: "))
        category = str(Input("Tipul cheltuielii: "))
        expense = Expenses.MakeExpense(day, ammount, category)
        Validator.ValidateExpense(expense)
        return expense
    except Exception as ex:
        OutputException(ex)
        return GetExpense()

def GetDay():
    """
    gets a day from the user
    
    Returns:
        int: a day
    """
    try:
        day = int(Input("Introduceti ziua dorita: "))
        return day
    except Exception as ex:
        OutputException(ex)

def GetAmmount():
    """
    gets an ammount from the user
    
    Returns:
        float: an ammount
    """
    try:
        ammount = float(Input("Introduceti suma dorita: "))
        return ammount
    except Exception as ex:
        OutputException(ex)

def GetCategory():
    """
    gets a category from the user
    
    Returns:
        str: a category
    """
    try:
        category = str(Input("Introduceti tipul de cheltuielii dorit: "))
        return category
    except Exception as ex:
        OutputException(ex)