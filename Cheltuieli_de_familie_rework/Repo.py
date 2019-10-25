expenseRepo = []

def IndexOfItemInRepo(repo, item):
    """
    searches the index of an item in a repository
    
    Args:
        repo (list): a repository of items
        item (any type): an item to search
    
    Raises:
        Exception: inexistent item in repo
    
    Returns:
        int: index of item in repo
    """
    for repoItem in repo:
        if repoItem == repo:
            return repo.index(repoItem)
    raise Exception("Entitate inexistenta in lista!")

def AddToRepo(repo, item):
    """
    adds an item to a repository
    
    Args:
        repo (list): a repository to add to
        item (any type): an item to be added

    Raises:
        Exception: expense not found in repo
    """
    repo.append(item)

def SwapInRepo(repo, originalExpense, updatedExpense):

    try:
        expenseRepo[IndexOfItemInRepo(expenseRepo, originalExpense)] = updatedExpense
    except Exception as ex:
        raise Exception(ex)