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
        Graphics.DisplayStart()
        menuType = IO.GetCommandId()
        if menuType == "1":
            Graphics.DisplayMenu1()
            commandId = IO.GetCommandId()
            Service.DoFunctionalityWithId(commandId)
        elif menuType == "2":
            Graphics.DisplayMenu2()
            command = IO.GetCommand()
            command.split()
            Service.DoCommand(command)

RunAllTests()
RunApplication()

# adauga 1, 2, apa
# 4 comenzi de genul asta