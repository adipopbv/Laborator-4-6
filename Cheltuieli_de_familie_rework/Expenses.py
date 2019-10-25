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

