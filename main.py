# Press the green button in the gutter to run the script.
def check_pin():
    # pin =  sample pin
    pin = int(1234)
    pincorect = False
    trials = 0
    while trials < 3:
        clientpin = int(input("W celu wykonania operacji podaj cztero cyfrowy PIN:"))
        trials += 1
        if clientpin == pin:
            print("PIN poprawny, wybierz operację jaką chcesz wykonać:")
            pincorect = True
            break
        elif trials == 3:
            break
        else:
            print("PIN niepoprawny, spróbuj ponownie")
    return pincorect


def operation_selection():
    selectedoperation = int(
        input("\nWypłata gotówki wprowadź '1'\nWyświetlenie stanu konta wprowadź '2'\nWyjście z SYMULATORA BANKOMATU '3'\n:"))
    return selectedoperation

def cash_withdrawal():
    multiple = 1
    while multiple > 0:
        paycheck = int(input("Proszę wprowadzić kwotę do wypłaty:"))
        multiple = (paycheck % 50)
        if multiple == 0:
            if paycheck <= accountbalans:
                if paycheck <= atmstate:
                    nrofbanknotes200 = paycheck // 200
                    nrofbanknotes100 = (paycheck - (200 * nrofbanknotes200)) // 100
                    nrofbanknotes50 = (paycheck - (200 * nrofbanknotes200) - (100 * nrofbanknotes100)) // 50
                    print("Wypłacasz kowotę:",paycheck,"\nOtrzymujesz:","\n",nrofbanknotes200,"banknot(ów) o nominale 200 PLN","\n", nrofbanknotes100, "banknot(ów) o nominale 100 PLN", "\n", nrofbanknotes50,"banknot(ów) o nominale 50 PLN")

                else:
                    print("Brak środków w SYMULATORZE BANKOMATU \nZapraszamy ponownie")

            else:
                print("Brak środków na koncie \nZapraszamy ponownie")

        else:
            print("Błędna kwota. Wprowadzona kwota musi być wielokrotnością liczby 50.")
    return

#         code here

if __name__ == '__main__':
    accountbalans = 550
    atmstate = 1000
    print("Witaj w SYMULATORZE BANKOMATU")
    if check_pin():
        selectedoperation = 4
        while selectedoperation > 3 or selectedoperation <= 0:
            selectedoperation = operation_selection()
            if selectedoperation == 1:
                 cash_withdrawal()
                 break
            elif selectedoperation == 2:
                accountbalans = 550
                print("Twój stan konta wynosi:{accountbalans}".format(accountbalans=accountbalans))
                break
            elif selectedoperation == 3:
                print("Dziękujemy, zapraszamy ponownie")
                break

            else:
                print("Nie wybrano poprawnej operacji, spróbuj ponownie:")

    else:
        print("Użytkownik zablkowany. Dziękujemy, zapraszamy ponownie")







