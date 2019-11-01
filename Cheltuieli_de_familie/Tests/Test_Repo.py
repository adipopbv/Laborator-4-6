import Repo
import Expenses

def RunAllTests():
    Test_MakeRepo()
    Test_IndexOfItemInRepo()
    Test_AddToRepo()
    Test_RemoveFromRepo()
    Test_SwapInRepo()
    Test_CloneRepo()

def Test_MakeRepo():
    repo = Repo.MakeRepo(Expenses.MakeExpense(2,3,"4"), Expenses.MakeExpense(3,4,"5"))
    assert repo == [Expenses.MakeExpense(2,3,"4"), Expenses.MakeExpense(3,4,"5")]
    assert not repo == [Expenses.MakeExpense(3,34,"6")]

def Test_IndexOfItemInRepo():
    repo = [0, 1]
    assert Repo.IndexOfItemInRepo(repo, 0) == 0
    try:
        Repo.IndexOfItemInRepo(repo, 2)
        assert False
    except:
        assert True

def Test_AddToRepo():
    repo = [0, 1]
    Repo.AddToRepo(repo, 2)
    assert repo[2] == 2

def Test_RemoveFromRepo():
    repo = [0, 1]
    Repo.RemoveFromRepo(repo, 1)
    assert repo == [0]

def Test_SwapInRepo():
    repo = [0, 2]
    Repo.SwapInRepo(repo, 2, 1)
    assert repo == [0, 1]

def Test_CloneRepo():
    var1 = [0,1]
    var2 = [2,3]
    repo = [var1, var2]
    newRepo = Repo.CloneRepo(repo)
    assert newRepo == repo
    newRepo[1] = [4,5]
    assert not newRepo == repo