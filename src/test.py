from main import add

number1 = 12
number2 = 2 
assert add(number1, number2) == number2 + number1, f"numbers are not equal"

number1 = 122
number2 = 12 
assert add(number1, number2) == number2 + number1, f"numbers are not equal"


number1 = 121
number2 = 5 
assert add(number1, number2) == number2 + number1, f"numbers are not equal"
