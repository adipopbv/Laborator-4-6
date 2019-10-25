from Cheltuieli_de_familie_rework.UI import IO
from Cheltuieli_de_familie_rework.UI import Graphics
from Cheltuieli_de_familie_rework import Commands

from Cheltuieli_de_familie_rework.Tests import Test_Repo
from Cheltuieli_de_familie_rework.Tests import Test_Expenses
from Cheltuieli_de_familie_rework.Tests import Test_Validator

def RunAllTests():
    """
    runs all asserting tests in the project
    """
    Test_Repo.RunAllTests()
    Test_Expenses.RunAllTests()
    Test_Validator.RunAllTests()

def RunApplication():
    """
    main loop holder
    shows the menu, gets and executes a command every iteration
    """
    while True:
        Graphics.DisplayMenu()
        commandId = IO.GetCommandId()
        Commands.DoCommandWithId(commandId)

RunAllTests()
RunApplication()