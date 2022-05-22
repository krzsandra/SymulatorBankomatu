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
            print("Pin Poprawny, Wybierz opcje")
            pincorect = True
            break
        elif trials == 3:
            break
        else:
            print("spróbuj ponownie")
    return pincorect


def option():
    options = int(
        input("\nWypłata gotówki wprowadź '1'\nSprawdzenie stanu konta wprowadź '2'\nZakończenie wprowadź '3'\n:"))
    return options

def proba():
    payment = int(input("Proszę wprowadzic kwotę:"))
    multiple = (payment % 50)
    if multiple == 0:
        if payment <= accountbalans:
            if payment <= atmstate:
                cash200 = payment // 200
                cash100 = (payment - (200 * cash200)) // 100
                cash50 = (payment - (200 * cash200) - (100 * cash100)) // 50
                print(cash200, cash100, cash50)
            else:
                print("brak środków w atm")

        else:
            print("komunikat brak srodkow na koncie")

    else:
        print("błedna kwota")



#         code here

if __name__ == '__main__':
    accountbalans = 550
    atmstate = 1000
    print("Witaj w symulatorze bankomatu ")
    if check_pin():
        options = 4
        while options > 3 or options <= 0:
            options = option()

            if options == 1:
                 proba()
                 break
            elif options == 2:
                accountbalans = 550
                print("Twój stan konta wynosi:{accountbalans}".format(accountbalans=accountbalans))
                break
            elif options == 3:
                print("dziękujemy zapraszam ponownie")
                break

            else:
                print("Nie wybrano poprawnej opcji, spróbuj raz jeszcze")

    else:
        print("zablokowany")







