import unittest
from unittest import mock
from monty_hall import play_game_stay, play_game_switch


class TestMonty(unittest.TestCase):

    @mock.patch('random.randint')
    def test_assert_true_stay(self, mock_random):
        mock_random.return_value = 1
        self.assertTrue(play_game_stay(['goat', 'Cadillac', 'goat']))

    @mock.patch('random.randint')
    def test_assert_false_stay(self, mock_random):
        mock_random.return_value = 2
        self.assertFalse(play_game_stay(['goat', 'Cadillac', 'goat']))

    @mock.patch('random.randint')
    def test_assert_true_switch(self, mock_random):
        mock_random.return_value = 2
        self.assertTrue(play_game_switch(['Cadillac', 'goat', 'goat']))

    @mock.patch('random.randint')
    def test_assert_false_switch(self, mock_random):
        mock_random.return_value = 0
        self.assertFalse(play_game_switch(['Cadillac', 'goat', 'goat']))


if __name__ == '__main__':
    unittest.main()
