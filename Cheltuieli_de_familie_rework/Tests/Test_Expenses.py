import Expenses

def RunAllTests():
    Test_MakeExpense()

def Test_MakeExpense():
    assert Expenses.MakeExpense(2,3.0,"altele") == {"day":2,"ammount":3.0,"category":"altele"}
