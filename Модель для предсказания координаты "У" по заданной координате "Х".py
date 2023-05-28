"""
1) Ваша задача — построить модель[1], которая может предсказывать координату y.
Вы можете пройти тесты, если прогнозируемые координаты y находятся в пределах погрешности.

Вы получите комплект train, который нужно использовать для сборки модели.
После того, как вы создадите модель, тесты будут вызывать функцию predict и передавать ей x.

Ошибка будет рассчитана с помощью RMSE
Нельзя использовать библиотеки: sklearn, pandas, tensorflow, numpy, scipy

example_train_set = [(0, 1), (2, 2), (4, 3), (9, 8), (3, 5)]

predicted = [dm.predict(point[0]) for point in example_test_set]

Объяснение:

[1] Модель интеллектуального анализа данных создается путем применения алгоритма к данным,
но это больше, чем алгоритм или контейнер метаданных: это набор данных, статистики и шаблоны,
которые можно применять к новым данным для создания прогнозов и выводов о взаимосвязях.

"""
# Для построения модели через точки с извесными координатами проведем аппроксимирующую прямую.
# Для построения прямой (вычисления коэффициентов a, b для функции y = a*x + b)
# воспользуемся методом наименьших квадратов

example_train_set = [(0, 1), (2, 2), (4, 3), (9, 8), (3, 5)]


def coef_calculate_(train: list) -> tuple:
    average_x = 0
    average_y = 0
    average_xy = 0
    average_xx = 0
    for point in train:
        average_x += point[0]
        average_y += point[1]
        average_xy += point[0] * point[1]
        average_xx += point[0] ** 2
    average_x = average_x / len(train)
    average_y = average_y / len(train)
    average_xy = average_xy / len(train)
    average_xx = average_xx / len(train)
    d_x = average_xx - average_x ** 2
    a = (average_xy - average_x * average_y) / d_x
    b = average_y - a * average_x
    return a, b


def rmse_calculate_(train: list) -> float:
    from math import sqrt
    average_y = float()
    rmse = list()
    for point in train:
        average_y += point[1]
    average_y = average_y / len(train)
    for point in train:
        rmse.append((point[1] - average_y) ** 2)
    rmse = sum(rmse) / len(rmse)
    return sqrt(rmse)



def predict(x_real):
    (a, b) = coef_calculate_(example_train_set)
    y_predict = a * x_real + b
    return round(y_predict)


print("Для вашего значения 'х', предсказанная координата 'у' = ", predict(20))
print(coef_calculate_(example_train_set))
print(rmse_calculate_(example_train_set))
