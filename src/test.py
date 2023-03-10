from main import add, mult

number1 = 12
number2 = 2 
assert add(number1, number2) == number2 + number1, f"numbers are not equal"

number1 = 122
number2 = 12 
assert add(number1, number2) == number2 + number1, f"numbers are not equal"


number1 = 121
number2 = 5 
assert add(number1, number2) == number2 + number1, f"numbers are not equal"

assert mult(19, 3) == 19 * 3, "mult is not right"
assert mult(193, 32) == 193 * 32, "mult is not right"
