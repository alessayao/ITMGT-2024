def interest(principal, rate, periods):
    quantity = int((rate*periods)*principal)
    interest_total = int(quantity+principal)
    return interest_total