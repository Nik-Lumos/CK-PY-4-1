def delete(list_, index=None):
    if index is None or index == -1:  # Случай, когда удаляем последний элемент
        return list_[:-1]
    else:  # Случай для остальных заданных положит. и отриц. величин индекса
        return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
