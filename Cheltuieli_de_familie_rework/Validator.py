def ValidateCommandId(commandId):
    """
    validates a command id
    
    Args:
        commandId (any type): a value to validate as command id
    
    Raises:
        Exception: command id not valid
    """
    try:
        commandId = int(commandId)
    except:
        raise Exception("Comanda invalida!")
    if (commandId < 1 or commandId > 16):
        raise Exception("Comanda invalida!")

def ValidateExpense(expense):
    """
    validates the given expense
    
    Args:
        expense (any type): a value to validate as expense
    
    Raises:
        Exception: expense not valid
    """
    if type(expense) != dict or type(expense["day"]) != int or type(expense["ammount"]) != float or type(expense["category"]) != str:
        raise Exception("Cheltuiala invalida!")