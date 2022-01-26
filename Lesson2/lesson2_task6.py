# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = []
while input("Хотите добавить товар? Введите да/нет: ") == 'да':
    number = int(input("Введите номер продукта: "))
    features = {}
    while input("Хотите добавить характеристики продукта? Введите да/нет: ") == 'да':
        feature_key = input("Введите наименование характеристики продукта: ")
        feature_value = input("Введите значение характеристики продукта: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
# goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitica = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitica:
            analitica[feature_key].append(feature_value)
        else:
            analitica[feature_key] = [feature_value]
print(analitica)
