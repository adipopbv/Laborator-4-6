import Repo

def RunAllTests():
    Test_IndexOfItemInRepo()
    Test_AddToRepo()
    Test_RemoveFromRepo()
    Test_SwapInRepo()
    Test_CloneRepo()

def Test_IndexOfItemInRepo():
    repo = [
        {
            "day": 3,
            "ammount": 4.0,
            "category": "altele"
        }
    ]
    assert Repo.IndexOfItemInRepo(repo, {"day":3,"ammount":4.0,"category":"altele"}) == 0
    try:
        Repo.IndexOfItemInRepo(repo, {"day":1000,"ammount":40.0,"category":"aele"})
        assert False
    except:
        assert True

def Test_AddToRepo():
    repo = [0,1]
    Repo.AddToRepo(repo, 2)
    assert repo[2] == 2

def Test_RemoveFromRepo():
    repo = [0,1]
    Repo.RemoveFromRepo(repo, 1)
    assert repo == [0]

def Test_SwapInRepo():
    repo = [ 
        {
            "day": 2,
            "ammount": 3.0,
            "category": "altele"
        }
    ]
    Repo.SwapInRepo(repo, {"day":2,"ammount":3.0,"category":"altele"}, {"day":3,"ammount":4.0,"category":"altele"})
    assert repo == [{"day":3,"ammount":4.0,"category":"altele"}]

def Test_CloneRepo():
    repo = [ 
        {
            "day": 2,
            "ammount": 3.0,
            "category": "altele"
        }
    ]
    newRepo = Repo.CloneRepo(repo)
    assert newRepo == repo
    newRepo[0]["day"] = 3
    assert not newRepo == repo