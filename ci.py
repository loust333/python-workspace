def compound_interest():
    principal = input("Please enter your initial deposit: $")
    rate = input("Please enter the expected interest rate: ")
    rate = rate/100
    time = input('Please enter the number of years it will be saved: ')
    time += 1
    compound = input('How many times is the interest compounded yearly?: ')

    print "Year %21s" % " amount on deposit"

    for time in range(1, time):
        formula = principal * (1.0 + rate)** time
        print "%4d%21.2f" % (time, formula)


def start():
    print "Let's start compounding your interest"
    compound_interest()

start()
