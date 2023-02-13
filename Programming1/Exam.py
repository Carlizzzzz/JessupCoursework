first_time = True


def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def divide(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print("You shall not divide a number by zero")
        exit()


def main(result, first_time):
    startWithSymbol = False
    formula = input("Type the formula, type end to end the program.\n")

    if formula.strip() == "end":    # end program
        exit()

    for i in formula:               # Check if there is sth not related to math
        if i not in "1234567890+-*x/. ":
            print("Invalid input")
            exit()

    formulaArray = formula.split()  # Break down the formula

    if formulaArray[0] in "+-*/x":  # See if the formula start with symbol
        if first_time:              # If it start with symbol but without previous result, it is not ok
            print("Invalid input")
            exit()
        else:
            startWithSymbol = True

    if startWithSymbol:
        if formulaArray[0] == "+":
            result = addition(result, formulaArray[1])
        elif formulaArray[0] == "-":
            result = subtraction(result, formulaArray[1])
        elif formulaArray[0] == "*" or "x":
            result = multiply(result, formulaArray[1])
        else:
            result = divide(result, formulaArray[1])
    else:
        if formulaArray[1] == "+":
            result = addition(formulaArray[0], formulaArray[2])
        elif formulaArray[1] == "-":
            result = subtraction(formulaArray[0], formulaArray[2])
        elif formulaArray[1] == "*" or "x":
            result = multiply(formulaArray[0], formulaArray[2])
        else:
            result = divide(formulaArray[0], formulaArray[2])

    print(result)
    first_time = False
    main(result, first_time)


main(0, True)
