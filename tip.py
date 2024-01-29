def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    onlynumber = ""
    for char in (d):
        if char.isdigit() or char == '.':
            onlynumber += char
    return float(onlynumber)



def percent_to_float(p):
    onlynumber = ""
    for char in (p):
        if char.isdigit() or char == '.':
            onlynumber += char
    return float(onlynumber) * 0.01
    



main()
