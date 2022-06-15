

def check_pin():
    pin = int(1234)
    pinCorrect = False
    trials = 0
    while trials < 3:
        clientPin = int(input("W celu wykonania operacji podaj cztero cyfrowy PIN:"))
        trials += 1
        if clientPin == pin:
            print("PIN poprawny, wybierz operację jaką chcesz wykonać:")
            pinCorrect = True
            break
        elif trials == 3:
            break
        else:
            print("PIN niepoprawny, spróbuj ponownie")
    return pinCorrect


def operation_selection():
    selectedOperation = int(input("\nWypłata gotówki wprowadź '1'\nWyświetlenie stanu konta wprowadź '2'\nWyjście z SYMULATORA BANKOMATU wprowadź'3'\n:"))
    return selectedOperation


def paycheck_is_a_multiple_of_50(paycheck):
    if paycheck > 0:
        return (paycheck % 50) == 0
    else:
        return False


def money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance):
    return paycheck <= accountBalance


def money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmState):
    return paycheck <= atmState


def banknotes_to_be_given_to_clients(paycheck):
    nrofbanknotes200 = paycheck // 200
    nrofbanknotes100 = (paycheck - (200 * nrofbanknotes200)) // 100
    nrofbanknotes50 = (paycheck - (200 * nrofbanknotes200) - (100 * nrofbanknotes100)) // 50
    return (nrofbanknotes200, nrofbanknotes100, nrofbanknotes50)




if __name__ == '__main__':
    accountBalans = 1550
    atmState = 1000
    print("Witaj w SYMULATORZE BANKOMATU")
    if check_pin():
        operationSelection = 4
        while operationSelection > 3 or operationSelection <= 0:
            operationSelection = operation_selection()
            if operationSelection == 1:
                multiple = 1
                while multiple != 0:
                    paycheck = int(input("Proszę wprowadzić kwotę do wypłaty:"))
                    if paycheck_is_a_multiple_of_50(paycheck):
                        if money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalans):
                            if money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmState):
                                banknotes = banknotes_to_be_given_to_clients(paycheck)
                                print("Otrzymujesz:\nLiczbę banknotów o nominale 200PLN:", banknotes[0], "\nLiczbę banknotów o nominale 100PLN:", banknotes[1], "\nLiczbę banknotów o nominale 50PLN:", banknotes[2])
                                break
                            else:
                                print("Brak środków w ATM")
                                break
                        else:
                            print("Brak środków na koncie")
                            break
                    else:
                        print("NIe poprawna kwota")
            elif operationSelection == 2:
                print("Twój stan konta wynosi", accountBalans)
                break
            elif operationSelection == 3:
                print("Dziękujemy, zapraszamy ponownie")
                break
            else:
                print("Nie wybrano poprawnej operacji, spróbuj ponownie:")
    else:
        print("Użytkownik zablkowany. Dziękujemy, zapraszamy ponownie")







