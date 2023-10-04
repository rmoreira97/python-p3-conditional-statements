#!/usr/bin/env python3

def admin_login(username, password):
    if (username.upper() == "ADMIN" and password == "12345"):
        return "Access granted"
    else :
        return "Access denied"
    

    pass

def hows_the_weather(temperature):
    if temperature == 33:
        response = "brisk"
    elif temperature == 55:
        response = "a little chilly"
    elif temperature == 99:
        response = "too dang hot"
    else:
        response = "perfect"
    
    return f"It's {response} out there!"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    

def calculator(operation, num1, num2):
    switcher = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
    }
    
    result = switcher.get(operation)
    if result is None:
        print("Invalid operation!")
        return None
    
    return result


