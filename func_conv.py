def conv_in_curr(r):
    if r:
        try:
            a = float(r)
            usd_rub = 77.59
            eur_rub = 88.05
            chf_rub = 85.1
            gbp_rub = 105.17
            cny_rub = 12.24
            print('Ты ввёл', a, 'руб.')
            curr_course = [usd_rub, eur_rub, chf_rub, gbp_rub, cny_rub]
            curr_values = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
            if a >= 0:
                for i in range(len(curr_values)):
                    print('Конвертированная сумма в', curr_values[i], ' = ', round((a / curr_course[i]), 2))
            else:
                print('Введите положительное число.')
        except ValueError:
            print('Вы ввели не число. Введите число.')
    else:
        print('Вы ввели пустое поле. Введите число.')

def conv_manual_curr(z):
    usd_rub = 77.59
    eur_rub = 88.05
    chf_rub = 85.1
    gbp_rub = 105.17
    cny_rub = 12.24
    curr_course = [usd_rub, eur_rub, chf_rub, gbp_rub, cny_rub]
    curr_values = ['USD', 'EUR', 'CHF', 'GBP', 'CNY']
    if z:
        for i in range(len(curr_values)):
            if z == curr_values[i]:
                    print('Введите сумму в рублях')
                    b = str.strip(input())
                    if b:
                        try:
                            a = float(b)
                            if a >= 0:
                                result = round((a / curr_course[i]), 2)
                                print('Вы ввели сумму в размере', a, 'руб. и валюту - ', curr_values[i], '\nконвертированная сумма в', curr_values[i], '=', result)
                                break
                            else:
                                print('Введите положительное число после выбора валюты.')
                                break
                        except ValueError:
                            print('Вы ввели не число. Введите число после выбора валюты.')
                            break
                    else:
                        print('Вы ввели пустое поле. Введите сумму после выбора валюты.')
                        break
            elif z != curr_values[i] and i < (len(curr_values)-1):
                continue
            else:
                print('unknown currency')
                break
    else:
        print('Вы ввели пустое поле или пробел. Введите название валюты.')
