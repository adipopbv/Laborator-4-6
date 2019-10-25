import Graphics

def Input(promptText):
    """
    gets a value from the user via the console
    
    Args:
        promptText (str): text to be outputted before reading input
    
    Returns:
        any type: the value inputted by the user
    """
    Graphics.Display(promptText)
    inputValue = input()
    return inputValue

def OutputException(exceptionMessage):
    """
    prints the given exception message in the console
    
    Args:
        exceptionMessage (str): the exception text to be printed
    """
    Graphics.Display(exceptionMessage)

def OutputExpense(expense):
    """
    prints an expense in the console
    
    Args:
        expense (dictionary): an expense to be printed
    """
    Graphics.Display("id: " + str(expense.get("id")) + '\n',
                    "day: " + str(expense.get("day")) + '\n',
                    "ammount" + str(expense.get("ammount")) + '\n',
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
