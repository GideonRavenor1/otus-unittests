from factories import InsertionSortFactory, MergeSortFactory, SelectionSortFactory

array = [
    28, 52, 71, 94, 46, 4, 28, 96, 10, 83, 21, 85, 47, 32, 94, 82, 9, 87, 7, 80, 63, 57, 19, 7, 22, 72, 40, 92,
    50, 84, 17, 35, 84, 32, 17, 46, 73, 17, 57, 57, 9, 25, 87, 40, 79, 33, 12, 52, 27, 67
]
sorted_array = [
    4, 7, 7, 9, 9, 10, 12, 17, 17, 17, 19, 21, 22, 25, 27, 28, 28, 32, 32, 33, 35, 40, 40, 46, 46, 47, 50, 52,
    52, 57, 57, 57, 63, 67, 71, 72, 73, 79, 80, 82, 83, 84, 84, 85, 87, 87, 92, 94, 94, 96
]


def test_sort_factories():
    # Тест для фабрики сортировки выбором
    factory = SelectionSortFactory()
    sorter = factory.create_sort()
    assert sorter.execute(array) == sorted_array
    
    # Тест для фабрики сортировки вставками
    factory = InsertionSortFactory()
    sorter = factory.create_sort()
    assert sorter.execute(array) == sorted_array
    
    # Тест для фабрики сортировки слиянием
    factory = MergeSortFactory()
    sorter = factory.create_sort()
    assert sorter.execute(array) == sorted_array
