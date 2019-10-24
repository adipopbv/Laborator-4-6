import Repo

def RunAllTests():
    Test_MakeExpense()
    Test_IndexOf()
    Test_ExpenseGreaterThanAmmount()
    Test_AddExpenseToList()
    Test_ReplaceExpense()
    Test_GetAllExpensesGreaterThanAmmount()
    Test_GetTotalAmmountForExpenseType()
    Test_EraseAllWithGivenExpenseType()

#---------------

def Test_MakeExpense():
    assert Repo.MakeExpense(2,3,"mancare") == [0,2,3,"mancare"]

def Test_IndexOf():
    expenseList = [[0,2,3,"altele"], [1,3,56.4,"haine"]]
    assert Repo.IndexOf(expenseList, [0,2,3,"altele"]) == 0
    try:
        Repo.IndexOf(expenseList, [1,4,5,"ceva"])
        assert False
    except:
        assert True

def Test_ExpenseGreaterThanAmmount():
    assert Repo.ExpenseGreaterThanAmmount([0,2,3,"altele"], 2) == True
    assert Repo.ExpenseGreaterThanAmmount([0,2,3,"altele"], 3) == False

#---------

def Test_AddExpenseToList():
    expensesList = []
    Repo.AddExpenseToList(expensesList, [0,2,3,"altele"])
    assert expensesList == [[0,2,3,"altele"]]

def Test_ReplaceExpense():
    expense1 = [0,1,2,"3"]
    expense3 = [1,2,3,"4"]
    expense2 = [2,3,4,"5"]
    expensesList = [expense1, expense2]
    Repo.ReplaceExpense(expensesList, expense2, expense3)
    assert expensesList == [expense1, expense3]
    try:
        Repo.ReplaceExpense(expensesList, [1,2,3,"7"], expense2)
        assert False
    except:
        assert True

def Test_GetAllExpensesGreaterThanAmmount():
    expensesList = [[0,1,2,"3"],[2,3,4,"5"]]
    assert Repo.GetAllExpensesGreaterThanAmmount(expensesList,3.0) == [[2,3,4,"5"]]
    try:
        Repo.GetAllExpensesGreaterThanAmmount(expensesList, 10.0)
        assert False
    except:
        assert True

def Test_GetTotalAmmountForExpenseType():
    expensesList = [[0,1,2,"3"],[2,3,4,"5"]]
    assert Repo.GetTotalAmmountForExpenseType(expensesList, "5") == 4.0
    try:
        Repo.GetTotalAmmountForExpenseType(expensesList, "6")
        assert False
    except:
        assert True

def Test_EraseAllWithGivenExpenseType():
    expensesList = [[0,1,2,"3"],[2,3,4,"5"]]
    Repo.EraseAllWithGivenExpenseType(expensesList, "3")
    assert expensesList == [[2,3,4,"5"]]
    try:
        Repo.EraseAllWithGivenExpenseType(expensesList, "4")
        assert False
    except:
        assert True