import Commands

def RunAllTests():
    Test_MakeCommand()

def Test_MakeCommand():
    assert Commands.MakeCommand('1') == 1
    assert Commands.MakeCommand(2) == 2
    try:
        Commands.MakeCommand("#")
        assert False
    except:
        assert True
    try:
        Commands.MakeCommand("#hj1b23fou")
        assert False
    except:
        assert True