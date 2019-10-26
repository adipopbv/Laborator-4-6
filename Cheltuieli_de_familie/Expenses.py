repo = []

def MakeExpense(day, ammount, category):
    """
    creates and returns an expense
    
    Args:
        day (int): a day
        ammount (float): an ammount
        category (str): a category
    
    Returns:
        dictionary: an expense
    """
    return {"day": day, "ammount": ammount, "category": category}

def GreaterAmmount(firstAmmount, secondAmmount):
    """
    compares the 2 ammounts. if the first is greater it returns true
    
    Args:
        firstAmmount (float): first ammount
        secondAmmount (float): second ammount
    
    Returns:
        bool: true or false
    """
    if firstAmmount > secondAmmount:
        return True
    return False

def SameCategory(firstCategory, secondCategory):
    """
    compares the 2 categories. if they are the same it returns true
    
    Args:
        firstCategory (str): first category
        secondCategory (str): second category
    
    Returns:
        bool: true or false
    """
    if firstCategory == secondCategory:
        return True
    return False

def Day(expense):
    """
    gets the day of an expense
    
    Args:
        expense (dictionary): an expense
    
    Returns:
        int: a day
    """
    return expense["day"]

def Ammount(expense):
    """
    gets the ammount of an expense
    
    Args:
        expense (dictionary): an expense
    
    Returns:
        float: an ammount
    """
    return expense["ammount"]

def Category(expense):
    """
    gets the category of an expense
    
    Args:
        expense (dictionary): an expense
    
    Returns:
        str: a category
    """
    return expense["category"]

