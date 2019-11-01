from UI import IO
from UI import Graphics
import Service

from Tests import Test_Repo
from Tests import Test_Expenses
from Tests import Test_Validator
from Tests import Test_Commands

def RunAllTests():
    """
    runs all asserting tests in the project
    """
    Test_Expenses.RunAllTests()
    Test_Repo.RunAllTests()
    Test_Validator.RunAllTests()
    Test_Commands.RunAllTests()

def RunApplication():
    """
    main loop holder
    shows the menu, gets and executes a command every iteration
    """
    while True:
        Graphics.DisplayMenu()
        commandId = IO.GetCommandId()
        Service.DoFunctionalityWithId(commandId)

RunAllTests()
RunApplication()