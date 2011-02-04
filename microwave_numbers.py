import unittest

KEYBOARD = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (None, 0, '*'))

def position(number):
    for index, tuple_ in enumerate(KEYBOARD):
        try:
            return (index, tuple_.index(number))
        except ValueError:
            pass
    
def steps_between(position_initial, position_final):
    return None
    
def microwave_numbers(seconds):
    s_distance = []
    for i in str(seconds):
        s_distance.append(position(i))
    
    minutes, seconds = divmod(seconds, 60)
    minutes = minutes * 100
    minutes = minutes + seconds
    m_distance = []
    for i in str(minutes):
        m_distance.append(position(i))
    print s_distance, m_distance
    return 99

class TestMicroWaveNumbers(unittest.TestCase):
    def test_99(self):
        self.assertEqual(99, microwave_numbers(99))

if __name__ == '__main__':
    unittest.main()
