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
        if repoItem == item:
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

def SwapInRepo(repo, originalItem, updatedItem):
    """
    swaps a value in repo
    
    Args:
        repo (list): a repository
        originalItem (any type): the item to be swapped
        updatedItem (any type): the item to swap with
    
    Raises:
        Exception: item not present in repo
    """
    try:
        repo[IndexOfItemInRepo(repo, originalItem)] = updatedItem
    except Exception as ex:
        raise Exception(ex)