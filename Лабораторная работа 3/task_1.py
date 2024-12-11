# TODO Напишите функцию для поиска индекса товара


#items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

#for find_item in ['банан', 'груша', 'персик']:
   # index_item = ...  # TODO Вызовите функцию, что получить индекс товара
   # if index_item is not None:
     #   print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
   # else:
    #    print(f"Товар '{find_item}' не найден в списке.")

# Я пытаюсь написать функцию, чтобы найти индекс товара в списке. Программа должна сказать, если товара нет.

def find_item_index(product_list, item_to_find):
    # Перебираем все товары в списке
    for index, product in enumerate(product_list):
        # Если мы нашли товар, возвращаем его индекс
        if product == item_to_find:
            return index
    # Если товара нет, возвращаем None
    return None

# Мой список товаров
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Я хочу узнать, где находятся некоторые товары
for find_item in ['банан', 'груша', 'персик']:
    # Вызываю функцию, чтобы получить индекс товара
    index_item = find_item_index(items_list, find_item)
    # Проверяю, нашел ли я индекс
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")