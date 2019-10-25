def Input(promptText):
    """
    gets a value from the user via the console
    
    Args:
        promptText (str): text to be outputted before reading input
    
    Returns:
        any type: the value inputted by the user
    """
    inputValue = input(promptText)
    return inputValue

def Output(text):
    """
    prints the given text in the console
    
    Args:
        text (str): the text to be printed
    """
    print(text)

def OutputExpense(expense):
    """
    prints an expense in the console
    
    Args:
        expense (dictionary): an expense to be printed
    """
    print("id: " + str(expense.get("id")) + '\n',
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
        Output(ex)
        return GetCommandId()
