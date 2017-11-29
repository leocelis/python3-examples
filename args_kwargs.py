# List
def test_var_args(farg, *args):
    print("formal arg:", farg)

    for arg in args:
        print("another arg:", arg)


test_var_args(1, "two", 3)


# Dict
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))


test_var_kwargs(farg=1, myarg2="two", myarg3=3)


# Calling a function - List
def test_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


args = ("two", 3)
test_var_args_call(1, *args)


# Calling a function - Dict
def test_var_args_call(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)
