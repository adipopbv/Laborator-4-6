import Commands
import Expenses
import Repo

def RunAllTests():
    Test_AddNewExpense()
    Test_UpdateExpense()
    Test_EraseAllExpensesForGivenDay()
    Test_EraseExpensesForTimePeriod()
    Test_EraseAllExpensesOfGivenCategory()
    Test_SearchExpensesGreaterThanAmmount()
    Test_SearchExpensesBeforeGivenDayAndLessThanAmmount()
    Test_SearchAllExpensesOfGivenCategory()
    Test_TotalAmmountForGivenCategory()
    Test_DayWithGreatestAmmount()
    Test_ExpensesWithGivenAmmount()
    Test_ExpensesSortedByCategory()
    Test_WithoutExpensesOfGivenCategory()
    Test_WithoutExpensesLessThanGivenAmmount()

def Test_AddNewExpense():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo()
    Commands.AddNewExpense(repo, expense1)
    assert repo == Repo.MakeRepo(expense1)
    assert not repo == Repo.MakeRepo(expense2)

def Test_UpdateExpense():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1)
    Commands.UpdateExpense(repo, expense1, expense2)
    assert repo == Repo.MakeRepo(expense2)
    assert not repo == Repo.MakeRepo(expense1)

def Test_EraseAllExpensesForGivenDay():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    repo = Commands.EraseAllExpensesForGivenDay(repo, 2)
    assert repo == Repo.MakeRepo(expense2)
    assert not repo == Repo.MakeRepo(expense1, expense2)

def Test_EraseExpensesForTimePeriod():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    repo = Commands.EraseExpensesForTimePeriod(repo, 1, 2)
    assert repo == Repo.MakeRepo(expense2)
    assert not repo == Repo.MakeRepo()

def Test_EraseAllExpensesOfGivenCategory():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    repo = Commands.EraseAllExpensesOfGivenCategory(repo, "altele")
    assert repo == Repo.MakeRepo(expense2)
    assert not repo == Repo.MakeRepo(expense1)

def Test_SearchExpensesGreaterThanAmmount():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.SearchExpensesGreaterThanAmmount(repo, 3.0) == Repo.MakeRepo(expense2)
    assert not Commands.SearchExpensesGreaterThanAmmount(repo, 3.0) == Repo.MakeRepo()

def Test_SearchExpensesBeforeGivenDayAndLessThanAmmount():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.SearchExpensesBeforeGivenDayAndLessThanAmmount(repo, 3, 5.0) == Repo.MakeRepo(expense1)
    assert not Commands.SearchExpensesBeforeGivenDayAndLessThanAmmount(repo, 3, 5.0) == Repo.MakeRepo(expense2)

def Test_SearchAllExpensesOfGivenCategory():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.SearchAllExpensesOfGivenCategory(repo, "altele") == Repo.MakeRepo(expense1)
    assert not Commands.SearchAllExpensesOfGivenCategory(repo, "altele") == Repo.MakeRepo(expense2)

def Test_TotalAmmountForGivenCategory():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.TotalAmmountForGivenCategory(repo, "altele") == 3.0
    assert not Commands.TotalAmmountForGivenCategory(repo, "altele") == 7.0

def Test_DayWithGreatestAmmount():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.DayWithGreatestAmmount(repo) == 3
    assert not Commands.DayWithGreatestAmmount(repo) == 2

def Test_ExpensesWithGivenAmmount():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.ExpensesWithGivenAmmount(repo, 4.0) == Repo.MakeRepo(expense2)
    assert not Commands.ExpensesWithGivenAmmount(repo, 4.0) == Repo.MakeRepo(expense1)

def Test_ExpensesSortedByCategory():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.ExpensesSortedByCategory(repo) == Repo.MakeRepo(expense1,expense2)
    assert not Commands.ExpensesSortedByCategory(repo) == Repo.MakeRepo(expense2,expense1)
    
def Test_WithoutExpensesOfGivenCategory():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.WithoutExpensesOfGivenCategory(repo, "mancare") == Repo.MakeRepo(expense1)
    assert not Commands.WithoutExpensesOfGivenCategory(repo, "mancare") == Repo.MakeRepo(expense2)
    
def Test_WithoutExpensesLessThanGivenAmmount():
    expense1 = Expenses.MakeExpense(2,3.0,"altele")
    expense2 = Expenses.MakeExpense(3,4.0,"mancare")
    repo = Repo.MakeRepo(expense1, expense2)
    assert Commands.WithoutExpensesLessThanGivenAmmount(repo, 4.0) == Repo.MakeRepo(expense2)
    assert not Commands.WithoutExpensesLessThanGivenAmmount(repo, 4.0) == Repo.MakeRepo(expense1)









