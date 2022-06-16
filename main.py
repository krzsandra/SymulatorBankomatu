

def check_pin():
    pin = 1234
    pinCorrect = False
    trials = 0
    while trials < 3:
        clientPin = int(input("W celu wykonania operacji podaj cztero cyfrowy PIN:"))
        trials += 1
        if clientPin == pin:
            print("PIN poprawny")
            pinCorrect = True
            break
        elif trials == 3:
            break
        else:
            print("PIN niepoprawny, spróbuj ponownie")
    return pinCorrect


def operation_selection(operations_dict):
    print("Dostępne operacje")
    for option, description in operations_dict.items():
        print(option, description)
    selectedOperation = int(input("Wybierasz operację nr:"))
    return selectedOperation


def is_paycheck_amount_correct(paycheck):
    return paycheck > 0 and (paycheck % 50) == 0


def money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance):
    return paycheck <= accountBalance


def money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmBalance):
    return paycheck <= atmBalance


def banknotes_to_be_given_to_clients(paycheck):
    nrofbanknotes200 = paycheck // 200
    nrofbanknotes100 = (paycheck - (200 * nrofbanknotes200)) // 100
    nrofbanknotes50 = (paycheck - (200 * nrofbanknotes200) - (100 * nrofbanknotes100)) // 50
    return (nrofbanknotes200, nrofbanknotes100, nrofbanknotes50)




if __name__ == '__main__':
    WITHDRAW = 1
    BALANCE = 2
    END = 3

    operations_dict = {WITHDRAW: "Wypłata",
                       BALANCE: "Stan konta",
                       END: "Zakończ pracę z bankomatem"}

    accountBalance = 1550
    atmBalance = 1000
    print("Witaj w SYMULATORZE BANKOMATU")
    if check_pin():
        operationSelection = 4
        while operationSelection > 3 or operationSelection <= 0:
            operationSelection = operation_selection(operations_dict)
            if operationSelection == WITHDRAW:
                multiple = 1
                while multiple != 0:
                    paycheck = int(input("Proszę wprowadzić kwotę do wypłaty:"))
                    if is_paycheck_amount_correct(paycheck):
                        if money_on_the_clients_account_less_equal_than_paycheck(paycheck, accountBalance):
                            if money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmBalance):
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
            elif operationSelection == BALANCE:
                print("Twój stan konta wynosi", accountBalance)
                break
            elif operationSelection == END:
                print("Dziękujemy, zapraszamy ponownie")
                break
            else:
                print("Nie wybrano poprawnej operacji, spróbuj ponownie:")
    else:
        print("Użytkownik zablkowany. Dziękujemy, zapraszamy ponownie")







