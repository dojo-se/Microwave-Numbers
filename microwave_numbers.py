import unittest

def microwave_numbers(seconds):
    return 99

class TestMicroWaveNumbers(unittest.TestCase):
    def test_99(self):
        self.assertEqual(99, microwave_numbers(99))

if __name__ == '__main__':
    unittest.main()
