from task_3 import rus_list, geo_ids_get, count_words, geo_logs, ids, queries

#1 задание
def test_rus_list():
    res = rus_list(geo_logs)
    assert [
        {'visit1': ['Москва', 'Россия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ] == res

test_rus_list()

#2 задание
def test_geo_ids_get():
    for res_item, check_item in zip(
            geo_ids_get(ids),
            [[213, 213, 213, 15, 213], [54, 54, 119, 119, 119], [213, 98, 98, 35]]
    ):
        assert res_item == check_item

test_geo_ids_get()

#3 задание
def test_count_words():
    count_block = 7
    count_2 = round(3 * 100 / count_block)
    count_3 = round(4 * 100 / count_block)
    result = count_words(queries)
    for res_item, check_item in zip(
        result,
        [count_2, count_3]
    ):
        assert res_item == check_item


test_count_words()

