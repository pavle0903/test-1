def bad_function():
    print("This function has an unused variable")
    unused_variable = 42  # SonarQube will flag this as a "Code Smell"

bad_function()

def execute_user_input():
    user_input = "print('This is insecure!')"  # Simulating user input
    eval(user_input)  # 🚨 SonarQube will flag this as a security vulnerability

execute_user_input()

def execute_user_inpuut():
    user_input = "print('This is insecure!')"  # Simulating user input
    eval(user_input)  # 🚨 SonarQube will flag this as a security vulnerability

execute_user_inpuut()
