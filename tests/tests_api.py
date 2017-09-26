import unittest
from bandecoapi.api import get_menu
from bandecoapi.cardapio import Cardapio
from datetime import datetime


class TestArguments(unittest.TestCase):

    def test_menu_required(self):
        res = get_menu()
        self.assertFalse(res.get("menu", False))
        self.assertTrue(res.get("error", False))
        self.assertEqual(res["error"], "'menus' é um argumento obrigatório")

    def test_menus_type(self):
        res = get_menu(menus="invalid")
        self.assertFalse(res.get("menu", False))
        self.assertTrue(res.get("error", False))
        self.assertIn("'menus' tem que ser do tipo", res["error"])

    def test_menus_options_wrong_type(self):
        res = get_menu(menus=[{"wrong": "type"}, 42])
        self.assertFalse(res.get("menu", False))
        self.assertTrue(res.get("error", False))
        self.assertEqual(res["error"], "Os valores da lista 'menus' têm que ser strings")

    def test_menus_options_invalid(self):
        res = get_menu(menus=["invalid", "option"])
        self.assertFalse(res.get("menu", False))
        self.assertTrue(res.get("error", False))
        self.assertIn("não é uma opção menu válida", res["error"])

    def test_invalid_argument(self):
        res = get_menu(menus=["breakfast", "lunch"], invalid="argument")
        self.assertFalse(res.get("menu", False))
        self.assertTrue(res.get("error", False))
        self.assertIn("não é um argumento válido", res["error"])

    def test_invalid_argument_type(self):
        res = get_menu(menus=["breakfast", "lunch"], days_delta="invalid")
        self.assertFalse(res.get("menu", False))
        self.assertTrue(res.get("error", False))
        self.assertIn("não é um tipo válido para o argumento", res["error"])

    def test_menus_only(self):
        res = get_menu(menus=["breakfast", "lunch"])
        card = Cardapio()
        self.assertTrue(res.get("menu", False))
        self.assertFalse(res.get("error", False))
        self.assertIsInstance(res.get("menu", False), dict)
        self.assertIsInstance(res["menu"].get("breakfast", False), str)
        self.assertIsInstance(res["menu"].get("lunch", False), str)
        self.assertNotIsInstance(res["menu"].get("veglunch", False), str)
        self.assertNotIsInstance(res["menu"].get("dinner", False), str)
        self.assertNotIsInstance(res["menu"].get("vegdinner", False), str)

        self.assertEqual(res["menu"]["breakfast"], card.breakfast)
        self.assertEqual(res["menu"]["lunch"], card.lunch)

    def test_menus_days(self):
        res = get_menu(menus=["breakfast", "lunch"], days_delta=1)
        card = Cardapio(days_delta=1)
        self.assertTrue(res.get("menu", False))
        self.assertFalse(res.get("error", False))
        self.assertIsInstance(res.get("menu", False), dict)
        self.assertIsInstance(res["menu"].get("breakfast", False), str)
        self.assertIsInstance(res["menu"].get("lunch", False), str)
        self.assertNotIsInstance(res["menu"].get("veglunch", False), str)
        self.assertNotIsInstance(res["menu"].get("dinner", False), str)
        self.assertNotIsInstance(res["menu"].get("vegdinner", False), str)

        self.assertEqual(res["menu"]["breakfast"], card.breakfast)
        self.assertEqual(res["menu"]["lunch"], card.lunch)

    def test_menus_hours(self):
        res = get_menu(menus=["breakfast", "lunch"], hours_delta=25)
        card = Cardapio(hours_delta=25)
        self.assertTrue(res.get("menu", False))
        self.assertFalse(res.get("error", False))
        self.assertIsInstance(res.get("menu", False), dict)
        self.assertIsInstance(res["menu"].get("breakfast", False), str)
        self.assertIsInstance(res["menu"].get("lunch", False), str)
        self.assertNotIsInstance(res["menu"].get("veglunch", False), str)
        self.assertNotIsInstance(res["menu"].get("dinner", False), str)
        self.assertNotIsInstance(res["menu"].get("vegdinner", False), str)

        self.assertEqual(res["menu"]["breakfast"], card.breakfast)
        self.assertEqual(res["menu"]["lunch"], card.lunch)

    def test_menus_date(self):
        d = datetime.today().strftime('%Y-%m-%d')
        res = get_menu(menus=["breakfast", "lunch"], date=d)
        card = Cardapio(date=d)
        self.assertTrue(res.get("menu", False))
        self.assertFalse(res.get("error", False))
        self.assertIsInstance(res.get("menu", False), dict)
        self.assertIsInstance(res["menu"].get("breakfast", False), str)
        self.assertIsInstance(res["menu"].get("lunch", False), str)
        self.assertNotIsInstance(res["menu"].get("veglunch", False), str)
        self.assertNotIsInstance(res["menu"].get("dinner", False), str)
        self.assertNotIsInstance(res["menu"].get("vegdinner", False), str)

        self.assertEqual(res["menu"]["breakfast"], card.breakfast)
        self.assertEqual(res["menu"]["lunch"], card.lunch)


def run_tests():
    unittest.main()


if __name__ == '__main__':
    run_tests()
