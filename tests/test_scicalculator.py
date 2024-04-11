import unittest
from src.scicalculator import SciCalculator

class TestSciCalculator(unittest.TestCase):
    def test_square_root_correct_input(self):
        # Arrange
        scicalculator = SciCalculator()
        x = 9
        expected_result = 3
        # Act
       
        result = scicalculator.square_root(x)
        
        # Assert
        self.assertEqual(result, expected_result)

    def test_square_with_correct_input(self):
        # Arrange
        scicalculator = SciCalculator()
        x = 4
        
        # Act
        expected_result = 16
        result = scicalculator.square(x)
        
        # Assert
        self.assertEqual(result, expected_result)   

 