import Expenses

def RunAllTests():
    Test_MakeExpense()
    Test_GreaterAmmount()
    Test_SameCategory()
    Test_Day()
    Test_Ammount()
    Test_Category()

def Test_MakeExpense():
    assert Expenses.MakeExpense(2,3.0,"altele") == {"day":2,"ammount":3.0,"category":"altele"}

def Test_GreaterAmmount():
    assert Expenses.GreaterAmmount(2, 3) == False
    assert Expenses.GreaterAmmount(3, 2) == True

def Test_SameCategory():
    assert Expenses.SameCategory("altele","altele") == True
    assert Expenses.SameCategory("lala","liiii") == False

def Test_Day():
    assert Expenses.Day({"day":3,"ammount":4,"category":"altele"}) == 3

def Test_Ammount():
    assert Expenses.Ammount({"day":3,"ammount":4,"category":"altele"}) == 4

def Test_Category():
    assert Expenses.Category({"day":3,"ammount":4,"category":"altele"}) == "altele"