import re

def calculate(expression):
    expression = re.sub(r'[:/]', '/', expression)
    try:
        result = eval(expression.replace(" ", ""))
        return result
    except Exception as e:
        print(f"Error: {e}")
        return "Incorrect syntax for CALC"