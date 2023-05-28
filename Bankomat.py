"""
            Банкомат

Есть валюты:  currencies = [RUB, USD, EUR]

Монеты/купюры каждой валюты бывают только такого номинала:
    nominals = [5000, 1000, 500, 100, 50, 10, 5, 1]

Нужно разработать программу "Банкомат" со следующими возможностями:

Принять в банкомат несколько монет/купюр:
    put(currensy, nominal, count) -> None

Выдать из банкомата определенную сумму денег в определенной валюте:
    get(currency, amount) -> [(nominal, count), ...]| raise UnavailableError

Ответом должен быть список, каким образом банкомат выдаст нужную сумму,
какими монетами/купюрами, в каком количестве.

Банкомат может выдать только то, что в него положили.
Если выдать требуемую сумму нет возможности - вызываем исключение UnavailableError.

"""

class UnavailableError(Exception):
    def err_message(self):
        return 'UnavailableError'


currencies = ['RUB', 'USD', 'EUR']  # Список валют
nominals = ['5000', '1000', '500', '100', '50', '10', '5', '1']  # Список номиналов валют
storage = dict()  # Переменная для хранения типа валют, номиналов валют и количества банкнот каждого номинала
for currency in currencies:
    storage[currency] = dict()
    for nominal in nominals:
        storage[currency][nominal] = 0  # Цикл создает пустое хранилище банкомата


# Принять в банкомат несколько монет/купюр одной валюты и номинала:
def put(currency: str, nominal: str, count: int) -> None:
    if valid_money(currency, nominal):
        storage[currency][nominal] += count
        return storage


# Проверка вносимых банкнот на соответствие
def valid_money(currency: str, nominal: str) -> bool:
    if currency in currencies and nominal in nominals:
        return True
    else:
        print('Вносимые валюты/номиналы валюты не определены')
        return False

# Проверка на возможность выдать из банкомата определенную сумму денег в определенной валюте:
def check(currency: str, amount: int) -> dict:
    payout = dict()
    amount = int(amount)

    for nominal in nominals:
        if amount < int(nominal) or storage[currency][nominal] == 0:
            continue

        count = amount // int(nominal)

        if storage[currency][nominal] < count:
            count = storage[currency][nominal]

        payout[nominal] = count
        amount -= count * int(nominal)

        if amount == 0:
            return payout
    if amount > 0:
        raise UnavailableError


def get(currency: str, amount: int) -> list:
    payout = check(currency, amount)
    payout_list = list()
    if payout:
        for key, value in payout.items():
            storage[currency][key] -= value
            payout_list.append((currency, key, value))
        return payout_list




print(put('RUB', '1', 10))
print(put('RUB', '5', 10))
print(put('RUB', '10', 10))
print(put('RUB', '50', 10))
print(put('RUB', '100', 10))
print(put('RUB', '500', 10))
print(put('RUB', '1000', 10))
print(put('RUB', '5000', 10))

print(get('RUB', 55000))
print(storage)
print(get('RUB', 11250))
print(storage)
