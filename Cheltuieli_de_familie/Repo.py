def MakeRepo(*items):
    """
    makes a new repository
    
    Returns:
        list: a new repo
    """
    repo = []
    if len(items) > 0:
        if type(items[0]) == list:
            for item in items[0]:
                AddToRepo(repo, item)
            return repo
    for item in items:
        AddToRepo(repo, item)
    return repo

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
    """
    repo.append(item)

def RemoveFromRepo(repo, item):
    """
    removes an item from a repository
    
    Args:
        repo (list): a repo to remove from
        item (any type): an item to be removed
    """
    repo.remove(item)

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

def CloneRepo(repo):
    """
    clones a repo
    
    Args:
        repo (list): a repo
    
    Raises:
        Exception: any exception
    
    Returns:
        list: a copy of the repo
    """
    try:
        repoClone = []
        for item in repo:
            itemClone = item.copy()
            repoClone.append(itemClone)
        return repoClone
    except Exception as ex:
        raise Exception(ex)