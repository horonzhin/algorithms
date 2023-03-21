if __name__ == '__main__':

    # Бинарный поиск минимального платежа, чтобы закрыть долг за 12 месяцев

    balance = 320000
    annualInterestRate = 0.2

    init_balance = balance
    monthlyInterestRate = annualInterestRate / 12
    lower = init_balance / 12
    upper = (init_balance * (1 + monthlyInterestRate) ** 12) / 12.0
    epsilon = 0.03

    while abs(balance) > epsilon:
        monthlyPaymentRate = (upper + lower) / 2
        balance = init_balance
        for i in range(12):
            balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
        if balance > epsilon:
            lower = monthlyPaymentRate
        elif balance < -epsilon:
            upper = monthlyPaymentRate
        else:
            break
    print('Lowest Payment:', round(monthlyPaymentRate, 2))

    # Расчет остатка долга, если платить минимальный процент погашения по сумме долга

    balance = 42
    annualInterestRate = 0.2
    monthlyPaymentRate = 0.04

    for i in range(12):
        balance = balance - (balance * monthlyPaymentRate) + (
                    (balance - (balance * monthlyPaymentRate)) * (annualInterestRate / 12))
    print("Remaining balance:", round(balance, 2))
