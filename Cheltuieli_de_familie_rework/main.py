from Cheltuieli_de_familie_rework.UI import IO
from Cheltuieli_de_familie_rework.UI import Graphics
from Cheltuieli_de_familie_rework import Commands

def RunAllTests():
    """
    runs all asserting tests in the project
    """
    pass

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