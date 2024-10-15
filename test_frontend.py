import unittest
from unittest.mock import patch, MagicMock
from frontend import Frontend  # Import the Frontend class from frontend.py

class TestFrontendSimplified(unittest.TestCase):

    def setUp(self):
        self.frontend = Frontend()  # Set up an instance of Frontend class
        self.player = MagicMock()   # Create a mock player object
        self.player.battle_pokemon = ["Pikachu", 100, 50]  # Example Pokémon data

    @patch('frontend.random.randint', return_value=3)
    def test_apply_poison_effect(self, mock_randint):
        self.frontend.apply_effect("poison", 2, "Pikachu", 50, self.player)
        self.assertEqual(self.player.battle_pokemon[2], 44)  # 50 - (3 * 2) = 44

    @patch('frontend.random.randint', return_value=3)
    def test_apply_potion_effect(self, mock_randint):
        self.frontend.apply_effect("potion", 2, "Pikachu", 50, self.player)
        self.assertEqual(self.player.battle_pokemon[2], 56)  # 50 + (3 * 2) = 56

    @patch('builtins.input', return_value="yes")
    @patch('frontend.random.choice', return_value="poison")
    @patch('frontend.Frontend.get_valid_user_input', return_value=2)
    @patch('frontend.Frontend.show_progress')  # Skip progress bar display
    def test_poison_or_potion(self, mock_progress, mock_user_input, mock_choice, mock_input):
        self.frontend.poison_or_potion(self.player)
        self.assertEqual(self.player.battle_pokemon[2], 44)  # Poison applied

if __name__ == '__main__':
    unittest.main()
