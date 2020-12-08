from unittest import TestCase

from src.potential_selections_generator import generate_all_possible_selections


class TestGenerate_all_possible_selections(TestCase):
    def test_generate_all_possible_selections(self):
        players = ["Billy", "Bob"]
        selections = generate_all_possible_selections(players)
        self.assertEqual(2, len(selections))
        for select in selections:
            self.assertEqual(1, len(select.black))
            self.assertEqual(1, len(select.white))

    def test_generate_all_possible_selections_odd(self):
        players = ["Billy", "Bob", "Jimmy"]
        selections = generate_all_possible_selections(players)
        self.assertEqual(3, len(selections))
        for select in selections:
            self.assertEqual(3, len(select.black + select.white))

    def test_generate_all_possible_selections_four(self):
        players = ["Billy", "Bob", "Jimmy", "Damo"]
        selections = generate_all_possible_selections(players)
        self.assertEqual(6, len(selections))
        for select in selections:
            self.assertEqual(4, len(select.black + select.white))
