import unittest

KEYBOARD = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (None, 0, '*'))

def position(number)
    return None
    
def steps_between(postion_initial, position_final)
    return None
    
def microwave_numbers(seconds):
    s_distance = []
    for i in str(seconds)
        s_distance.append(position(i))
    
    minutes = seconds / 60
    seconds = seconds % 60
    minutes = minutes * 100
    minutes = minutes+seconds
    m_distance = []
    for i in str(minutes):
        m_distance.append(position(i))
    return 99

class TestMicroWaveNumbers(unittest.TestCase):
    def test_99(self):
        self.assertEqual(99, microwave_numbers(99))

if __name__ == '__main__':
    unittest.main()
