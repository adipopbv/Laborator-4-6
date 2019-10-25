import Repo

def RunAllTests():
    pass

def Test_AddToRepo():
    repo = [0,1]
    Repo.AddToRepo(repo, 2)
    assert repo[2] == 2
