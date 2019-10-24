def ValidateCommand(command):
    """
    validates the command
    :param command: a command
    :return: nothing
    :raises: NotIntegerValueException if command is not an integer
    """
    try:
        command = int(command)
        if(command < 0):
            raise Exception("Valoare invalida!")
    except:
        raise Exception("Valoare invalida!")

def ValidateValue(value, valueType):
    """
    validates a value as valueType
    :param value: a value
    :param valueType: a variable type
    :return: nothing
    :raises: exception if value is not of valueType
    """
    try:
        value = valueType(value)
    except:
        raise Exception("Valoare invalida!")

def ValidateExpense(expense):
    """
    validates an expense
    :param expense: list of day, ammount, expense type
    :return: nothing
    :raises: exception if invalid expense
    """
    if type(expense[0]) == int and type(expense[1]) == int and type(expense[2]) == float and type(expense[3]) == str and len(expense) == 4:
        return
    raise Exception("Cheltuiala invalida!")