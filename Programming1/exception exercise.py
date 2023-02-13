def readposint(integer):
    try:
        integer = int(integer)
    except ValueError:
        print("This is not a number")

    else:
        if integer <= 0:
            print("This is not a positive integer")
        else:
            print("Thank you!")



def main():
    try:
        readposint()

    except TypeError:
        print("You didn't enter anything!")


main()
