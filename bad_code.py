def bad_function():
    print("This function has an unused variable")
    unused_variable = 42  # SonarQube will flag this as a "Code Smell"

bad_function()
