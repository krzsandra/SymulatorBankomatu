# Press the green button in the gutter to run the script.
def check_pin():
    # pin =  sample pin
    pin = int(1234)
    pincorect = False
    trials = 0
    while trials < 3:
        clientpin = int(input("W celu wykonania opecaji podaj 4 cyfrowy pin:"))
        trials += 1
        if clientpin == pin:
            print("Pin Poprawny")
            pincorect = True
            break
        elif trials == 3:
            break
        else:
            print("spróbuj ponownie")
    return pincorect


#         code here

if __name__ == '__main__':
    print("Witaj w symulatorze bankomatu ")
    if check_pin():
        pass
    else:
        print("zablokowany")
