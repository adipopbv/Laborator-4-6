import GraphicalUI
import InputOutputUI
import Commands

def RunApplication():
    """
    main loop holder
    :return: nothing
    """
    while True:
        GraphicalUI.ShowMenu()
        command = InputOutputUI.GetCommand()
        Commands.DoCommand(command)

from Tests import Test_Commands
from Tests import Test_Repo

def RunAllTests():
    """
    runs all assert tests for functions that return values
    :return: nothing
    """
    Test_Commands.RunAllTests()
    Test_Repo.RunAllTests()

RunAllTests()
RunApplication()