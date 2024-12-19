import unittest
from unittest.mock import patch
import time

# Assume the math_game function is in a file called `math_game.py`
from game import math_game

class TestMathGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['3', '5', '12', '18', '6', '9', '7'])  # Simulate user inputs
    @patch('builtins.print')  # Mock print to suppress output in tests
    @patch('random.randint', side_effect=[1, 2, 3, 4, 2, 3, 5])  # Simulate random number generation
    @patch('random.choice', side_effect=['+', '-', '*'])  # Simulate random operator selection
    def test_math_game(self, mock_input, mock_print, mock_randint, mock_choice):
        # Mock time to simulate a 30-second time limit
        start_time = time.time()
        with patch('time.time', side_effect=[
            start_time, start_time + 2, start_time + 5, start_time + 10,
            start_time + 20, start_time + 25, start_time + 31
        ]):
            math_game()

        # Verify correct outputs
        # First question: 1 + 2 = 3
        mock_print.assert_any_call("Was ist 1 + 2?")
        mock_print.assert_any_call("Richtig!")

        # Second question: 3 - 4 = -1 (user answered 5)
        mock_print.assert_any_call("Was ist 3 - 4?")
        mock_print.assert_any_call("Falsch! Die richtige Antwort ist -1.")

        # Third question: 2 * 3 = 6 (user answered 12)
        mock_print.assert_any_call("Was ist 2 * 3?")
        mock_print.assert_any_call("Falsch! Die richtige Antwort ist 6.")

        # Verify game ends after time limit
        mock_print.assert_any_call("Zeit vorbei! Du hast 1 Aufgaben richtig gelöst.")

if __name__ == "__main__":
    unittest.main()
