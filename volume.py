def vol(n):
    if (type(n) is str):
        return "Numbers only"

    if (n <= 0):
        return "Positive numbers only"
    
    return n * n * n