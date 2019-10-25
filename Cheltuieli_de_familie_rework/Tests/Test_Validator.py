from Cheltuieli_de_familie_rework import Validator

def RunAllTests():
    Test_ValidateCommandId()
    Test_ValidateExpense()

def Test_ValidateCommandId():
    try:
        Validator.ValidateCommandId("5")
        assert True
    except:
        assert False
    try:
        Validator.ValidateCommandId("-1")
        assert False
    except:
        assert True
    try:
        Validator.ValidateCommandId("%$#&")
        assert False
    except:
        assert True
    try:
        Validator.ValidateCommandId("60")
        assert False
    except:
        assert True

def Test_ValidateExpense():
    try:
        Validator.ValidateExpense({"day":2,"ammount":4.0,"category":"altele"})
        assert True
    except:
        assert False
    try:
        Validator.ValidateExpense("lala")
        assert False
    except:
        assert False
    try:
        Validator.ValidateExpense({"day":"ha","ammount":[],"category":0.0})
        assert False
    except:
        assert True