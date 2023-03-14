import unittest
from API_ya import Yandex
from TOKEN import TOKEN



class TestYandex(unittest.TestCase):

    def test_find_folder(self):
        self.assertTrue(Yandex(TOKEN).find_folder('new_file') == 200)
        print(f'Файл найден')

    def test_not_find_folder_(self):
        self.assertAlmostEqual(Yandex(TOKEN).find_folder('new_file'), 404)
        print(f'Не удалось найти запрошенный ресурс')

    def test_not_acces(self):
        self.assertNotEqual(Yandex(TOKEN).find_folder('new_file'), 503)
        print(f'Сервис доступен')

if __name__ == "__main__":
    unittest.main()
