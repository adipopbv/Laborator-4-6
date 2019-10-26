from UI import IO
from UI import Graphics
import Commands

from Tests import Test_Repo
from Tests import Test_Expenses
from Tests import Test_Validator

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