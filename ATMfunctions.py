
def find_customer(idEntered, customerList):
    for client in customerList:
        if idEntered == client.idclient:
            return client
    return None


def check_pin(customer):
    pinCorrect = False
    trials = 0
    while trials < 3:
        pinEntered = int(input("W celu wykonania operacji podaj cztero cyfrowy PIN:"))
        trials += 1
        if pinEntered == customer.pin:
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


def is_withdrawal_amount_correct(withdrawal):
    return withdrawal > 0 and (withdrawal % 50) == 0


def money_on_the_clients_account_less_equal_than_withdrawal(withdrawal, customer):
    return withdrawal <= customer


def money_on_the_atm_state_higher_equal_than_withdrawal(withdrawal, atmBalance):
    return withdrawal <= atmBalance


def banknotes_to_be_given_to_clients(withdrawal):
    nrofbanknotes200 = withdrawal // 200
    nrofbanknotes100 = (withdrawal - (200 * nrofbanknotes200)) // 100
    nrofbanknotes50 = (withdrawal - (200 * nrofbanknotes200) - (100 * nrofbanknotes100)) // 50
    return nrofbanknotes200, nrofbanknotes100, nrofbanknotes50


def withdrawal_operation(customer,atmBalance):
    correct_withdrawal = False
    while correct_withdrawal is not True:
        withdrawalEntered = int(input("Proszę wprowadzić kwotę do wypłaty:"))
        correct_withdrawal = is_withdrawal_amount_correct(withdrawalEntered)
        if correct_withdrawal:
            if money_on_the_clients_account_less_equal_than_withdrawal(withdrawalEntered, customer.balance):
                if money_on_the_atm_state_higher_equal_than_withdrawal(withdrawalEntered, atmBalance):
                    banknotes = banknotes_to_be_given_to_clients(withdrawalEntered)
                    print("Otrzymujesz:\nLiczbę banknotów o nominale 200PLN:", banknotes[0],
                          "\nLiczbę banknotów o nominale 100PLN:", banknotes[1], "\nLiczbę banknotów o nominale 50PLN:",
                          banknotes[2])
                    break
                else:
                    print("Brak środków w bankomacie.")
                    break
            else:
                print("Brak środków na koncie.")
                break
        else:
            print("Niepoprawna kwota.\nKwota musi być wielokrotnością liczby 50")
    return correct_withdrawal