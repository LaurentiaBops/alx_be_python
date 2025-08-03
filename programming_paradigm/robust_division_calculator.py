#Division calculator that robustly handles errors

def safe_divide(numerator, denominator):
    #Error for division by zero
    try:
        result = float(float(numerator)/float(denominator))
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."



