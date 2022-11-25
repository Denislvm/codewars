# Create a function which should a return number that the customers need to pay.
def sale_hotdogs(n):
    if n < 5:
        return 100*n
    elif n >= 5 and n < 10:
        return 95*n
    elif n >= 10:
        return 90*n