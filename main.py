from customer import *


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


def is_paycheck_amount_correct(paycheck):
    return paycheck > 0 and (paycheck % 50) == 0


def money_on_the_clients_account_less_equal_than_paycheck(paycheck, customer):
    return paycheck <= customer


def money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmBalance):
    return paycheck <= atmBalance


def banknotes_to_be_given_to_clients(paycheck):
    nrofbanknotes200 = paycheck // 200
    nrofbanknotes100 = (paycheck - (200 * nrofbanknotes200)) // 100
    nrofbanknotes50 = (paycheck - (200 * nrofbanknotes200) - (100 * nrofbanknotes100)) // 50
    return (nrofbanknotes200, nrofbanknotes100, nrofbanknotes50)


def withdrawal_operation(customer):
    correct_paycheck = False
    while correct_paycheck is not True:
        paycheck = int(input("Proszę wprowadzić kwotę do wypłaty:"))
        correct_paycheck = is_paycheck_amount_correct(paycheck)
        if correct_paycheck:
            if money_on_the_clients_account_less_equal_than_paycheck(paycheck, customer.balance):
                if money_on_the_atm_state_higher_equal_than_paycheck(paycheck, atmBalance):
                    banknotes = banknotes_to_be_given_to_clients(paycheck)
                    print("Otrzymujesz:\nLiczbę banknotów o nominale 200PLN:", banknotes[0],
                          "\nLiczbę banknotów o nominale 100PLN:", banknotes[1], "\nLiczbę banknotów o nominale 50PLN:",
                          banknotes[2])
                    break
                else:
                    print("Brak środków w ATM")
                    break
            else:
                print("Brak środków na koncie")
                break
        else:
            print("Nie poprawna kwota")
    return correct_paycheck


if __name__ == '__main__':
    WITHDRAW = 1
    BALANCE = 2
    END = 3
    operations_dict = {WITHDRAW: "Wypłata",
                       BALANCE: "Stan konta",
                       END: "Zakończ pracę z bankomatem"}

    customer01 = Customer(10, 5236, 1500)
    customer02 = Customer(20, 1234, 150)
    customer03 = Customer(30, 7878, 2251)
    customer04 = Customer(40, 1546, 562)
    customer05 = Customer(50, 1234, 2250)
    customer06 = Customer(60, 5236, 250)
    customer07 = Customer(70, 4589, 50)
    customer08 = Customer(80, 2107, 140)
    customer09 = Customer(90, 1806, 850)
    customer10 = Customer(100, 5469, 150)

    customersList = [customer01, customer02, customer03, customer04, customer05, customer06, customer07, customer08, customer09 , customer10]

    atmBalance = 1000

    print("Witaj w SYMULATORZE BANKOMATU")
    idEntered = int(input("Proszę o podanie indentyfikatora klienta:"))
    customer = find_customer(idEntered,customersList)
    if customer:
        if check_pin(customer):
            operationSelection = 4
            while operationSelection > END or operationSelection <= 0:
                operationSelection = operation_selection(operations_dict)
                if operationSelection == WITHDRAW:
                    withdrawal_operation(customer)
                elif operationSelection == BALANCE:
                    print("Twój stan konta wynosi", customer.balance)
                    break
                elif operationSelection == END:
                    print("Dziękujemy, zapraszamy ponownie")
                    break
                else:
                    print("Nie wybrano poprawnej operacji, spróbuj ponownie:")
        else:
            print("Użytkownik zablokowany. Dziękujemy, zapraszamy ponownie")
    else:
        print("Nie poprawny indentyfikator.Zapraszamy ponownie")