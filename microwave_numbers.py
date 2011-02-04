import unittest

KEYBOARD = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (None, 0, '*'))

def position(number):
    for row, col in enumerate(KEYBOARD):
        try:
            return row, col.index(int(number))
        except ValueError:
            pass
    
def steps_between(position_initial, position_final):
    effort_between_rows = abs(position_initial[0] - position_final[0])
    effort_between_cols = abs(position_initial[1] - position_final[1])
    return effort_between_cols + effort_between_rows
    
def microwave_numbers(seconds):
    s_distance = []
    for i in str(seconds):
        s_distance.append(position(i))

    s_effort = 0
    for j in range(len(s_distance)-1):
        s_effort += steps_between(s_distance[j], s_distance[j+1])
    
    minutes = reduce(lambda x,y: x*100+y, divmod(seconds, 60))
    
    m_distance = []
    for i in str(minutes):
        m_distance.append(position(i))

    m_effort = 0
    for j in range(len(m_distance)-1):
        m_effort += steps_between(m_distance[j], m_distance[j+1])
    
    if s_effort < m_effort:
        return seconds
    else:
        return minutes

class TestMicroWaveNumbers(unittest.TestCase):
    def test_99(self):
        self.assertEqual(99, microwave_numbers(99))
    def test_71(self):
        self.assertEqual(111, microwave_numbers(71))
    def test_1(self):
        self.assertEqual(1, microwave_numbers(1))
    def test_120(self):
        self.assertEqual(200, microwave_numbers(120))
    def test_123(self):
        self.assertEqual(123, microwave_numbers(123))

if __name__ == '__main__':
    unittest.main()
