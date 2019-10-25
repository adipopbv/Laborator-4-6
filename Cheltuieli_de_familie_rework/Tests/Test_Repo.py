import Repo

def RunAllTests():
    Test_IndexOfItemInRepo()
    Test_AddToRepo()
    Test_SwapInRepo()

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