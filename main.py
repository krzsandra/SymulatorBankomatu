from customer import *
from ATMfunctions import *


if __name__ == '__main__':
    atmBalance = 1000
    WITHDRAWAL = 1
    BALANCE = 2
    END = 3
    operations_dict = {WITHDRAWAL: "Wypłata",
                       BALANCE: "Sprawdzenie salda konta",
                       END: "Zakończ pracę z bankomatem"}

    customer01 = Customer(10, 5236, 150)
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

    print("Witaj w SYMULATORZE BANKOMATU")
    idEntered = int(input("Proszę o podanie indentyfikatora klienta:"))
    customer = find_customer(idEntered, customersList)
    if customer:
        if check_pin(customer):
            operationSelection = 4
            while operationSelection > END or operationSelection <= 0:
                operationSelection = operation_selection(operations_dict)
                if operationSelection == WITHDRAWAL:
                    withdrawal_operation(customer, atmBalance)
                    print("Dziękujemy, zapraszamy ponownie")
                elif operationSelection == BALANCE:
                    print("Twój stan konta wynosi", customer.balance)
                    print("Dziękujemy, zapraszamy ponownie")
                    break
                elif operationSelection == END:
                    print("Dziękujemy, zapraszamy ponownie")
                    break
                else:
                    print("Nie wybrano poprawnej operacji, spróbuj ponownie:")
        else:
            print("Pin niepoprawny.Wykorzystałeś dostępne próby.\nDziękujemy, zapraszamy ponownie")
    else:
        print("Niepoprawny indentyfikator.\nDziękujemy, zapraszamy ponownie")