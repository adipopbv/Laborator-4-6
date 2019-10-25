import IO
import Graphics

def RunAllTests():
    """
    runs all assertin tests in the project
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
        DoCommandWithId(commandId)