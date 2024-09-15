# import module
# message=module.txt_greetings("Betrand")
# print(message)

def my_decorator(func):  # Outer function
    def wrapper():  # Inner function
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper  # Return the inner function

@my_decorator
def say_hello():  # The function being decorated
    print("Hello!")

say_hello()  # Calls the wrapper function, not the original function directly
